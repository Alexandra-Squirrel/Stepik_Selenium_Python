from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# вот вам функция для копирования ответа с алерта
def copy_accept_code_to_clipboard(driver: WebDriver) -> None:
    alert = driver.switch_to.alert
    alert_text = alert.text
    accept_code = alert_text.split(':')[-1].strip()
    os.system(f'echo {accept_code} | xclip -selection clipboard')

# press button block
def click_button():
  button = browser.find_element(By.TAG_NAME, "button")
  button.click()

try:
    browser = webdriver.Chrome()
    browser.get(link)
    click_button()
    # window block
    browser.switch_to.alert.accept()
    # calculation block
    time.sleep(1)
    x_element = browser.find_element(By.ID, "input_value")
    y = calc(x_element.text)
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)
    click_button()
    time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в кон