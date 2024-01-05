# TODO: Detect when it will rain or snow in the day
# TODO: Send a notification SMS of the weather on rainy on snowy days
# https://openweathermap.org/weather-conditions
# https://pro.openweathermap.org/data/2.5/forecast/hourly?q={city name}&appid={API key}

import os
from dotenv import load_dotenv
from requests import get
from notifier import SMSNotifier

load_dotenv("../.env")

OPEN_WEATHER_API_KEY = os.environ.get("OPEN_WEATHER_API")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
PERSONAL_NUMBER = os.environ.get("PERSONAL_NUMBER")
CITY_NAME = "CHAMGE THIS"

payload = {'q': CITY_NAME, 'appid': OPEN_WEATHER_API_KEY, "cnt": 4}
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
    sms_notifier = SMSNotifier(sender_number=TWILIO_NUMBER, receiver_number=PERSONAL_NUMBER, username=TWILIO_ACCOUNT_SID, password=TWILIO_AUTH_TOKEN)
    if snow and not rain:
        sms_notifier.sendMessage("It's snowing today ❄️⛄, take some gloves.")

    elif rain and snow or rain and not snow:
        sms_notifier.sendMessage("It's going to rain today. Remenber to bring an ☔")

else:
    print("Request to openweathermap API failed.")