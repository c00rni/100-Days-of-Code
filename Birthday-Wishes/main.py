# TODO: Send a mail with python
# send a mail a specific date with datetime module
# send a motivation quote on mondays
# list birthdays in a csv file
# Automate a birthday wisher 
# Run the script on the cloud pythonanywhere.com


# smtp.gmail.com

import smtplib
import datetime as dt
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import random

load_dotenv("../.env")

GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")


subject = "[TEST] Antony python"
sender = GMAIL_ADDRESS
recipients = ["gmigan.a@gmail.com"]
password = GMAIL_PASSWORD


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


def dayChecker(year=None, month=None, day=None):
    today = dt.datetime.today()
    if today.year == year and today.month == month and today.day == day:
        with open("quotes.txt","r") as quote_file:
            body = f"Hello sir ! \n\n{random.choice(quote_file.readlines())}"
        send_email(subject, body, sender, recipients, password)
    
dayChecker(2024, 1, 3)
dayChecker(2024, 1, 2)
