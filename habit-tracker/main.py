from requests import get, post, put
from random import choice
from re import fullmatch
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv("../.env")

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")

# function to Create user

# print the link to view my account
# open https://pixe.la/v1/users/a-know/graphs/test-graph.html

# function to create a new grapth
# put /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>


class HabitTracker:

    def __init__(self, username="", token="") -> None:
        self._username = username
        self._token = token

    def createUser(self, username:str, agree_terms:str="yes", not_minor:str="yes") -> None:
        if not fullmatch(pattern="[a-z][a-z0-9-]{1,32}", string=username):
            raise ValueError("The username must be in lower case and digist only")
        
        self._token = self._createToken(128)
        payload = {
            "token": self._token,
            "username":username,
            "agreeTermsOfService":agree_terms,
            "notMinor":not_minor
        }
        request = post("https://pixe.la/v1/users", json=payload)
        if request.status_code != 200:
            raise ValueError(request.json()['message'])
        print(f"Created the new username: {username}\nYour unique token is: {self._token}")
        print(request.json()['message'])

    
    def _createToken(self, token_lenght:int) -> str:
        letter = list("abcdefghijklmnopqrstuvwsyz0123456789")
        digits = list()
        token = ""

        for _ in range(token_lenght):
            token += choice(digits+letter) 
        return token

    def getProfile(self) -> None:
        if self._username:
            print(f"Profile page: https://pixe.la/@{self._username}")
    
    def createGraph(self, name:str, unit:str, type:str="int", color:str="shibafu") -> None:
        if not self._token or not self._username:
            raise ValueError("The token must be provide.")
        type = type.lower()
        if type not in ["int", "float"]:
            raise ValueError('Type must be "int" or "Float"')
        supported_color = ["shibafu", "momiji", "sora", "ichou", "ajisai", "kuro"]
        if color not in supported_color:
            raise ValueError('Invalid color name.')
        
        id = self._createToken(16)
        payload = {
            "id":id,
            "name":name,
            "unit":unit,
            "type":type,
            "color":color
        }
        headers = {"X-USER-TOKEN": self._token}
        request = post(f"https://pixe.la/v1/users/{self._username}/graphs", headers=headers, json=payload)
        print(f"{request.json()['message']} Graph id: {id}")

    def recordPixel(self, grapheh_id:str, date:datetime, quantity:int) -> None:
        if not self._token or not self._username:
            raise ValueError("The token must be provide.")
        payload = {
            "date":date.strftime("%Y%m%d"),
            "quantity":str(quantity)
        }
        headers = {"X-USER-TOKEN": self._token}
        request = post(f"https://pixe.la/v1/users/{self._username}/graphs/{grapheh_id}", headers=headers, json=payload)
        if request.status_code != 200:
            raise ValueError(request.json()['message'])
        print(f"{request.json()['message']} Pixel recorded.")


tracker = HabitTracker("corni", PIXELA_TOKEN)
date = datetime.today()
tracker.recordPixel("ugksbf1vhnisiitz", date,3)