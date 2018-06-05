# import requests
# from Handler import CommandHandler

# url_name = 'http://www.nbrb.by/API/ExRates/Rates/{}?ParamMode=2'
# # описание возвращаемого объекта json:{
# # "Cur_ID":145,
# интегрирован в курс
# # "Date":"2018-05-22T00:00:00",
# # "Cur_Abbreviation":"USD",
# # "Cur_Scale":1,
# # "Cur_Name":"Доллар США",
# # "Cur_OfficialRate":2.0022}


# def get_course_with_name(name):
#     try:
#         usd_course = requests.get(url_name.format(name.upper())).json()
#         return str(usd_course['Cur_Scale']) + ' ' + usd_course['Cur_Name'] + ' - ' + str(usd_course['Cur_OfficialRate']) + ' белорусских рубля'
#     except:
#         return 'По данному запросу возникла ошибка. Проверьте правильность написания короткого имени'


# def course_pro(name):
#     message = ''
#     message += get_course_with_name(name)
#     return message, ''


# info_command = CommandHandler.Command()
# info_command.keys = ['/:']
# info_command.description = 'Покажу курс указанной валюты. Формат команды /:[имя_валюты](usd, EUR и т.д.)'
# info_command.process = course_pro


# def func(*args):
#     if '/stre' in args[0]:
#         print(True)
#     else:
#         print('false')


# st = "/:usd"
# print(st[2:])
# func(st)
# func('headf/:')
# func('/:usd')
