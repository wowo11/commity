from framework.browser_engine import BrowserEngine
import unittest,time
from selenium import webdriver
browser=BrowserEngine()
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=browser.open_browser()
        time.sleep(3)
    def tearDown(self):
        self.driver=browser.quit_browser()