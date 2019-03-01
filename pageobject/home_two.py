from selenium.webdriver.common.by import By
from framework.base import BasePage
import time
class Delete(BasePage):
    moren_search_loc = (By.CSS_SELECTOR, '.bm_c h2 a')      #默认版块

    xuanzhong_shan=(By.CSS_SELECTOR, '.o input')        #选中要删除帖子前的方框
    click_delete=(By.LINK_TEXT,'删除')        #点击删除超链接
    sure_btn=(By.NAME,'modsubmit')             #点击弹出框的确定按钮

    managecenter=(By.LINK_TEXT,'管理中心')      #管理中心
    luntan = (By.CSS_SELECTOR, '.nav li:nth-child(7)')      #选中论坛

    addbankuai=(By.CSS_SELECTOR, '.lastboard a')            #点击新建板块
    # xinmingcheng=(By.XPATH,'//tbody/tr/td/div[@class='board']/input/[@name='newforum[1][]']')
    tijiao_bankuai=(By.CSS_SELECTOR, '.fixsel input')

    xinbankuai = (By.LINK_TEXT, '新版块名称')        #点击新版块
    biaoti=(By.ID, 'subject')                       #标题
    fa_neirong = (By.ID, 'fastpostmessage')         #发帖内容
    huifu_tuichu_btn = (By.ID, 'fastpostsubmit')      #发表
    huifuneirong=(By.ID, 'fastpostmessage')     #回复内容
    sendinf_btn = (By.ID, 'fastpostsubmit')     #发送回复
    def click_moren(self):
        self.click(*self.moren_search_loc)       # 点击默认版块
    def shantie(self):
        self.click(*self.xuanzhong_shan)    #选中要删除帖子前的方框
        self.click(*self.click_delete)      #点击删除超链接
        self.click(*self.sure_btn)          #点击弹出框的确定按钮

    def newbankuai(self):
        self.click(*self.managecenter)      #管理中心
        time.sleep(5)
        self.window_handles(1)
        self.click(*self.luntan)        #选中论坛
        self.switch_to('main')
        self.click(*self.addbankuai)        #点击新建板块
        self.click(*self.tijiao_bankuai)      #点击提交

    def fahui(self,content1,content2,content3):
        self.click(*self.xinbankuai)
        self.sendkeys(content1,*self.biaoti)
        self.sendkeys(content2, *self.fa_neirong)
        self.click(*self.huifu_tuichu_btn)
        time.sleep(2)
        self.sendkeys(content3,*self.huifuneirong)
        self.click(*self.sendinf_btn)  # 发送






