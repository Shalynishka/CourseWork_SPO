from Handler.FileHandler import get_user_list
import vkapi

host = '153466186'


def choose_command(data, token):
    if '/spam' in data['body']:
        spam(data['body'][6:], token)
    elif '/users' in data['body']:
        show_users(token)


def spam(mes_to_spam, token):
    attachment = ''
    list_to_spam = get_user_list()
    for l in list_to_spam:
        user_id0 = l
        if user_id0 == host:
            continue
        else:
            vkapi.send_messages(user_id0, token, mes_to_spam, attachment)


def show_users(token):
    attachment = ''
    list_to_spam = get_user_list()
    message = 'Users:\n'

    for l in list_to_spam:
        user_id0 = l
        if user_id0 == host:
            continue
        else:
            message = message + 'vk.com/id' + str(l) + '\n'
    vkapi.send_messages(user_id0, token, message, attachment)
