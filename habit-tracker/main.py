from requests import get, post, put
from random import choice
from re import fullmatch
from dotenv import load_dotenv
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

    def createUser(self, username, agree_terms="yes", not_minor="yes") -> None:
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

    
    def _createToken(self, token_lenght) -> str:
        letter = list("abcdefghijklmnopqrstuvwsyz0123456789")
        digits = list()
        token = ""

        for _ in range(token_lenght):
            token += choice(digits+letter) 
        return token

    def getProfile(self) -> None:
        if self._username:
            print(f"Profile page: https://pixe.la/@{self._username}")
    
    def createGraph(self, name, unit, type="int", color="shibafu") -> None:
        if not self._token:
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


tracker = HabitTracker("corni", PIXELA_TOKEN)
tracker.createGraph("Lecture", "pages", "int")