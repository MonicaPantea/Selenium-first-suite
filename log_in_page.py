import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogIn(unittest.TestCase):
    ACCOUNT_BUTTON = (By.XPATH, '//*[@id="nav-link-accountList-nav-line-1"]')
    LOG_IN_BUTTON = (By.XPATH, '//*[@id="nav-flyout-ya-newCust"]/a')
    INPUT_NAME_BOX = (By.XPATH, '//*[@id="ap_customer_name"]')
    INPUT_MAIL_BOX = (By.XPATH, '//*[@id="ap_email"]')
    INPUT_PASSWORD_BOX = (By.XPATH, '//*[@id="ap_password"]')
    CHECK_PASSWORD_BOX = (By.XPATH, '//*[@id="ap_password_check"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="continue"]')
    PASSWORD_CHARACTERS_MESSAGE = (By.XPATH, '//*[@id="ap_register_form"]/div/div/div[3]/div[1]/div[1]/div/div')
    ERROR_MESSAGE = (By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[1]/div/div/h4')
    chrome = None

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.amazon.com/')

    def tearDown(self):
        self.chrome.quit()

    def test_log_in(self) -> None:
        a = ActionChains(self.chrome)
        account_button = self.chrome.find_element(*self.ACCOUNT_BUTTON)
        a.move_to_element(account_button).perform()
        log_in_button = self.chrome.find_element(*self.LOG_IN_BUTTON)
        a.move_to_element(log_in_button).click().perform()

        self.chrome.find_element(*self.INPUT_NAME_BOX).send_keys('Monica')
        self.chrome.find_element(*self.INPUT_MAIL_BOX).send_keys('Monica@gmail.com')

        elem = self.chrome.find_element(*self.PASSWORD_CHARACTERS_MESSAGE)
        self.assertTrue(elem.is_displayed(), 'Mesajul nu e vizibil')

        self.chrome.find_element(*self.INPUT_PASSWORD_BOX).send_keys('Monica22')
        self.chrome.find_element(*self.CHECK_PASSWORD_BOX).send_keys('Monica22')
        self.chrome.find_element(*self.CONTINUE_BUTTON).click()

        actual = self.chrome.find_element(*self.ERROR_MESSAGE).text
        expected = 'Email address already in use'
        self.assertEqual(expected, actual, 'Error message is incorrect')




