import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWSAPI_API_KEY = os.getenv('NEWSAPI_API_KEY')
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
params = {
    "function": "TIME_SERIES_DAILY",
    "datatype": "json",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY
}
response = requests.get(url=STOCK_ENDPOINT, params=params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday = data_list[0]
yesterday_closing_price = float(yesterday["4. close"])

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday["4. close"])

difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
difference_percent = (difference / yesterday_closing_price) * 100

print(difference_percent)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if difference_percent > 3:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWSAPI_API_KEY,
    }
    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_articles = response.json()['articles']



    print(news_articles[:3])
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


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
