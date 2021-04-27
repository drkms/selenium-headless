import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class TestTestisikagoogle():
  def setup_method(self, method):
    options = FirefoxOptions()
    options.add_argument("--headless")
    self.driver = webdriver.Firefox(firefox_binary="/usr/bin/firefox", options=options)
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_testisikagoogle(self):
    self.driver.get("https://www.google.com/")
    self.driver.find_element(By.NAME, "q").send_keys("selenium")
    self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
