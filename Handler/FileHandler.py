from Handler.file_handler import FileWork
import vk_api

host = '153466186'


class Admin:
    @staticmethod
    def choose_command(data, token):
        if '//spam' in data:
            Admin.spam(data[6:], token)
        elif '//users' in data:
            Admin.show_users(token)
        else:
            attachment = ''
            mess = 'Команда не определена: ' + data
            vk_api.send_messages(host, token, mess, attachment)

    @staticmethod
    def spam(mes, token):
        attachment = ''
        list_to_spam = FileWork.get_user_list()
        for l in list_to_spam:
            user_id0 = l
            if user_id0 == host:
                continue
            else:
                try:
                    vk_api.send_messages(user_id0, token, mes, attachment)
                except Exception as ex:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    wrong = template.format(type(ex).__name__, ex.args)
                    message = '\n' + 'Ошибка спама:\n' + 'vk.com/id' + str(user_id0) + '\nзабанил нас\n'  + wrong
                    FileWork.delete_user(user_id0)
                    vk_api.send_messages(host, token, message, attachment)
        vk_api.send_messages(host, token, 'Сделано', attachment)

    @staticmethod
    def show_users(token):
        attachment = ''
        list_to_spam = FileWork.get_user_list()
        message = 'Users:\n'
        i = 1
        for l in list_to_spam:
            user_id0 = l
            if user_id0 == host:
                continue
            else:
                message = message + str(i) + ': ' + 'vk.com/id' + str(l) + '\n'
                i += 1
        vk_api.send_messages(host, token, message, attachment)
