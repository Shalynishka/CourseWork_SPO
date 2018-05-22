#принимает сообщение пользователя, обрабатывает его
#changed 21.05.18, изменена обработка ошибки с файлом. Organizer
import vkapi
import os
import random
import importlib
from Handler.CommandHandler import command_list
from Handler.FileHandler import add_user
from Handler.adminHandler import choose_command
host = 153466186
problemMessage = {1: 'Прости, не понимаю тебя.', 2: 'Сорян, не разбираю твои каракули', 3: 'Трудности перевода, воспользуйся помощью', 4: 'Я не ИИ, пиши по ГОСТу'}


# парсим сообщение и выбираем, что сделать
def get_answer(body, user_id):
    message = problemMessage.get(random.randint(1, 4))
    attachment = ''
    # необходимо сделать файл, тогда разграничим две функции
    for c in command_list:
        for d in c.keys:
            if d in body:
                message, attachment = c.process(body, user_id)
        #if body in c.keys:
    return message, attachment


# получили сообщение и делаем штуки с ним
def create_answer(data, token):
    # загрузить модули
    load_modules()
    # добавить пользователя
    user_id = data['user_id']
    try:
        add_user(user_id)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        wrong = template.format(type(ex).__name__, ex.args)
        error_message = 'Ошибка добавления пользователя:\n' + wrong
        vkapi.send_messages(host, token, error_message, '')
    finally:
        if '/' == data['body'].lower()[1]:
            if user_id != host:
                vkapi.send_messages(user_id, token, 'Нет доступа к командам', '')
            else:
                choose_command(data['body'], token)
            data['body'] = 'wat'
        else:
            message, attachment = get_answer(data['body'].lower(), user_id)
            vkapi.send_messages(user_id, token, message, attachment)


def load_modules():
    files = os.listdir("mysite/Commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("Commands." + m[0:-3])

