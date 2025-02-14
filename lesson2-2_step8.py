from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Alexandra")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Squirrel")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("aleksandra@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file1.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.XPATH, "//input[@type='file']")
    element.send_keys(file_path)

    time.sleep(1)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в кон