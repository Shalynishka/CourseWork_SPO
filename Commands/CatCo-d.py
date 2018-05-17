from Handler import CommandHandler
import vkapi


def cat():
    #Получаем случайную картинку из паблика(явно котики)

    attachment = vkapi.get_random_wall_picture(-33621085)
    message = 'Вот тебе котяра. Наслаждайся'
    return message, attachment


cat_command = CommandHandler.Command()
cat_command.keys = ['котик', 'котяра', 'котэ', 'кот', 'cat']
cat_command.description = 'Покажу котика'
cat_command.process = cat
