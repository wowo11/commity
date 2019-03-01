from selenium.webdriver.common.by import By
from framework.base import BasePage
import time
from ddt import unpack

class Search(BasePage):
    time.sleep(10)
    sousuokuang=(By.ID,'scbar_txt')
    # sousuokuang=(By.NAME,'srchtxt')
    ss_btn=(By.ID,'scbar_btn')
    # ss_btn = (By.NAME, 'searchsubmit')
    tiezi=(By.CSS_SELECTOR,'.pbw h3 a')
    def sousuo(self,content1):
        self.sendkeys(content1,*self.sousuokuang)
        self.click(*self.ss_btn)
        time.sleep(3)
        self.window_handles(1)
    def jieguo(self):
        rs=self.get_text(*self.tiezi)
        return  rs












