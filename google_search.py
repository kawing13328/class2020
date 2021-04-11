from time import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# steps
browser = webdriver.Chrome()

# or specify the path: driver = webdriver.Chrome('/path/to/chromedriver')
sleep(5)

browser.get("https://google.com")

search_text_box = browser.find_element_by_name("q")
search_text_box.clear()
search_text_box.send_keys("python selenium integration")  # typing in the search box
search_text_box.send_keys(Keys.RETURN)  # hitting the enter key
sleep(5)

search_text_box2 = browser.find_element_by_name("q")
search_text_box2.clear()  # delete everything in the search box
sleep(10)
browser.close()
print("completed!!!!!!!!!!!!!!!")
