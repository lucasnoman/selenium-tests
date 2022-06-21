# pylint: disable=missing-docstring
# pylint: disable=import-error
# pylint: disable=relative-beyond-top-level
from selenium.webdriver.common.by import By

from page_objects.base_element import BaseElement


class TrainingGroundPage:

  def __init__(self, driver) -> None:
    self.driver = driver
    self.url = 'https://techstepacademy.com/training-ground/'

  def start(self):
    self.driver.get(self.url)

  # Esse @property permite chamar a função sem os parênteses
  @property
  def button1(self):
    locator = (By.ID, 'b1')
    return BaseElement(driver=self.driver, by=locator[0], value=locator[1])
