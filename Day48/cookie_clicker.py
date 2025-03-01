from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

clicker = driver.find_element(By.CSS_SELECTOR, '#middle #cookie')

# getting all store items
store = driver.find_elements(By.CSS_SELECTOR, '#store div')
store_ids = [item.get_attribute("id") for item in store]
# print(store_ids)

# available amount of cookie money
money = driver.find_element(By.ID, 'money').text
if "," in money:
    money = money.replace(",", "")
cookie_amount = int(money)

# getting items prices as a list
item_price = driver.find_elements(By.CSS_SELECTOR, '#store b')
price_list = [[price.text for price in item_price]]
new_price_list = []
for n in range(0, 8):
    price = [price[n].split('-')[1] for price in price_list]
    single_price = int(price.pop().replace(",", ""))
    new_price_list.append(single_price)

# print(new_price_list)
# print(money)

# setting a timer 
timer = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

while True:
    clicker.click()

    # code to run every 5sec
    if time.time() > timer:

        # create dictionary to house our store item and prices
        cookie_upgrade = {}
        for n in range(len(new_price_list)):
            cookie_upgrade[new_price_list[n]] = store_ids[n]
            print(cookie_upgrade)

        # find upgrades that can be bought
        affordable_upgrade = {}
        for cost, ide in cookie_upgrade.items():
            print(cost, ide)
            if cookie_amount > cost:
                print(cookie_amount)
                affordable_upgrade[cost] = ide

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrade)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrade[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break


