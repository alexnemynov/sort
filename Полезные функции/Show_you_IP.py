import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://2ip.ru/'

options = webdriver.ChromeOptions()
options.add_argument('--headless')

with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    time.sleep(5)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)
