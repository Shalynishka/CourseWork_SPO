# изменино 21.05.18
from Handler.FileHandler import get_user_list
from Handler.FileHandler import delete_user
import vkapi

host = '153466186'


def choose_command(data, token):
    if '//spam' in data:
        spam(data[6:], token)
    elif '//users' in data:
        show_users(token)
    else:
        attachment = ''
        mess = 'Команда не определена: ' + data
        vkapi.send_messages(host, token, mess, attachment)


def spam(mes_to_spam, token):
    attachment = ''
    list_to_spam = get_user_list()
    for l in list_to_spam:
        user_id0 = l
        if user_id0 == host:
            continue
        else:
            try:
                vkapi.send_messages(user_id0, token, mes_to_spam, attachment)
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                wrong = template.format(type(ex).__name__, ex.args)
                message = '\n' + 'Ошибка спама:\n' + 'vk.com/id' + str(user_id0) + '\nзабанил нас\n'  + wrong
                delete_user(user_id0)
                vkapi.send_messages(host, token, message, attachment)
    vkapi.send_messages(host, token, 'Сделано', attachment)




def show_users(token):
    attachment = ''
    list_to_spam = get_user_list()
    message = 'Users:\n'
    i = 1
    for l in list_to_spam:
        user_id0 = l
        if user_id0 == host:
            continue
        else:
            message =message + str(i) + ': ' +  'vk.com/id' + str(l) + '\n'
            i += 1
    vkapi.send_messages(host, token, message, attachment)
