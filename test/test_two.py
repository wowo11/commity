import unittest
import time
from pageobject.home_two import Delete
from pageobject.base_testcase import BaseTestCase
class Test_two(BaseTestCase):
    def test_login_two(self):
        shanchu = Delete(self.driver)
        shanchu.login()  # 登录
        shanchu.click_moren()  # 点击默认版块
        shanchu.shantie()  # 选中后删除，确定
        shanchu.newbankuai()    #新建版块
        shanchu.window_handles(1)
        shanchu.close_window()
        time.sleep(5)
        shanchu.window_handles(0)
        shanchu.exit_page()
        time.sleep(8)
        shanchu.login_common()
        shanchu.fahui('1111111111','2222222222222222222222222','33333333333333333')
        shanchu.exit_page()
if __name__ == "__main__":
    unittest.main()
