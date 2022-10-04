import requests
import datetime
from pprint import pprint
from config import open_weather_token

code_to_smile = {
    "Clear": "Ясно \U00002600",
    "Clouds": "Облачно \U00002601",
    "Rain": "Дождь \U00002614",
    "Drizzle": "Небольшой дождь \U00002614",
    "Thunderstorm": "Гроза \U000026A1",
    "Snow": "Снег \U0001F328",
    "Mist": "Туман \U0001F32B"
}

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        #pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Ошибка о погоде!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])


        print(f"**{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}**\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}°C {wd}\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.столба\n"
              f"Скорость ветра: {wind}М/С\nВосход: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n"
              f"Продолжителность светового дня: {length_of_the_day}\n"
              f"Одевайтесь по погоде!"
              )

    except Exception as ex:
        print(ex)
        print("Проверьте название города")

def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()

