from requests import post
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv("../.env")

NUTRITION_API_ID = os.environ.get("NUTRITION_API_ID")
NUTRITION_API_KEY = os.environ.get("NUTRITION_API_KEY")

# TODO: 1. Using the Nutritionix "Natural Language for Exercise" API Documentation, figure out how to print the exercise stats for plain text input.

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
print(r.json())
