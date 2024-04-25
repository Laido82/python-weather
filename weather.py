from dotenv import load_dotenv
from pprint import pprint
import os
import requests
load_dotenv()


def get_current_weather(city="Kansas"):
    # request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print('\n*** Get Weather Conditions ***\n')
    city = input('\n Please enter a city name : ')

    if not bool(city.strip()):
        city = "Algiers"
        weather_data = get_current_weather(city)
        print('\n')
        pprint(weather_data)
    weather_data = get_current_weather(city)
    if weather_data['cod'] != 200:
        print('City not found')
