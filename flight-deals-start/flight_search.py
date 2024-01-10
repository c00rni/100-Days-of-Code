from datetime import datetime, timedelta
from flight_data import FlightData
from requests import get
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self, API_KEY:str, closest_date:int = 1 , farest_date:int = 30*6) -> None:
        self._api_key = API_KEY
        self._minimal_departure_date = (datetime.today() + timedelta(days=closest_date)).strftime("%d/%m/%Y")
        self._maximal_departure_date = (datetime.today() + timedelta(days=farest_date)).strftime("%d/%m/%Y")

    def search(self, flight_data:FlightData):
        headers = {
            "apikey": self._api_key,
            "accept": "application/json"
        }
        payload = {
            "fly_from": flight_data.departure_code,
            "data_from": self._minimal_departure_date,
            "fly_to": flight_data.destination_code,
            "date_to": self._maximal_departure_date,
            "price_to": flight_data.highiest_price_allowed,
            "curr": "CHF",
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "one_for_city": 0,
            "max_stopovers": 1
        }
        r = get("https://api.tequila.kiwi.com/v2/search",headers=headers, params=payload)
        if r.status_code != 200:
            print(r.json())
            return []
        data = r.json()["data"]
        valid_flights = []
            
        for flight in data:
            entry = {}
            entry['cityFrom'] = flight['cityFrom']
            entry['cityTo'] = flight['cityTo']
            entry['price'] = flight['price']
            entry['link'] = flight['deep_link']
            valid_flights.append(entry)
        return valid_flights
