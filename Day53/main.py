from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import lxml
import requests

google_form = ("https://docs.google.com/forms/d/e/1FAIpQLSfrYxx_RNb16AgYWXD_8HL-uNIc2nvtnX6FmdwsCgg18e9tXw/viewform?usp=header")
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

# creating a connection using requests to the site url
data = requests.get(ZILLOW_URL).text

# making a soup object
soup = BeautifulSoup(data, "lxml")

# getting the prices of all apartment
prices = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')
price_list = [price.get_text().split('/')[0].split('+')[0] for price in prices]

#  getting the address of all apartment
apartments = soup.select(".StyledPropertyCardDataWrapper a address")
apartment_list = [ item.get_text().replace('\n', "").lstrip().rstrip() for item in apartments]

#  getting the links of every apartment
links = soup.select(".StyledPropertyCardDataWrapper a")
link_list = [item["href"] for item in links]

print(apartment_list)
print(price_list)
print(link_list)


# let's create and set selenium driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


for n in range(len(apartment_list)):
    driver.get(google_form)
    time.sleep(5)

    the_address = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    the_price = driver.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input[@type="text"]')
    the_link = driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input[@type="text"]')
    send = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    the_address.send_keys(apartment_list[n])

    the_price.send_keys(price_list[n])

    the_link.send_keys(link_list[n])

    send.click()

