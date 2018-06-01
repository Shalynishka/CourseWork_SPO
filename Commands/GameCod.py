from Handler import CommandHandler
import requests
import random

word_check_url = 'https://speller.yandex.net/services/spellservice.json/checkText?text={}'

answers_for_start = {1: 'Поиграем!', 2: 'Готовьте пушк.., кхе-кхе, словари! Пора за дело!',
                     3: 'Да тебе меня не победить!'}

answers_for_lose = {1: 'Ты проиграл :с Вот твой результат: {}',
                    2: 'Поражение! Твой результат: {}. Не волнуйся, в следующий раз победишь.'}

answers_for_end = {1: 'Твой результат {}. Заходи еще :)', 2: 'Устал поди. Отдыхай, твой результат {}.'}

answers_for_win = {1: 'А ты крепкий орешек. Вот твой результат {} и возьми пирожок с полки.',
                   2: 'Ты победил :с Твой результат {}.'}

bad_let = ['ъ', 'ы', 'ь']

file_way = '/home/NikitaKotikov/mysite/Commands/letters/'

gamers = dict()


class GameChecker:
    def __init__(self, user_id):
        self.__user_id = user_id
        self.__useless_words = list()
        self.__result = 0

    # вернет id игрока
    @property
    def user_id(self):
        return self.user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    # @property
    def get_result(self):
        return self.__result

    # покажет использованные слова
    def show_useless(self):
        print(self.__useless_words)
        pass

    # увеличивает результат
    def up_result(self):
        self.__result += 1
        pass

    # добавляет использованное слово
    def add_useless(self, word):
        self.__useless_words.append(word)

    # проверка слова на правильность и существование
    def check_word_ex(self, s):
        answer = requests.get(word_check_url.format(s)).json()
        if answer == list():
            return 'ok'
        else:
            return 'bad'

    # проверка на вхождение слова в использованные слова
    def check_useless_word(self, s):
        if s in self.__useless_words:
            return 'bad'
        else:
            return 'ok'

        # проверка на первую букву слова игрока
    def check_last_letter(self, letter):
        if self.__useless_words.__len__() == 0:
            return 'ok'
        word = list(self.__useless_words[-1])
        word.reverse()
        for l in word:
            if l in bad_let:
                continue
            # е и ё по правилам одинаковы
            if l == 'ё' and letter == 'е' or letter == 'ё' and l == 'е':
                return 'ok'
            if l != letter:
                return 'bad'
            return 'ok'

    def get_last_letter(self, word):
        word_ls = list(word)
        word_ls.reverse()
        for l in word_ls:
            if l in bad_let:
                continue
            # е и ё по правилам одинаковы
            if l == 'ё':
                return 'е'
            return l


def game(*args):
    body = args[0]
    user_id = args[1]
    if user_id not in gamers:
        gamers[user_id] = GameChecker(user_id)
        return 'Правила: пиши существительные. Хотя я плохо знаю части речи, но учти: я проверю тебя на вшивость. ' \
               'Ошибка в слове карается поражением. ' \
               'Повторение слова тоже карается поражением. ' \
               'Буква ё будет считаться за е\nЕсли захочешь закончить игру, напиши end\n' + answers_for_start[random.randint(1, 3)], ''
    else:
        g = gamers[user_id]
        # игрок захотел завершить игру
        if body == 'end':
            res = answers_for_end.format(str(g.get_result()))
            del g
            gamers.pop(user_id)
            return res, ''
        # игрок ввел слово не на ту букву
        if g.check_last_letter(body[0]) == 'bad':
            res = 'Не та буква!\n' + answers_for_lose[random.randint(1, 2)].format(str(g.get_result()))
            del g
            gamers.pop(user_id)
            return res, ''
        # игрок ввел неправильное или несуществующее слово
        if g.check_word_ex(body) == 'bad':
            res = 'В слове ошибка! Ну или ты просто слова выдумываешь\n' + answers_for_lose[random.randint(1, 2)].\
                format(str(g.get_result()))
            del g
            gamers.pop(user_id)
            return res, ''
        # игрок ввел слово, которое уже было
        if g.check_useless_word(body) == 'bad':
            res = 'Такое слово уже было!' + answers_for_lose[random.randint(1, 2)].format(str(g.get_result()))
            del g
            gamers.pop(user_id)
            return res, ''
        # запомнили это слово
        g.add_useless(body)
        last_let = g.get_last_letter(body)
        words = list()
        with open(file_way + last_let + '.txt', 'rt') as f:
            for line in f:
                words.append(line)
            # если после 5-ой попытки бот не найдет подходящее слово, то он проиграл
            i = 5
            length = words.__len__()
            while i > 0:
                try_word = words[random.randint(0, length - 1)][:-1]

                if g.check_useless_word(try_word) == 'bad':
                    i -= 1
                else:
                    g.add_useless(try_word)
                    g.up_result()
                    return try_word, ''
        f.close()
        del g
        gamers.pop(user_id)
        return answers_for_win[random.randint(1, 2)].format(str(g.get_result())), ''


game_command = CommandHandler.Command()
game_command.keys = ['/game']
game_command.description = 'Поиграем в слова'
game_command.process = game


def check_user(user_id):
    if user_id in gamers:
        return 'ok'
    else:
        return 'bad'
