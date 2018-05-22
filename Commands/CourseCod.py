import requests
from Handler import CommandHandler

classic = [145, 292, 298, 293, 143]
usd = 145
rus = 298
eur = 292
zlot = 293
funt_en = 143

url_num = 'http://www.nbrb.by/API/ExRates/Rates/'
# описание возвращаемого объекта json:{
#  'Cur_ID': 145,                   внутренний код валюты
#  'Date': '2018-05-22T00:00:00',   дата, на которую запрашивается курс
#  'Cur_Abbreviation': 'USD',       буквенный код
#  'Cur_Scale': 1,                  колличество единиц запрашиваемой валюты
#  'Cur_Name': 'Доллар США',        наименование валюты на русском языке(множественное/единственное число)
#  'Cur_OfficialRate': 2.0022}      курс


def get_course_with_num(num):
    try:
        usd_course = requests.get(url_num + str(num)).json()
        return str(usd_course['Cur_Scale']) + ' ' + usd_course['Cur_Name'] + ' - ' + str(usd_course['Cur_OfficialRate']) + ' белорусских рубля'
    except:
        return 'По данному запросу возникла ошибка. Не подвезли курс?'


def course_classic(*args):
    message = ''
    for c in classic:
        message += get_course_with_num(c)
    return message, ''


info_command = CommandHandler.Command()
info_command.keys = ['/course']
info_command.description = 'Покажу курс валют'
info_command.process = course_classic


course_classic()