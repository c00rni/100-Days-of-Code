from requests import post
import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("../.env")

NUTRITION_API_ID = os.environ.get("NUTRITION_API_ID")
NUTRITION_API_KEY = os.environ.get("NUTRITION_API_KEY")
WORKOUT_PROJECT_CREDS = os.environ.get("WORKOUT_PROJECT_CREDS")

SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PROJECT_NAME = os.environ.get("SHEETY_PROJECT_NAME")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

domain = "https://trackapi.nutritionix.com"
exercice_endpoint = "/v2/natural/exercise"
headers = {
    'x-app-id': NUTRITION_API_ID,
    'x-app-key': NUTRITION_API_KEY
}
data = {
    "query": input("Tell me wish execice you did? ")
}

r = post(f"{domain}{exercice_endpoint}", headers=headers, json=data)
exercice_datas = r.json()['exercises']

date = datetime.now()
for exercice in exercice_datas:

    new_row_data = {
        SHEET_ENDPOINT: {       
        "date": date.strftime("%d/%m/%Y"),
        "time": date.strftime("%H:%M:%S"),
        "exercise": exercice['user_input'],
        "duration": float(exercice['duration_min']),
        "calories": float(exercice['nf_calories'])
        }
    }

    headers = {
        "Authorization": f"Basic {WORKOUT_PROJECT_CREDS}"
    }
    r = post(f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEET_ENDPOINT}", headers=headers, json=new_row_data)
    error = r.json().get("error")
    if error:
        print(error)
    else:
        print(r.json())