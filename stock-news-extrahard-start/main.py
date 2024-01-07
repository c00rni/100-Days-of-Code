import os
from dotenv import load_dotenv
from requests import get
from datetime import datetime, timedelta
from pytz import timezone
from notifier import SMSNotifier

load_dotenv("../.env")

ALPHA_VENTURE_API_KEY = os.environ.get("ALPHA_VENTURE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
PERSONAL_NUMBER = os.environ.get("PERSONAL_NUMBER")

STOCK_SYMBOL = "TSLA"
COMPANY_NAME = "Tesla"


payload = {f"function": "TIME_SERIES_DAILY", "symbol": {STOCK_SYMBOL}, "outputsize": "compact", "apikey": {ALPHA_VENTURE_API_KEY}}
alpha_vantage_request = get("https://www.alphavantage.co/query", params=payload)

date_1 = (datetime.today() - timedelta(days=1))
date_2 = (date_1 - timedelta(days=1)).strftime("%Y-%m-%d")
date_1 = date_1.strftime("%Y-%m-%d")
try:
    date1_market_data = alpha_vantage_request.json()['Time Series (Daily)'][date_1]
    date2_market_data = alpha_vantage_request.json()['Time Series (Daily)'][date_2]

    value_difference = float(date2_market_data['4. close']) - float(date1_market_data['4. close'])
    change_pourcentage = (value_difference / float(date2_market_data['4. close'])) * 100


    if change_pourcentage > 5:
        payload = {"q": COMPANY_NAME, "pageSize": 3, "page": 0, "apiKey": NEWS_API_KEY}
        r = get("https://newsapi.org/v2/top-headlines", params=payload)
        articles = r.json()['articles']
        sign = "🔺" if value_difference > 0 else "🔻"
        message = f"\n\n{sign} change_pourcentage %\n"
        sms_notifier = SMSNotifier(sender_number=TWILIO_NUMBER, receiver_number=PERSONAL_NUMBER, username=TWILIO_ACCOUNT_SID, password=TWILIO_AUTH_TOKEN)
        
        for article in articles:
            message += f"Headline: {article['title']}\nBrief: {article['description']}\n"
        sms_notifier.sendMessage(message)
except Exception:
    print(alpha_vantage_request.json().get('Information'))
