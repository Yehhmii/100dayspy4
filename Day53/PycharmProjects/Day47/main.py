import requests
import lxml
import os
import smtplib
from pprint import pprint
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
USER_AGENT = os.environ.get("USER_AGENT")
ACCEPT_LANGUAGE = os.environ.get("ACCEPT_LANGUAGE")
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("E_PASSWORD")
receive_email = os.environ.get("OTHER_EMAIL")

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE,
}

response = requests.get(URL, headers=headers)
website_html = response.text
# pprint(website_html)

soup = BeautifulSoup(website_html, "lxml")
item_price = int(soup.find(name="span", class_="a-price-whole").getText().split(".")[0])
item_name = soup.find(name="span", id="productTitle").getText()
# print(item_price)
# print(item_name)

if item_price < 70:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn:
        conn.ehlo()
        conn.login(user=my_email, password=password)
        conn.sendmail(
            from_addr=my_email,
            to_addrs=receive_email,
            msg=f"Subject: Amazon Price Alert \n\n {item_name} \n is now ${item_price} \n Buy Now @ {URL}".encode("utf-8")
        )
