from selenium.webdriver.common.by import By
from framework.base import BasePage
import time
class Toupiao(BasePage):
    moren_search_loc = (By.CSS_SELECTOR, '.bm_c h2 a')      #默认版块


    fatie_search_loc = (By.ID, 'newspecial')
    toupiaoanniu=(By.CSS_SELECTOR,'.ct2_a_r li:nth-child(2) a')
    toupiaobiaoti=(By.ID, 'subject')
    choices_one=(By.XPATH,'//div/p/input[1]')
    choices_two = (By.XPATH, '//div/p[2]/input[1]')
    choices_three= (By.XPATH, '//div/p[3]/input[1]')
    faqi=(By.ID, 'postsubmit')

    zhuti=(By.CSS_SELECTOR,'.pl td h1 span')

    xuanxiang_one=(By.CSS_SELECTOR,'.pcht  table tr  td:nth-child(2) label')
    xuanxiang_one_pencent=(By.CSS_SELECTOR,'.pcht  table  tr:nth-child(2) td:nth-child(3)')

    xuanxiang_two = (By.CSS_SELECTOR, '.pcht  table  tr:nth-child(3) td:nth-child(2) label')
    xuanxiang_two_pencent = (By.CSS_SELECTOR, '.pcht  table  tr:nth-child(4) td:nth-child(3)')

    xuanxiang_three = (By.CSS_SELECTOR, '.pcht  table  tr:nth-child(5) td:nth-child(2) label')
    xuanxiang_three_pencent = (By.CSS_SELECTOR, '.pcht  table  tr:nth-child(6) td:nth-child(3)')

    def click_moren(self):
        self.click(*self.moren_search_loc)       # 点击默认版块

    def faqitoupiao(self,content4,content1,content2,content3):
        self.click(*self.fatie_search_loc)  # 发帖图片
        self.click(*self.toupiaoanniu)
        self.sendkeys(content4, *self.toupiaobiaoti)
        time.sleep(5)
        self.sendkeys(content1, *self.choices_one)
        self.sendkeys(content2, *self.choices_two)
        self.sendkeys(content3, *self.choices_three)
        time.sleep(2)
        self.click(*self.faqi)
        time.sleep(10)
    def get_zhuti(self):
        self.get_text(*self.zhuti)
    def toupiaoneirong1(self):
        self.get_text(*self.xuanxiang_one)

    def toupiaoneirong2(self):
        self.get_text(*self.xuanxiang_two)

    def toupiaoneirong3(self):
        self.get_text(*self.xuanxiang_three)
    def baifenbi1(self):
        self.get_text(*self.xuanxiang_one_pencent)

    def baifenbi2(self):
        self.get_text(*self.xuanxiang_two_pencent)

    def baifenbi3(self):
        self.get_text(*self.xuanxiang_three_pencent)








