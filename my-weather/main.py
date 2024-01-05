# TODO: GET latitude and longitude
# TODO: Request forecast API
# TODO: print status code
# TODO: print the response to the console
# TODO: print the weather id and secription

import os
from dotenv import load_dotenv

load_dotenv("../.env")

HOME_LONGITUDE = os.environ.get("HOME_LONGITUDE")
HOME_LATITUDE = os.environ.get("HOME_LATITUDE")

print(HOME_LATITUDE)
print(HOME_LONGITUDE)