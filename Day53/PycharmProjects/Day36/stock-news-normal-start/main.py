import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHA_STOCK_API_KEY = ""
NEWS_API_KEY = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_STOCK_API_KEY,
}

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

stock = [value for (key, value) in data.items()]
yesterday = stock[0]
yesterday_closing_stock = yesterday["4. close"]

day_before_yesterday = stock[1]
day_before_yesterday_closing = day_before_yesterday["4. close"]

difference = float(yesterday_closing_stock) - float(day_before_yesterday_closing)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_stock)) * 100)
# print(diff_percent)

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if abs(diff_percent) > 5:
    param = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "sortBy": "popularity"
    }
    res = requests.get(url=NEWS_ENDPOINT, params=param)
    res.raise_for_status()
    articles = res.json()["articles"]
    top_three = articles[:3]
    # print(top_three)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

    top_three_headlines = [f"{STOCK_NAME}: {up_down}{diff_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in top_three]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in top_three_headlines:
        message = client.messages.create(
            body=article,
            from_="+12015813103",
            to='+2348158619466'
        )
        print(message.status)
