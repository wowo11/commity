from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os.path
from framework.logger import Logger
logger=Logger(logger='BasePage').getlog()

class BasePage(object):
    #构造函数
    def __init__(self,driver):
        self.driver=driver
    # 后退动作
    def back(self):
        self.driver.back()
        logger.info('click back on current page')
    # 前进动作
    def forward(self):
        self.driver.forward()
        logger.info('click forward on current page')
    #清除文本框内容
    def clear(self,*loc):
        a2=self.find_element(*loc)
        try:
            a2.clear()
        except Exception as e:
            # self.get_windows_img()
            logger.error('error:%s' %e)

    #根据网址打开页面
    def open_url(self,url):
        self.driver.get(url)
        time.sleep(5)
    #根据定位查找元素
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info('find the element,successful')
            return self.driver.find_element(*loc)
        except:
            logger.error('%s页未找到%s元素：'%(self,loc))
            self.get_windows_img()
    #捕获屏幕截图
    def get_windows_img(self):
        file = os.path.dirname(os.path.abspath('.')) + '/screenshots'
        content=time.strftime('%y%m%d%h%m',time.localtime((time.time())))
        name = file + content+'.png'
        try:
            self.driver.get_screenshot_as_file(name)
            logger.info('success:/screenshots')
        except Exception as e:
            logger.error('error:%s' % e)
            self.get_windows_img()
    #点击回车
    def sendkeys(self,text,*loc):
        a1 = self.find_element(*loc)
        # a1.clear()
        try:
            a1.send_keys(text)
            logger.info(text)
        except Exception as e:
            logger.error('error:%s' %e)
            self.get_windows_img()
    #点击
    def click(self,*loc):
        a3=self.find_element(*loc)
        try:
            a3.click()
            logger.info('click the element%s'%a3.text)
        except Exception as e:
            logger.error('error:%s' %e)
            self.get_windows_img()
    #关闭当前页面
    def close(self):
        try:
            self.driver.close()
            logger.info('exit')
        except Exception as e:
            logger.error('error：%s'%e)
    # 退出
    def quit_close(self):
        self.driver.quit()

    def window(self):
        window = self.driver.current_window_handle
        self.driver.switch_to.window(window)

    def window_handles(self, a):
        self.driver.switch_to.window(self.driver.window_handles[a])

    def close_window(self):
        self.driver.close()

    def switch_to(self,name):
        self.driver.switch_to.frame(name)

    def frame(self,id):
        self.driver.switch_to.frame(id)
    def login(self):
        name = self.driver.find_element_by_name('username')
        name.send_keys('admin')
        psd = self.driver.find_element_by_name('password')
        psd.send_keys('admin')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_tag_name('button').click()  # 点击登录

    def login_common(self):
        name = self.driver.find_element_by_id('ls_username')
        name.send_keys('123456')
        psd = self.driver.find_element_by_id('ls_password')
        psd.send_keys('123456')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_tag_name('button').click()  # 点击登录
    def exit_page(self):
        self.driver.find_element_by_link_text("退出").click()

    def get_text(self,*loc):
        try:
            e1=self.find_element(*loc)
            e2=e1.text
            logger.info('find %s' % e2)
            return e2
        except Exception as e:
            logger.error('element don''t find %s'%e)
            self.get_windows_img()