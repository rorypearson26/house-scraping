from selenium.webdriver.common.by import By

from utils.base_driver import BaseDriver
from utils.xpath import Xpath

class Driver(BaseDriver):
    
    def get_by_xpath(self, xpath: Xpath, attribute: str = None):
        if attribute:
            return self.driver.find_element(By.XPATH(xpath.xpath)).get_attribute(attribute)
        else:
            return self.driver.find_element(By.XPATH(xpath)).text
        
    def get_elements_by_xpath(self, xpath: str):
        return self.driver.find_elements(By.XPATH(xpath))