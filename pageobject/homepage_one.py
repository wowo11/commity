from selenium.webdriver.common.by import By
import time
from framework.base import BasePage
class Fatie(BasePage):
    moren_search_loc = (By.CSS_SELECTOR, '.bm_c h2 a')      #默认版块

    fatie_search_loc = (By.ID, 'newspecial')                #发帖
    biaoti_search_loc=(By.ID,'subject')                     #标题

    kuangjia=(By.TAG_NAME,'iframe')                         #iframe
    neirong_loc = (By.TAG_NAME,'body')                         #框架内主体

    sendinf_btn=(By.ID, 'postsubmit')                           #发送按钮
    huifu=(By.ID, 'fastpostmessage')                              #回复消息
    huifu_tuichu_btn=(By.ID, 'fastpostsubmit')                #参与回复
    def search(self, content1,content2,content3):
        self.click(*self.moren_search_loc)       # 点击默认版块
        self.window()
        time.sleep(1)
        self.click(*self.fatie_search_loc)      # 发帖图片
        time.sleep(3)
        self.sendkeys(content1, *self.biaoti_search_loc)#标题
        self.frame('e_iframe')
        self.sendkeys(content2, *self.neirong_loc)  #发帖内容
        self.window()               #激活外面窗口
        time.sleep(1)
        self.click(*self.sendinf_btn)           #发送
        time.sleep(5)
        self.window()
        self.sendkeys(content3, *self.huifu)  # 回复内容
        self.click(*self.huifu_tuichu_btn)      #回复按钮


