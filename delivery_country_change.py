import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestDeliveryCountryChange(unittest.TestCase):
    DELIVER_TO_ROMANIA_BUTTON = (By.XPATH, '//*[@id="glow-ingress-block"]')
    COUNTRY_LIST_BUTTON = (By.XPATH, '//*[@id="GLUXCountryListDropdown"]/span/span')
    ROMANIA_FIELD = (By.XPATH, '//*[@id="GLUXCountryList_183"]')
    DONE_BUTTON = (By.XPATH, '//*[@id="a-popover-1"]/div/div[2]/span/span/span/button')
    chrome = None

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.amazon.com/')

    def tearDown(self):
        self.chrome.quit()

    def test_delivery_country_change(self):
        self.chrome.find_element(*self.DELIVER_TO_ROMANIA_BUTTON).click()
        time.sleep(1)
        self.chrome.find_element(*self.COUNTRY_LIST_BUTTON).click()
        time.sleep(1)
        self.chrome.find_element(*self.ROMANIA_FIELD).click()
        time.sleep(1)
        self.chrome.find_element(*self.DONE_BUTTON).click()
        time.sleep(1)
