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
import pandas as pd

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


def dayChecker():
    today = dt.datetime.today()
    birthdays_dataframe = pd.read_csv("birthdays.csv")
    birthdays_selection = birthdays_dataframe[(birthdays_dataframe.month == today.month) & (birthdays_dataframe.day == today.day)].to_dict('records')
    for row in birthdays_selection:
        print(row)
        #send_email(subject, body, sender, recipients, password)
    
dayChecker()
