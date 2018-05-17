from Handler import CommandHandler


def hello():
    message = 'Hello, i\'m bot\n Do u now de way?'
    return message, ''


hello_command = CommandHandler.Command()
hello_command.keys = ['привет', 'день добрый!', 'хай', 'вечер в хату', 'дороу', 'hello'] #6
hello_command.description = 'Поздороваюсь'
hello_command.process = hello
