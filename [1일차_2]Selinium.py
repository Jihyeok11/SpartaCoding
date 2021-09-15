from selenium import webdriver
driver = webdriver.Chrome('chromedriver')
import time

driver.get("http://www.naver.com")
time.sleep(5)

