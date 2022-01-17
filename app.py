from http import server
from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://youtube.com")
print(driver.title)

search = driver.find_element_by_name("search_query")
search.send_keys("NEW ORLEANS SAINTS")
search.send_keys(Keys.RETURN)


time.sleep(5)
driver.quit()