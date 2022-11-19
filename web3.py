import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))


# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "book")))
button.click()

b2 = browser.find_element(By.ID, "input_value").text
x = calc(b2)

b3 = browser.find_element(By.CLASS_NAME, "form-control")
b3.send_keys(x)

b4 = browser.find_element(By.CSS_SELECTOR, "#solve")
b4.click()

time.sleep(10)