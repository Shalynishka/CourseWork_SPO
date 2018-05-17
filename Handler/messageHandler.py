#принимает сообщение пользователя, обрабатывает его
#changed
import vkapi
import os
import importlib
from Handler.CommandHandler import command_list
from Handler.FileHandler import add_user
from Handler.adminHandler import choose_command


#вы звали меня?
def get_answer(body):
    message = "Сори, не понимаю тебя."
    attachment = ''
    for c in command_list:
        if body in c.keys:
            message, attachment = c.process()
    return message, attachment


def create_answer(data, token):
    flag = False
    wrong = ''
    load_modules()
    user_id = data['user_id']
    try:
        add_user(user_id)
    except Exception as ex:
        flag = True
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        wrong = template.format(type(ex).__name__, ex.args)
    finally:
        if '/' == data['body'].lower()[0]: #todo: divide into new file admin commands
            choose_command(data, token)
        else:
            message, attachment = get_answer(data['body'].lower())
            if flag is True:
                message += '\n' + 'Ошибка и я хз какая\n' + wrong
            vkapi.send_messages(user_id, token, message, attachment)


def load_modules():
    files = os.listdir("mysite/Commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("Commands." + m[0:-3])

