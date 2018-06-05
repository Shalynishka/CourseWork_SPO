from Handler import command_handler


class Info:
    def __init__(self):
        info_command = command_handler.Command()
        info_command.keys = ['помощь', 'нужна помощь', 'помоги', 'help', 'я тупой']
        info_command.description = 'Покажу список команд'
        info_command.process = Info.info

    @staticmethod
    def info():
        message = ''
        for c in command_handler.command_list:
            message += c.keys[0] + ' - ' + c.description + '\n'
        return message, ''

# if u wanna be my friend, create new object. Without it doesn't work!!!!!


Info()

