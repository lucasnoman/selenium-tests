# pylint: disable=missing-docstring
# pylint: disable=relative-beyond-top-level
# pylint: disable=import-error
from selenium import webdriver
from page_objects.training_ground_page import TrainingGroundPage

# Testing setup
browser = webdriver.Edge()
TEST_VALUE = 'it worked'

# Testing
training_page = TrainingGroundPage(driver=browser)
training_page.start()
assert training_page.button1.text == 'Button1'
browser.quit()
