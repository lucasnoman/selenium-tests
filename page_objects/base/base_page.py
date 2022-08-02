class BasePage():
  url = None

  def __init__(self, driver) -> None:
    self.driver = driver

  def start(self):
    self.driver.get(self.url)
