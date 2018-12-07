from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("http://google.com")
element = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
element.send_keys("Котики")
sleep(3)
element.send_keys(Keys.ENTER)
# assert driver.title == 'Риалвеб - Поиск в Google'
