from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.amazon.jobs/en/job_categories/software-development'

# driver = webdriver.Chrome()


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds
driver.get(url)

driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(5)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "job")))

jobSection = driver.find_element(By.CLASS_NAME, 'job')
title = jobSection.find_element(By.TAG_NAME, 'h3').text
location = jobSection.find_element(By.TAG_NAME, 'p').text
desc = jobSection.find_element(By.CLASS_NAME, 'description').text

# message that bot will send
print(title)
print(location)
print(desc)
print(url)
