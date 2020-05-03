from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #Переходим по ссылке
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Находим значение переменной x
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    # Скролл страницы
    text_box = browser.find_element_by_id("answer").send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", text_box)
    # Заполняем текстовое поле
    #text_box = browser.find_element_by_id("answer").send_keys(y)
    # Чекбокс
    check_box = browser.find_element_by_id('robotCheckbox').click()
    # Радиобокс
    radio_box = browser.find_element_by_id('robotsRule').click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
