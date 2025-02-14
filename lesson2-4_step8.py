from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Дождаться, когда цена (#price) дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    # Нажать на кнопку "Book" (#book)
    button = browser.find_element(By.ID, "book")
    button.click()

    # # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    # button = WebDriverWait(browser, 12).until(
    #     EC.element_to_be_clickable((By.ID, "verify"))
    # )
    # button.click()
    # message = browser.find_element(By.ID, "verify_message")

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x_element = browser.find_element(By.ID, "input_value")
    y = calc(x_element.text)
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)
    time.sleep(1)
    browser.find_element(By.ID, "solve").click()
    time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # не забываем оставить пустую строку в кон
