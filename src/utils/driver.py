from selenium.webdriver.common.by import By

from utils.base_driver import BaseDriver

class Driver(BaseDriver):
    def find_by_xpath(self, xpath: str, attribute: str = None):
        if attribute:
            return self.driver.find_element(By.XPATH(xpath)).get_attribute(attribute)
        else:
            return self.driver.find_element(By.XPATH(xpath))