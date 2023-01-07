from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pymongo 
from pymongo import MongoClient

client=pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
db=client["DiscordBot"]
collection=db["Website"]
id="9"


url = 'https://unstop.com/hackathons?filters=open&types=oppstatus'

driver = webdriver.Chrome()
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds
driver.get(url)

Challenge = driver.find_element(By.CLASS_NAME, 'cptn')
heading = Challenge.find_element(By.TAG_NAME, 'h2').text
org = Challenge.find_element(By.TAG_NAME, 'h3').text
link = driver.find_element(By.CLASS_NAME, 'listing').get_attribute('href')
post= {"id":id,"title":heading,"org":org,"link":link}
collection.insert_one(post)

print(heading)
print(org)
print(link)

##### for database ######
# 1. heading
# 2. org
# 3. link
