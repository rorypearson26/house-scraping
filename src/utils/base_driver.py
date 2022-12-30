from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BaseDriver:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.find_element()
    
    def go_to_url(self, url: str):
        self.driver.get(url)
        