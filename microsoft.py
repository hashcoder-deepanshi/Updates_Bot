# /html/body/div[2]/div[2]/div/div[2]/div[1]/section[1]/div/div/div[3]/div[3]/div[1]/span/button

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager

url = 'https://careers.microsoft.com/students/us/en/search-results'

# driver = webdriver.Chrome()


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds
driver.get(url)

driver.find_element(
    By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/section[1]/div/div/div[3]/div[3]/div[1]/span/button').click()
driver.find_element(
    By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/section[1]/div/div/div[3]/div[3]/div[2]/div/div[3]/ul/li[8]/label/span[1]').click()

time.sleep(5)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "information")))

driver.execute_script("window.scrollTo(0, 200)")
update = driver.find_element(By.CLASS_NAME, 'information')
heading = update.find_element(By.TAG_NAME, 'a')
# additionalInfo = update.find_elements(By.TAG_NAME, 'span')

print(heading.text)

# for info in additionalInfo:
#     print(info.text)
