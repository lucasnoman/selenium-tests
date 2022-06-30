# pylint: disable=missing-docstring
# pylint: disable=import-error
import sys

from selenium.webdriver.common.by import By

from base.base_element import BaseElement
from base.base_page import BasePage
from base.locator import Locator

sys.path.append('..')


class TrainingGroundPage(BasePage):

  url = 'https://techstepacademy.com/training-ground/'

  # Esse @property permite chamar a função sem os parênteses
  @property
  def button1(self):
    locator = Locator(by=By.ID, value='b1')
    return BaseElement(driver=self.driver, locator=locator)
