# TODO: GET latitude and longitude
# TODO: Request forecast API
# TODO: print status code
# TODO: print the response to the console
# TODO: print the weather description

import os
from dotenv import load_dotenv
from requests import get

load_dotenv("../.env")

OPEN_WEATHER_API_KEY = os.environ.get("OPEN_WEATHER_API")

payload = {'q': "nyon", 'appid': OPEN_WEATHER_API_KEY}
r = get("https://api.openweathermap.org/data/2.5/weather", params=payload)
if r.status_code == 200:
    description = r.json()["weather"][0]["description"]
    cloudiness_pourcentage = r.json()["clouds"]["all"]
    print(f"Decription: {description}, Cloud: {cloudiness_pourcentage}%.")
else:
    print("Request to openweathermap API failed.")