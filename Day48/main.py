from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome browser open even after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#  setting up the driver
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.jumia.com.ng/itel-a06-6.6-hd-32gb-rom-up-to-4gb-ram-4000mah-4g-365072751.html")

# price = driver.find_element(By.CSS_SELECTOR, value='.brcbs a')
# price = driver.find_element(By.XPATH, value='//*[@id="jm"]/main/div[1]/section/div/div[2]/div[2]/div[2]/div[2]/span')
# print(price.text)


#  let us create a dictionary that houses upcoming events in  python.org
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')

menu_time = driver.find_elements(By.CSS_SELECTOR, value='.event-widget ul time')
menu = driver.find_elements(By.CSS_SELECTOR, value='.event-widget ul a')
new_menu_time = [time.text for time in menu_time]
new_menu = [item.text for item in menu]
# print(new_menu_time)
# print(new_menu)

new_record = {}
for n in range(len(menu_time)):
    new_record[n] = {
        "time": new_menu_time[n],
        "Event": new_menu[n]
    }
print(new_record)

# driver.close()
driver.quit()

