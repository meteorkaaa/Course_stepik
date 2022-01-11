
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    journey_button = browser.find_element(By.TAG_NAME, 'button')
    journey_button.click()

    browser.switch_to.window(browser.window_handles[1])



    get_num = browser.find_element(By.ID, 'input_value')

    xv = get_num.text

    input_value = browser.find_element(By.ID, 'answer')
    input_value.send_keys(calc(xv))

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button')
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
