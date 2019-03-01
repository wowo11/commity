import unittest
import time
from pageobject.base_testcase import BaseTestCase
from pageobject.homepage_one import Fatie
class Test_one(BaseTestCase):
    def test_login_one(self):
        fatie = Fatie(self.driver)
        fatie.login()
        time.sleep(3)
        fatie.search("wqqwqqqqq","ggggggggggg","qqqqqqqqqqqqqqqqqqqqqq")
        fatie.exit_page()
if __name__=="__main__":
    unittest.main()
