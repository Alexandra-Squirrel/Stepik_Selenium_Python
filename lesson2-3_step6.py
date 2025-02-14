from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.TAG_NAME, "button").click()

    # switch window
    # first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # calculation block
    x_element = browser.find_element(By.ID, "input_value")
    y = calc(x_element.text)
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)
    time.sleep(1)
    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в кон