# added 21.05.18, 22.05 - команды имеют свой экземпляр. Имя команды изменено
# added 21.05.18
# 27.05.2018 changed: Формат команды. Многопоточность в трубу как и функция будильника
import datetime
from Handler import CommandHandler

alarms = dict()


# structure: day:hour:minute-message
def parse_date(s):
    date = 0
    now = datetime.datetime.now()
    try:
        day = '0'
        if ':' in s[2]:
            day = s[0:2]
            s = s[3:]
        else:
            day = s[0:1]
            s = s[2:]
        if str.isdecimal(day).__eq__(False):
            raise ValueError
        hour = '0'
        if ':' in s[1]:
            hour = s[0:1]
            s = s[2:]
        else:
            hour = s[0:2]
            s = s[3:]
        if str.isdecimal(hour).__eq__(False):
            raise ValueError
        minute = s
        if str.isdecimal(minute).__eq__(False) or hour.__len__() >= 3:
            raise ValueError
        date = datetime.datetime(now.year, now.month, int(day), int(hour), int(minute))
       # if now > date:
       #     raise ValueError
       # if now.year > date.year:
            # print('year problem')
       #     raise ValueError
       # if now.month > date.month and now.year == date.year:
            # print('month problem')
       #     raise ValueError
       # if now.day > date.day and now.month == date.month:
            # print('day problem')
        #    raise ValueError
    except ValueError:
        # print('some problem with date')
        date = 0
    finally:
        return date


# structure: day:hour:minute-message
def add_alarm(*args):
    message = 'Напоминание создано'
    id_user = args[1]
    s = args[0][11:]
    try:
        d = parse_date(s[:s.index('-')])
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


make_command = CommandHandler.Command()
make_command.keys = ['/makeAlarm']
make_command.description = '/makeAlarm: создам напоминалку'
make_command.process = add_alarm


def show_alarms(*args):
    alarm = alarms.get(args[1])
    message = ''
    if alarm is None:
        return 'Нет текущих напоминалок', ''
    else:
        for c in alarm:
            message += c[0].strftime("%d числа, в %H:%M") + ' -> ' + c[1] + '\n'
        return message, ''


show_command = CommandHandler.Command()
show_command.keys = ['/showAlarm']
show_command.description = '/showAlarm: покажу текущую напоминалку'
show_command.process = show_alarms


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


delete_command = CommandHandler.Command()
delete_command.keys = ['/deleteAlarm']
delete_command.description = '/deleteAlarm [N] - удалю напоминалку с номером N'
delete_command.process = delete_alarms
