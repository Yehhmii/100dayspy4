import smtplib
import datetime as dt
import random

my_email = ""
password = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt", "r") as data:
        quotes = data.readlines()
        quote = random.choice(quotes)
    print(quote)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn:
        conn.ehlo()
        conn.login(user=my_email, password=password)
        conn.sendmail(from_addr=my_email, to_addrs="",
                      msg=f"Subject: Quote of the Day \n\n {quote}")
