# принимает сообщение пользователя, обрабатывает его
# changed 21.05.18, изменена обработка ошибки с файлом. Organizer
import vk_api
import os
import random
import importlib
from Handler.command_handler import command_list
from Handler.file_handler import FileWork
from Handler.admin_handler import Admin
host = '153466186'
problemMessage = {1: 'Прости, не понимаю тебя.', 2: 'Сорян, не разбираю твои каракули', 3: 'Трудности перевода, воспользуйся помощью', 4: 'Я не ИИ, пиши по ГОСТу'}


class Answer:
    # парсим сообщение и выбираем, что сделать
    @staticmethod
    def get_answer(body, user_id):
        message = problemMessage.get(random.randint(1, 4))
        attachment = ''
        # необходимо сделать файл, тогда разграничим две функции
        for c in command_list:
            if body in c.keys:
                message, attachment = c.process(body, user_id)
        return message, attachment

    # получили сообщение и делаем штуки с ним
    @staticmethod
    def create_answer(data, token):
        # загрузить модули
        Answer.load_modules()
        # добавить пользователя
        user_id = data['user_id']
        try:
            FileWork.add_user(user_id)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            wrong = template.format(type(ex).__name__, ex.args)
            error_message = 'Ошибка добавления пользователя:\n' + wrong
            vk_api.send_messages(host, token, error_message, '')
        finally:
            if '/' == data['body'][1]:
                if user_id != host:
                    vk_api.send_messages(user_id, token, 'Нет доступа к командам', '')
                else:
                    Admin.choose_command(data['body'], token)
                # data['body'] = 'wat'
            else:
                message, attachment = Answer.get_answer(data['body'].lower(), user_id)
                vk_api.send_messages(user_id, token, message, attachment)

    @staticmethod
    def load_modules():
        files = os.listdir("mysite/Commands")
        modules = filter(lambda x: x.endswith('.py'), files)
        for m in modules:
            importlib.import_module("Commands." + m[0:-3])

