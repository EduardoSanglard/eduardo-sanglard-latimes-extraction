# Generated by Selenium IDE
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestMain():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_main(self):
    # Test name: Main
    # Step # | name | target | value
    # 1 | open | / | 

    # Increase timeout
    self.driver.set_page_load_timeout(30000)

    self.driver.get("https://www.latimes.com/")
    # 2 | setWindowSize | 1439x680 | 
    self.driver.maximize_window()
    # 3 | mouseOver | css=.px-2\.5 | 
    self.driver.find_element(By.CSS_SELECTOR, ".xs-5\\3Ah-6 > use").click()
    # 6 | click | name=q | 
    self.driver.find_element(By.NAME, "q").click()
    # 7 | type | name=q | Iran
    self.driver.find_element(By.NAME, "q").send_keys("Iran")
    # 8 | click | css=.h-6\.25 | 
    self.driver.find_element(By.CSS_SELECTOR, ".h-6\\.25").click()
    # 9 | click | id=modality-584782890322 | 
    self.driver.find_element(By.ID, "modality-584782890322").click()
    # 10 | click | name=f0 | 
    self.driver.find_element(By.NAME, "f0").click()
    # 11 | mouseOver | name=f0 | 
    element = self.driver.find_element(By.NAME, "f0")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 12 | mouseOut | name=f0 | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 13 | mouseOver | name=f0 | 
    element = self.driver.find_element(By.NAME, "f0")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 14 | mouseOut | name=f0 | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 15 | mouseOver | css=.search-filter:nth-child(1) li:nth-child(2) .checkbox-input-element:nth-child(1) | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".search-filter:nth-child(1) li:nth-child(2) .checkbox-input-element:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 16 | runScript | window.scrollTo(0,300) | 
    self.driver.execute_script("window.scrollTo(0,300)")
    # 17 | mouseOut | css=.search-filter:nth-child(1) li:nth-child(2) .checkbox-input-element:nth-child(1) | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 18 | runScript | window.scrollTo(0,400) | 
    self.driver.execute_script("window.scrollTo(0,400)")
    # 19 | mouseOver | css=.search-filter:nth-child(1) li:nth-child(3) .checkbox-input-element:nth-child(1) | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".search-filter:nth-child(1) li:nth-child(3) .checkbox-input-element:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 20 | click | css=.search-filter:nth-child(1) li:nth-child(3) .checkbox-input-element:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".search-filter:nth-child(1) li:nth-child(3) .checkbox-input-element:nth-child(1)").click()
    # 21 | mouseOut | css=.search-filter:nth-child(1) li:nth-child(3) .checkbox-input-element:nth-child(1) | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 22 | click | css=.search-results-module-filters-selected-filter:nth-child(2) .icon | 
    self.driver.find_element(By.CSS_SELECTOR, ".search-results-module-filters-selected-filter:nth-child(2) .icon").click()
    # 23 | close |  | 
    self.driver.close()
  
def main():
  test = TestMain()
  test.setup_method(None)
  test.test_main()
  test.teardown_method(None)

if __name__ == "__main__":
  main()