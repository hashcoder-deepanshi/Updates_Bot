from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://www.metacareers.com/jobs'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds
driver.get(url)

driver.find_element(
    By.XPATH, '//*[@id="search_result"]/div/div[1]/div[2]/div[2]/div[2]/div[1]').click()
time.sleep(5)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "_8sel")))

driver.execute_script("window.scrollTo(0, 200)")
title = driver.find_element(By.CLASS_NAME, '_8sel')
location = driver.find_element(By.CLASS_NAME, '_8see').text

print(title.text)
print(location)


####### database #####
# 1. title
# 2. location

