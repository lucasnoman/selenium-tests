# pylint: disable=missing-docstring
import sys
from selenium import webdriver

from pages.training_ground_page import TrainingGroundPage
from pages.trial_page import TrialPage

sys.path.append('..')

# Testing setup
browser = webdriver.Edge()

# Trial Page
trial_page = TrialPage(driver=browser)
trial_page.start()
trial_page.stone_input.input_text('rock')
trial_page.stone_button.click()
input()  # para a página aqui, que fica esperando por algum input

# Training Grounds
training_page = TrainingGroundPage(driver=browser)
training_page.start()
assert training_page.button1.text == 'Button1', 'Unexpected button text'

input()
browser.quit()
