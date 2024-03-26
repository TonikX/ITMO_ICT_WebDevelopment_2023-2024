from selenium import webdriver
import time

# Инициализация браузера
driver = webdriver.Chrome()

# 1. Проверка доступности страницы регистрации, когда вход в аккаунт не выполнен
# Открытие веб-страницы
driver.get("http://localhost:8000/register/")

# Ожидание результата
time.sleep(2)

# Проверка результата
assert driver.current_url == "http://localhost:8000/register/"

# 2. Проверка доступности страницы регистрации, когда вход в аккаунт выполнен
# Открытие веб-страницы
driver.get("http://localhost:8000/")

# Взаимодействие с элементами страницы
username_input = driver.find_element("name", "username")
username_input.send_keys("katrin")

pwd_input = driver.find_element("name", "password")
pwd_input.send_keys("trs56245")

submit_button = driver.find_element("xpath", "//button[text()='Вход']")
submit_button.click()

# Ожидание результата
time.sleep(2)

# Открытие веб-страницы
driver.get("http://localhost:8000/register/")

# Ожидание результата
time.sleep(2)

# Проверка результата
assert driver.current_url == "http://localhost:8000/"

# 3. Проверка доступности страницы регистрации после выхода из аккаунта
# Взаимодействие с элементами страницы
logout_button = driver.find_element('xpath', "//a[@href='/logout/']")
logout_button.click()

# Ожидание результата
time.sleep(2)

# Открытие веб-страницы
driver.get("http://localhost:8000/register/")

# Ожидание результата
time.sleep(2)

# Проверка результата
assert driver.current_url == "http://localhost:8000/register/"

# Закрытие браузера
driver.quit()
