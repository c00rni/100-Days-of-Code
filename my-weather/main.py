# TODO: Detect when it will rain or snow in the day
# TODO: Send a notification SMS of the weather on rainy on snowy days
# https://openweathermap.org/weather-conditions
# https://pro.openweathermap.org/data/2.5/forecast/hourly?q={city name}&appid={API key}

import os
from dotenv import load_dotenv
from requests import get

load_dotenv("../.env")

OPEN_WEATHER_API_KEY = os.environ.get("OPEN_WEATHER_API")

payload = {'q': "briançon", 'appid': OPEN_WEATHER_API_KEY, "cnt": 4}
r = get("https://api.openweathermap.org/data/2.5/forecast", params=payload)
rain = False
snow = False
if r.status_code == 200:
    weather_states = [weather_forcast["weather"][0]["id"] for weather_forcast in r.json()['list']]
    for states in weather_states:
        if not rain and (states > 500 and states < 532 or states > 615 and states < 623):
            rain = True
        if not snow and (states > 600 and states < 623):
            snow = True
    if snow and not rain:
        print("It's snowing today ❄️⛄, take some gloves.")
    elif rain and snow or rain and not snow:
        print("It's going to rain today. Remenber to bring an ☔")

else:
    print("Request to openweathermap API failed.")