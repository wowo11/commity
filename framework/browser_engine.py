import os.path
from configparser import ConfigParser
from  selenium import webdriver
from framework.logger import Logger

logger=Logger(logger='BrowserEngine').getlog()

class BrowserEngine(object):
    dir_path=os.path.dirname(os.path.abspath('.'))
    firefox_path =dir_path +'/tools/geckodriver.exe'
    Chrome_path =dir_path +'/tools/chromedriver.exe'
    IE_path =dir_path +'/tools/IEDriverServer.exe'
    def open_browser(self):
        config=ConfigParser()
        file=os.path.dirname(os.path.abspath('.'))+'/config/file.ini'
        config.read(file)
        browser=config.get('browserType','browserName')
        logger.info('选择浏览器：%s'% browser)
        url=config.get('testServer','URL')
        logger.info('地址：%s'% url)
        if browser=='Chrome':
            self.driver = webdriver.Chrome(self.Chrome_path)
            logger.info('打开Chrome浏览器')
        elif browser=='IE':
            self.driver = webdriver.Ie(self.IE_path)
            logger.info('打开IE浏览器')
        elif browser=='Firefox':
            self.driver=webdriver.Firefox(self.firefox_path)
            logger.info('打开火狐浏览器')
        self.driver.get(url)
        logger.info('打开网址')
        # self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        return  self.driver

    def quit_browser(self):
        logger.info('退出浏览器')
        self.driver.quit()