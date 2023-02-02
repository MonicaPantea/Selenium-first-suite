import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestFirstPage(unittest.TestCase):
    AMAZON_BUTTON = (By.XPATH, '//*[@id="nav-logo-sprites"]')
    DELIVER_TO_ROMANIA_BUTTON = (By.XPATH, '//*[@id="glow-ingress-block"]')
    SELECT_CATEGORIES_BUTTON = (By.XPATH, '//*[@id="searchDropdownBox"]')
    SEARCH_BOX = (By.XPATH, '//*[@id="twotabsearchtextbox"]')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="nav-search-submit-button"]')
    LANGUAGE_BUTTON = (By.XPATH, '//*[@id="icp-nav-flyout"]/span/span[2]/span[1]')
    ACCOUNT_BUTTON = (By.XPATH, '//*[@id="nav-link-accountList-nav-line-1"]')
    ORDERS_BUTTON = (By.XPATH, '//*[@id="nav-orders"]/span[1]')
    CART_BUTTON = (By.XPATH, '//*[@id="nav-cart-text-container"]')
    COPYRIGHT_SYMBOL = (By.XPATH, '//*[@id="navFooter"]/div[5]/span')
    chrome = None

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.amazon.com/')

    def tearDown(self):
        self.chrome.quit()

    def test_url(self) -> None:
        actual = self.chrome.current_url
        expected = 'https://www.amazon.com/'
        self.assertEqual(expected, actual, 'URL is incorrect')

    def test_amazon_button(self):
        self.chrome.find_element(*self.AMAZON_BUTTON).click()

    def test_deliver_to_romania_button(self):
        self.chrome.find_element(*self.DELIVER_TO_ROMANIA_BUTTON).click()

    def test_select_categories_button(self):
        self.chrome.find_element(*self.SELECT_CATEGORIES_BUTTON).click()

    def test_search_box(self):
        self.chrome.find_element(*self.SEARCH_BOX).send_keys('Gift')

    def test_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def test_language_button(self):
        self.chrome.find_element(*self.LANGUAGE_BUTTON).click()

    def test_account_button(self):
        self.chrome.find_element(*self.ACCOUNT_BUTTON).click()

    def test_orders_button(self):
        self.chrome.find_element(*self.ORDERS_BUTTON).click()

    def test_cart_button(self):
        self.chrome.find_element(*self.CART_BUTTON).click()

    def test_copyright_symbol_is_displayed(self):
        elem = self.chrome.find_element(*self.COPYRIGHT_SYMBOL)
        self.assertTrue(elem.is_displayed(), 'Simbolul nu e vizibil')
