# Para criar um venv: python3 -m venv /path/to/new/virtual/environment
# pylint: disable=invalid-name
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('https://techstepacademy.com/training-ground')
original_window = driver.current_window_handle  # salva o id da página atual
driver.switch_to.new_window('tab')  # abre uma nova aba

for wh in driver.window_handles:
  if wh != original_window:
    driver.switch_to.new_window(original_window)  # retorna a aba original
    break

# ---- Método para esperar algo
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.expected_conditions import alert_is_present
# print('Arrived')
# WebDriverWait(driver, 10).until(alert_is_present())
# print('An alert appeared')

# ---- Método para usar em <select><option></option></select>
# from selenium.webdriver.support.select import Select
# sel = driver.find_element(By.ID, 'sel1')
# my_select = Select(sel)
# my_select.select_by_visible_text('Battlestar Galactica')
# my_select.select_by_index(0)
# my_select.select_by_value('second')
# print(my_select.first_selected_option.text)
