from prev import prev1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from apscheduler.schedulers.background import BackgroundScheduler
import pywhatkit
import datetime
now = datetime.datetime.now()

url = 'https://careers.google.com/jobs/results/'

driver = webdriver.Chrome()
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds
driver.get(url)

job = driver.find_element(
    By.XPATH, '//*[@id="46"]').send_keys("Software Engineering")

driver.find_element(
    By.XPATH, '//*[@id="46"]').send_keys(Keys.RETURN)

card = driver.find_element(By.CLASS_NAME, 'gc-card__title').text

header = driver.find_element(By.CLASS_NAME, 'gc-card__header')
location = header.find_elements(By.TAG_NAME, 'span')

address = ""
for addr in location:
    address += addr.text
    address += " "

para = driver.find_element(By.CLASS_NAME, 'gc-card__preview')

eligiblity = para.find_elements(By.TAG_NAME, 'li')

print(card, address)
desc = ""
for qual in eligiblity:
    desc += qual.text
    desc += '\n'

print(desc)

msg = card + '\n' + address + '\n' + desc

if card != prev1["google"]:
    pywhatkit.sendwhatmsg("+91 9667573950", msg, now.hour, now.minute + 2)
    prev1["google"] = card

driver.quit()
