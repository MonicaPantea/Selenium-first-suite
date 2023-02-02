import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLanguageChange(unittest.TestCase):
    LANGUAGE_BUTTON = (By.XPATH, '//*[@id="icp-nav-flyout"]/span/span[2]/span[1]')
    SPANISH_FIELD = (By.XPATH, '//*[@id="icp-language-settings"]/div[3]/div/label/span/span')
    SAVE_CHANGE_BUTTON = (By.XPATH, '//*[@id="icp-save-button"]/span/input')
    chrome = None

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.amazon.com/')

    def tearDown(self):
        self.chrome.quit()

    def test_language_change(self):
        self.chrome.find_element(*self.LANGUAGE_BUTTON).click()
        time.sleep(1)
        self.chrome.find_element(*self.SPANISH_FIELD).click()
        time.sleep(1)
        self.chrome.find_element(*self.SAVE_CHANGE_BUTTON).click()
        time.sleep(1)
