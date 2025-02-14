from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

link = "https://suninjuly.github.io/selects1.html"
def calc(x1, x2):
  return str(x1 + x2)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element(By.ID, "num1")
    x2_element = browser.find_element(By.ID, "num2")
    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
    x1 = int(x1_element.text)
    x2 = int(x2_element.text)
    # Используйте функцию calc(), которая рассчитает и вернет вам значение функции
    y = calc(x1, x2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)  # ищем элемент списка со значением y
    time.sleep(1)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла