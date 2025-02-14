from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.TAG_NAME, 'img')
    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
    x = x_element.get_attribute("valuex")
    # Используйте функцию calc(), которая рассчитает и вернет вам значение функции
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    time.sleep(1)

    checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox.click()
    checkbox = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    checkbox.click()
    time.sleep(1)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла