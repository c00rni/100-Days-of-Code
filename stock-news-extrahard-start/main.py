import os
from dotenv import load_dotenv
from requests import get
from datetime import datetime, timedelta
from pytz import timezone

load_dotenv("../.env")

ALPHA_VENTURE_API_KEY = os.environ.get("ALPHA_VENTURE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

STOCK_SYMBOL = "TSLA"
COMPANY_NAME = "Tesla"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com / Pywhatkit library
# Send a seperate message with the percentage change and each article's title and description to through whatapp. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


# Search for symbol
# https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=TSLA&apikey=demo

payload = {f"function": "TIME_SERIES_DAILY", "symbol": {STOCK_SYMBOL}, "outputsize": "compact", "apikey": {ALPHA_VENTURE_API_KEY}}
alpha_vantage_request = get("https://www.alphavantage.co/query", params=payload)

date_1 = (datetime.today() - timedelta(days=1))
date_2 = (date_1 - timedelta(days=1)).strftime("%Y-%m-%d")
date_1 = date_1.strftime("%Y-%m-%d")
try:
    date1_market_data = alpha_vantage_request.json()['Time Series (Daily)'][date_1]
    date2_market_data = alpha_vantage_request.json()['Time Series (Daily)'][date_2]

    change_pourcentage = (abs(float(date2_market_data['4. close']) - float(date1_market_data['4. close'])) / float(date2_market_data['4. close'])) * 100


    if change_pourcentage > 5:
        payload = {"q": COMPANY_NAME, "pageSize": 3, "page": 0, "apiKey": NEWS_API_KEY}
        r = get("https://newsapi.org/v2/top-headlines", params=payload)
        articles = r.json()['articles']
        for article in articles:
            print(article['title'])
except Exception:
    print(alpha_vantage_request.json().get('Information'))