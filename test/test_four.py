import unittest
import time
from pageobject.homepage_four import Toupiao
from pageobject.base_testcase import BaseTestCase
class Test_four(BaseTestCase):
    def test_toupiao(self):
        tp = Toupiao(self.driver)
        tp.login_common()
        time.sleep(4)
        tp.click_moren()
        time.sleep(5)
        tp.faqitoupiao('星期天是学习还是休息？','学习','休息','劳逸结合')
        time.sleep(10)
        tp.get_zhuti()
        tp.toupiaoneirong1()
        tp.toupiaoneirong2()
        tp.toupiaoneirong3()
        tp.baifenbi1()
        tp.baifenbi2()
        tp.baifenbi3()
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()
