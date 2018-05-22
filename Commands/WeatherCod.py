import requests
import json
from Handler import CommandHandler

api_key = 'e0c8b55b1c3db7832226c7b6dfae20fc'

url = 'http://api.openweathermap.org/data/2.5/find?q={}&type=like&units=metric&lang=ru&APPID=e0c8b55b1c3db7832226c7b6dfae20fc'


def get_weather(*args):
    city = args[0][9:]
    try:
        #data = requests.get("http://api.openweathermap.org/data/2.5/find", params={'id': city, 'units': 'metric', 'lang': 'ru', 'APPID': api_key}).json()
        data = requests.get(url.format(city)).json()
        with open('answer.json', 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        if data['count'] == 0:
            return 'Нет совпадений по городу {}'.format(city), ''
        data_list = list(data['list'])
        temp = data_list[0]['main']['temp']
        pressure = data_list[0]['main']['pressure']
        humidity = data_list[0]['main']['humidity']
        # country = data['list'][0]['sys']['country']
        weather = data_list[0]['weather'][0]['description']
        return 'Температура:{}\nДавление:{}\nВлажность:{}\n{}'.format(str(temp), str(pressure), str(humidity), weather), ''
    except Exception as e:
        return "Exception (find):{}".format(str(e)), ''
        pass


weather_command = CommandHandler.Command()
weather_command.keys = ['/weather']
weather_command.description = 'Покажу погоду указанного города. (/weather минск)'
weather_command.process = get_weather
