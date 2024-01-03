from requests import get
from dotenv import load_dotenv
from datetime import datetime
import os
import pytz

load_dotenv("../.env")

IPSTACK_API_KEY = os.environ.get("IPSTACK_API_KEY")
CLAUSE_DISTANCE = 5

#if os.path.isfile("user-position.txt"):
try:
    with open("user-position.txt") as user_position_file:
        user_lat = float(user_position_file.readline().rstrip())
        user_long = float(user_position_file.readline().rstrip())
except OSError:
    ip = get('https://api.ipify.org').content.decode('utf8')
    r = get(f"http://api.ipstack.com/{ip}?access_key={IPSTACK_API_KEY}")
    user_lat = float(r.json()['latitude'])
    user_long = float(r.json()['longitude'])
    with open("user-position.txt", "w") as user_position_file:
        user_position_file.write(f"{user_lat}\n{user_long}")


payload = {'lat': user_lat, 'lng': user_long, 'formatted':"0"}
r = get("https://api.sunrise-sunset.org/json", params=payload)
sunset_date_str = r.json()['results']["sunset"]
sunrise_date_str = r.json()['results']["sunrise"]

r = get("http://api.open-notify.org/iss-now.json")
iss_postisions = r.json()["iss_position"]
iss_lat = float(r.json()["iss_position"]["latitude"])
iss_long = float(r.json()["iss_position"]["longitude"])

sunset_time = datetime.fromisoformat(sunset_date_str).replace(tzinfo=pytz.UTC)
sunrise_time = datetime.fromisoformat(sunrise_date_str).replace(tzinfo=pytz.UTC)
currnet_date = datetime.now().replace(tzinfo=pytz.UTC)

is_night = (sunset_time < currnet_date or sunrise_time > currnet_date)

if user_lat > 0:
    lat_is_close = abs(iss_lat - user_lat) <= CLAUSE_DISTANCE
else:
    lat_is_close = abs(iss_lat + user_lat) <= CLAUSE_DISTANCE
if user_long > 0:
    long_is_close = abs(iss_long - user_long) <= CLAUSE_DISTANCE
else:
    long_is_close = abs(iss_long + user_long) <= CLAUSE_DISTANCE

is_close = lat_is_close and long_is_close

print(f"Night: {is_night}")
print(f"User: {user_lat}, {user_long}")
print(f"ISS: {iss_lat}, {iss_long}")

if is_close and is_night:
    pass