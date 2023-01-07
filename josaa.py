from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://josaa.nic.in/'

driver = webdriver.Chrome()
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds
driver.get(url)

updatesSection = driver.find_element(By.CLASS_NAME, 'gen-list')
title = updatesSection.find_element(By.TAG_NAME, 'a').text
link = updatesSection.find_element(By.TAG_NAME, 'a').get_attribute('href')

print(title)
print(link)

##### for database ####
# 1. title
# 2. link

