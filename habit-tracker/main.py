from requests import get, post, put
from random import choice
from re import fullmatch

# function to Create user

# print the link to view my account
# open https://pixe.la/v1/users/a-know/graphs/test-graph.html

# function to create a new grapth
# put /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>


class HabitTracker:

    def __init__(self, username="") -> None:
        self._username = username

    def createUser(self, username, agree_terms="yes", not_minor="yes") -> None:
        if not fullmatch(pattern="[a-z][a-z0-9-]{1,32}", string=username):
            raise ValueError("The username must be in lower case and digist only")
        
        self._token = self._createToken()
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

    
    def _createToken(self) -> str:
        letter = list("abcdefghijklmnopqrstuvwsyz0123456789")
        digits = list()
        token = ""

        for _ in range(128):
            token += choice(digits+letter) 
        return token

    def getProfile(self) -> None:
        if self._username:
            print(f"Profile page: https://pixe.la/@{self._username}")


tracker = HabitTracker("corni")
tracker.getProfile()