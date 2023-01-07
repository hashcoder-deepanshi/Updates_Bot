from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pymongo 
from pymongo import MongoClient

client=pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
db=client["DiscordBot"]
collection=db["Website"]
id="2"



url = 'https://jacdelhi.admissions.nic.in/'

driver = webdriver.Chrome()
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds
driver.get(url)

updatesSection = driver.find_element(By.CLASS_NAME, 'gen-list')
title = updatesSection.find_element(By.TAG_NAME, 'a').text
link = updatesSection.find_element(By.TAG_NAME, 'a').get_attribute('href')
post= {"id":id,"link":link,"title":title}
collection.insert_one(post)
print(title)
print(link)

##### for database ####
# 1. title
# 2. link

