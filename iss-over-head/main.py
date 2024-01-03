from requests import get
from dotenv import load_dotenv
from datetime import datetime
import os
import pytz
from time import sleep

load_dotenv("../.env")

IPSTACK_API_KEY = os.environ.get("IPSTACK_API_KEY")
CLAUSE_DISTANCE = 5

class ISSTracker:

    def __init__(self) -> None:
        self._setNightTime()

    def _setUserPosition(self):
        try:
            with open("user-position.txt") as user_position_file:
                self._user_lat = float(user_position_file.readline().rstrip())
                self._user_long = float(user_position_file.readline().rstrip())
        except OSError:
            ip = get('https://api.ipify.org').content.decode('utf8')
            r = get(f"http://api.ipstack.com/{ip}?access_key={IPSTACK_API_KEY}")
            self._user_lat = float(r.json()['latitude'])
            self._user_long = float(r.json()['longitude'])
            with open("user-position.txt", "w") as user_position_file:
                user_position_file.write(f"{self._user_lat}\n{self._user_long}")

    def _setNightTime(self):
        self._setUserPosition()
        payload = {'lat': self._user_lat, 'lng': self._user_long, 'formatted':"0"}
        r = get("https://api.sunrise-sunset.org/json", params=payload)
        sunset_date_str = r.json()['results']["sunset"]
        sunrise_date_str = r.json()['results']["sunrise"]

        self._sunset_time = datetime.fromisoformat(sunset_date_str).replace(tzinfo=pytz.UTC)
        self._sunrise_time = datetime.fromisoformat(sunrise_date_str).replace(tzinfo=pytz.UTC)
        self._currnet_date = datetime.now().replace(tzinfo=pytz.UTC)

    def _setISSPosition(self):
        r = get("http://api.open-notify.org/iss-now.json")
        self._iss_lat = float(r.json()["iss_position"]["latitude"])
        self._iss_long = float(r.json()["iss_position"]["longitude"])

    def _isNight(self):
        return (self._sunset_time < self._currnet_date or self._sunrise_time > self._currnet_date)

    def _issIsClause(self):
        self._setISSPosition()
        if self._user_lat > 0:
            lat_is_close = abs(self._iss_lat - self._user_lat) <= CLAUSE_DISTANCE
        else:
            lat_is_close = abs(self._iss_lat + self._user_lat) <= CLAUSE_DISTANCE
        if self._user_long > 0:
            long_is_close = abs(self._iss_long - self._user_long) <= CLAUSE_DISTANCE
        else:
            long_is_close = abs(self._iss_long + self._user_long) <= CLAUSE_DISTANCE
        return lat_is_close and long_is_close
    
    def isISSVisible(self):
        if self._isNight() and self._issIsClause():
            self._notify()

    def _notify(self):
        print("Iss visible !!")

    

tracker = ISSTracker()
while True:
    tracker.isISSVisible()
    sleep(1000*60*5)