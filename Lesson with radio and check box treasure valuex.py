from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute("valuex")

    y = calc(x)

    put_x_element = browser.find_element(By.ID, 'answer')
    put_x_element.send_keys(y)

    activate_box = browser.find_element(By.ID, "robotCheckbox")
    activate_box.click()

    robots_rule = browser.find_element(By.ID, 'robotsRule')
    robots_rule.click()
  

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()




    time.sleep(1)




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
