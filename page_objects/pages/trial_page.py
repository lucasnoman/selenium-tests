from selenium.webdriver.common.by import By

from base.base_element import BaseElement
from base.base_page import BasePage
from base.locator import Locator


class TrialPage(BasePage):
  url = 'https://techstepacademy.com/trial-of-the-stones/'

  @property
  def stone_input(self):
    locator = Locator(By.CSS_SELECTOR, 'input#r1Input')
    return BaseElement(driver=self.driver, locator=locator)

  @property
  def stone_button(self):
    locator = Locator(By.CSS_SELECTOR, 'button#r1Btn')
    return BaseElement(driver=self.driver, locator=locator)

  @property
  def secrets_input(self):
    locator = Locator(By.CSS_SELECTOR, 'input#r2Input')
    return BaseElement(driver=self.driver, locator=locator)

  @property
  def secrets_button(self):
    locator = Locator(By.CSS_SELECTOR, 'button#r2Butn')
    return BaseElement(driver=self.driver, locator=locator)
