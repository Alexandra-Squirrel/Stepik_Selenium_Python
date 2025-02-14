from selenium import webdriver
from selenium.webdriver.common.by import By

# Если значение атрибута отсутствует, то это равносильно значению атрибута равному "false".
# Давайте еще раз взглянем на страницу http://suninjuly.github.io/math.html
# На ней есть radiobuttons, для которых выбрано значение по умолчанию.
# В автотесте нам может понадобиться проверить, что для одного из radiobutton по умолчанию уже выбрано значение.
# Для этого мы можем проверить значение атрибута checked у этого элемента.
#
# Вот HTML-код элемента:
# <input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>

# Найдём этот элемент с помощью WebDriver:
people_radio = browser.find_element(By.ID, "peopleRule")
# Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)

assert people_checked is not None, "People radio is not selected by default"
# ИЛИ
assert people_checked == "true", "People radio is not selected by default"

robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None

# "true" написано с маленькой буквы, — все методы WebDriver взаимодействуют с браузером с помощью JavaScript,
# в котором булевые значения пишутся с маленькой буквы, а не с большой, как в Python.

# Так же мы можем проверять наличие атрибута disabled, (может ли пользователь взаимодействовать с элементом).
# В предыдущем задании на странице с капчей для роботов JavaScript устанавливает атрибут disabled у кнопки Submit,
# когда истекает время, отведенное на решение задачи.

# <button type="submit" class="btn btn-default" disabled>Submit</button>