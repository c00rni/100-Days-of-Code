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
BIRTHDAY_MAIL_SUBJECT = os.environ.get("BIRTHDAY_MAIL_SUBJECT")


subject = BIRTHDAY_MAIL_SUBJECT
sender = GMAIL_ADDRESS
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
        with open(f"letters/{random.choice(os.listdir('letters'))}") as base_letter_file:
            base_letter = base_letter_file.read()
            personalies_letter = base_letter.replace("[name]", row['name'])
            personalies_letter = personalies_letter.replace("[relationship]", row['relationship'])
            personalies_letter = personalies_letter.replace("[nickname]", row['nickname'])
            send_email(subject, personalies_letter, sender, row['email'], password)
    
dayChecker()
