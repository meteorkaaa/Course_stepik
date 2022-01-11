from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text

    y = calc(x)
    print(y)
    put_x_element = browser.find_element(By.ID, 'answer')
    put_x_element.send_keys(y)
    
    browser.execute_script("window.scrollBy(0, 100);")
    
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