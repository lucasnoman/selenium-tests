# pylint: disable=missing-docstring
import sys
from base.base_element import BaseElement
from base.base_page import BasePage

from selenium.webdriver.common.by import By

sys.path.append('..')


class TrainingGroundPage(BasePage):

  url = 'https://techstepacademy.com/training-ground/'

  # Esse @property permite chamar a função sem os parênteses
  @property
  def button1(self):
    locator = (By.ID, 'b1')
    return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
