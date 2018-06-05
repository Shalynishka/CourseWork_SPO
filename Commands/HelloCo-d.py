from Handler import command_handler
import random
helloAnswer = {1: 'Hello', 2: 'Привет', 3: 'Здорово!', 4:  'Доброго времени суток!', 5: 'Хай', 6: 'Хаюшки', 7: 'Мое почтение', 8: 'Здря', 9: 'Дороу', 10: 'Hi'}


class Hello:
    def __init__(self):
        hello_command = command_handler.Command()
        hello_command.keys = ['привет', 'день добрый!', 'хай', 'вечер в хату', 'дороу', 'hello', 'хаюшки']  # 6
        hello_command.description = 'Поздороваюсь'
        hello_command.process = Hello.hello

    @staticmethod
    def hello(*args):
        message = helloAnswer.get(random.randint(1,10))
        return message, ''


Hello()

