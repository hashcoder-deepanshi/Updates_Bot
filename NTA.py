from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pymongo 
from pymongo import MongoClient

client=pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
db=client["DiscordBot"]
collection=db["Website"]
id="6"



url = 'https://nta.ac.in/'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds
driver.get(url)

driver.execute_script("window.scrollTo(0, 400)")
time.sleep(5)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="maincont"]/div/div/div[3]/div[1]/div[2]/div[2]/marquee')))

updateSection = driver.find_element(
    By.XPATH, '//*[@id="maincont"]/div/div/div[3]/div[1]/div[2]/div[2]/marquee')

title = updateSection.find_element(By.TAG_NAME, 'content').text
docs = updateSection.find_element(By.TAG_NAME, 'a').get_attribute('href')
post= {"id":id,"title":title}
collection.insert_one(post)
print(title)
print(docs)

####### for database #######
# 1. title
# 2. docs
