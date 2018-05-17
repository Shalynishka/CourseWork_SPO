from Handler import CommandHandler


def info():
    message = ''
    len = CommandHandler.command_list.__sizeof__()#######################
    for c in CommandHandler.command_list:
        message += c.keys[0] + '-' + c.description + '\n'+len
        return message, ''


info_command = CommandHandler.Command()
info_command.keys = ['помоги', 'помоги', 'help']
info_command.description = 'Покажу список команд'
info_command.process = info
