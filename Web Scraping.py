from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
import time

chorome_driver = webdriver.Chrome("chromedriver.exe")
chorome_driver.get("https://www.facebook.com/")

time.sleep(2)

correo = chorome_driver.find_element_by_name("email")
correo.send_keys("drakonc@gmail.com")

time.sleep(2)

password = chorome_driver.find_element_by_name("pass")
password.send_keys("MariaLuisa07")

time.sleep(2)

button  = chorome_driver.find_element_by_name("login")
button.click()
# password.send_keys(Keys.ENTER)

time.sleep(2)

chorome_driver.execute_script("window.open('');")

time.sleep(2)

chorome_driver.switch_to.window(chorome_driver.window_handles[1])

time.sleep(2)

chorome_driver.get("https://gmail.com/")