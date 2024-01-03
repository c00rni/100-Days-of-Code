from issTracker import ISSTracker
from time import sleep
import os
from dotenv import load_dotenv
from mailManager import MailManager


load_dotenv("../.env")

IPSTACK_API_KEY = os.environ.get("IPSTACK_API_KEY")
CLAUSE_DISTANCE = 5
GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")
TEXT = '''Hello,

The International Space Station is visible from your locolization.

Regards,
ISS over head script
'''

mail_manager = MailManager(GMAIL_ADDRESS, GMAIL_PASSWORD)
tracker = ISSTracker(IPSTACK_API_KEY, CLAUSE_DISTANCE)
while True:
    if tracker.isISSVisible():
        mail_manager.send_email("[ISS-Over-Head] ISS is visible",TEXT,[GMAIL_ADDRESS])
        sleep(1000*60*30)
    else:
        sleep(1000*60*5)