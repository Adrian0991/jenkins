import unittest
from selenium import webdriver
from pages.Home_page import HomePage


class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """

    def test_setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://seleniumdemo.com/")
        self.driver.implicitly_wait(10)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()