import requests
import re
from Handler import command_handler

classic = [145, 292, 298, 293, 143]
# usd = 145
# rus = 298
# eur = 292
# zlot = 293
# funt_en = 143

url_num = 'http://www.nbrb.by/API/ExRates/Rates/'
url_name = 'http://www.nbrb.by/API/ExRates/Rates/{}?ParamMode=2'

# описание возвращаемого объекта json:{
#  'Cur_ID': 145,                   внутренний код валюты
#  'Date': '2018-05-22T00:00:00',   дата, на которую запрашивается курс
#  'Cur_Abbreviation': 'USD',       буквенный код
#  'Cur_Scale': 1,                  колличество единиц запрашиваемой валюты
#  'Cur_Name': 'Доллар США',        наименование валюты на русском языке(множественное/единственное число)
#  'Cur_OfficialRate': 2.0022}      курс


class Course:
    def __init__(self):
        info_command = command_handler.Command()
        info_command.keys = ['/course']
        info_command.description = 'Покажу курс валют'
        info_command.process = Course.course_classic

        info_command = command_handler.Command()
        info_command.keys = ['/:']
        info_command.description = 'Покажу курс указанной валюты. Формат команды /:[имя_валюты](usd, EUR и т.д.)'
        info_command.process = Course.course_pro

    @staticmethod
    def get_course_with_num(num):
        try:
            usd_course = requests.get(url_num + str(num)).json()
            return str(usd_course['Cur_Scale']) + ' ' + usd_course['Cur_Name'] + ' - ' + str(usd_course['Cur_OfficialRate']) + ' белорусских рубля'
        except:
            return 'По данному запросу возникла ошибка. Не подвезли курс?'

    @staticmethod
    def course_classic(*args):
        message = ''
        for c in classic:
            message += Course.get_course_with_num(c)
        return message, ''

    @staticmethod
    def get_course_with_name(name):
        try:
            usd_course = requests.get(url_name.format(name.upper())).json()
            return str(usd_course['Cur_Scale']) + ' ' + usd_course['Cur_Name'] + ' - ' + str(
                usd_course['Cur_OfficialRate']) + ' белорусских рубля\n'
        except:
            return 'По данному запросу возникла ошибка. Проверьте правильность написания короткого имени\n'

    @staticmethod
    def course_pro(*args):
        message = ''
        pattern = re.compile('/:\w+')
        ind = 0
        for c in pattern.findall(args[0]):
            ind += 1
            if c.__len__() != 5:
                message += 'Неверный формат имени с индексом {}. Короткие имена валют состоят из трех символов\n'.format(str(ind))
            else:
                message += Course.get_course_with_name(c[2:])
        return message, ''


Course()
