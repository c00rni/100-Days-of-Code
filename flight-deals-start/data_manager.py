from requests import get

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self, sheety_username:str, sheety_project_name:str, sheety_endpoint:str) -> None:
        self._username = sheety_username
        self._project_name = sheety_project_name
        self._endpoint = sheety_endpoint

    def getFlights(self):
        r = get(f"https://api.sheety.co/{self._username}/{self._project_name}/{self._endpoint}")
        return r.json()['cities']
