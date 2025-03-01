from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# creating the driver
driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
driver.get('https://secure-retreat-92358.herokuapp.com/')

# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# article_count.click()
# print(article_count.text)

# filling the app form
fname = driver.find_element(By.NAME, value='fName')
lname = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')

fname.send_keys("Kiko")
lname.send_keys("Last")
email.send_keys('kikolast@gmail.com', Keys.ENTER)

#  hitting the enter btn
# btn = driver.find_element(By.CLASS_NAME, 'btn-block')
# btn.click()

# driver.quit()
