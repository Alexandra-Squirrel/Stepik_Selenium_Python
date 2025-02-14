from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

##### Ваша программа должна выполнить следующие шаги:
# Открыть страницу https://suninjuly.github.io/math.html
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.

link = "https://suninjuly.github.io/math.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
    x = x_element.text
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