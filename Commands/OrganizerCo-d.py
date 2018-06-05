# added 21.05.18, 22.05 - команды имеют свой экземпляр. Имя команды изменено
# added 21.05.18
# 27.05.2018 changed: Формат команды. Многопоточность в трубу как и функция будильника
import datetime
from Handler import command_handler

alarms = dict()


class Organizer:
    def __init__(self):
        make_command = command_handler.Command()
        make_command.keys = ['/makeAlarm']
        make_command.description = '/makeAlarm: создам напоминалку'
        make_command.process = Organizer.add_alarm

        show_command = command_handler.Command()
        show_command.keys = ['/showAlarm']
        show_command.description = '/showAlarm: покажу текущую напоминалку'
        show_command.process = Organizer.show_alarms

        delete_command = command_handler.Command()
        delete_command.keys = ['/deleteAlarm']
        delete_command.description = '/deleteAlarm [N] - удалю напоминалку с номером N'
        delete_command.process = Organizer.delete_alarms

        delete_all_command = command_handler.Command()
        delete_all_command.keys = ['/deleteAll']
        delete_all_command.description = '/deleteAll - удалю все ваши напоминалки'
        delete_all_command.process = Organizer.delete_all

    @staticmethod
    # structure: day:hour:minute-message
    def add_alarm(*args):
        message = 'Напоминание создано'
        id_user = args[1]
        s = args[0][11:]
        try:
            d = Organizer.parse_date(s[:s.index('-')])
            if d == 0:
                raise ValueError
            # user_info =  + s[s.index('-') + 1:]
            user_info = (d, s[s.index('-') + 1:])
            # s = s[s.index('-') + 1:]
            if id_user in alarms.keys():
                alarms.get(id_user).append(user_info)
            else:
                alarms[id_user] = [user_info]
        except ValueError:
            message = 'Неверый формат команды. Правильный: [день]:[час]:[минута]-[сообщение]'
            # send_message: problem with date
        finally:
            print('message:' + message)
            return message, ''

    @staticmethod
    def show_alarms(*args):
        alarm = alarms.get(args[1])
        message = ''
        if alarm is None:
            return 'Нет текущих напоминалок', ''
        else:
            for c in alarm:
                message += c[0].strftime("%d числа, в %H:%M") + ' -> ' + c[1] + '\n'
            return message, ''

    @staticmethod
    def delete_alarms(*args):
        index = args[0][13:]
        if index.isdigit():
            print(int(index))
            try:
                if args[1] in alarms.keys():
                    alarms.get(args[1]).pop(int(index) - 1)
                    if alarms.get(args[1]) == list():
                        alarms.pop(args[1])
                    return 'Удалено', ''
                else:
                    return 'Нет ваших напоминалок', ''
            except IndexError:
                print('Ошибка. Неверный номер элемента.')
                return 'Ошибка. Неверный номер элемента.', ''
        else:
            print('Ошибка. Индекс должен состоять из цифр.')
            return 'Ошибка. Неверный номер элемента.', ''

    @staticmethod
    def delete_all(*args):
        if args[1] in alarms.keys():
            alarms.pop(args[1])
            return 'Напоминания удалены', ''
        else:
            return 'Нет ваших напоминалок', ''


Organizer()




