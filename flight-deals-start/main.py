#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# 1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).
# 2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
# 3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.
# 4. The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. e.g.

# Tequila search API documentation : https://tequila.kiwi.com/portal/docs/user_guides/search_api__general_information_

# Extract all the city name from the sheet (sheety API)
from requests import get
import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

load_dotenv("../.env")

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")

spreadSheet_manager = DataManager(sheety_username=SHEETY_USERNAME, sheety_project_name="flightDeals", sheety_endpoint="cities")
flight_searcher = FlightSearch(API_KEY=TEQUILA_API_KEY)
mailer = NotificationManager(GMAIL_ADDRESS, GMAIL_PASSWORD)
sheet_data = spreadSheet_manager.getFlights()
result = False

mail_body = ""
mail_subject = "[Cheap Flight Bot] - Cheap flight opportunities"
mail_receipients = ["gmigan.a@gmail.com","cpouvani@gmail.com"]

for row in sheet_data:
    flight = FlightData(departure_city_name="Geneva",
                        departure_iata_code="GVA",
                        destination_city_name=row['city'],
                        destination_iata_code=row['iataCode'],
                        accepted_price=row['lowestPrice'])
    
    valide_flights = flight_searcher.search(flight)
    if valide_flights:
        result = True
        for flight_info in valide_flights:
            flight_info['price']
            flight_info['link']
            mail_body += f"{flight_info['cityFrom']} -> {flight_info['cityTo']} AT {flight_info['price']} CHF\n"
            mail_body += f"{flight_info['link']}\n\n "

mailer.send_email(body=mail_body,subject=mail_subject, recipients=mail_receipients)