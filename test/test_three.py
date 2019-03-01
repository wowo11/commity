import unittest
import time

from pageobject.homepage_three import Search
from pageobject.base_testcase import BaseTestCase
class Test_three(BaseTestCase):
    def test_common_login_three(self):
        ss = Search(self.driver)
        ss.login_common()
        ss.sousuo('haotest')
        actual=ss.jieguo()
        time.sleep(5)
        self.assertEqual(actual,'haotest',msg=actual)
        ss.exit_page()
if __name__ == "__main__":
    unittest.main()
