from page.basepage import BasePage
from selenium import webdriver
import time

class KeyWordMethod(object):
    #打开浏览器操作
    def open_browser(self,browser,node):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    #根据传入url打开网址
    def get_url(self,url,node):
        result = self.driver.get(url)
        return result

    #调用BasePage定位页面元素
    def find_element(self,element,node):
        el = BasePage(self.driver,node)
        return el.find_element(element)

    #输入内容
    def element_send_keys(self,element,value,node):
        self.find_element(element,node).send_keys(value)

    #点击元素操作
    def click_element(self,element,node):
        self.find_element(element,node).click()

    #等待操作
    def sleep_time(self,second,node):
        time.sleep(second)

    #关闭浏览器
    def close_browser(self,node):
        self.driver.close()

    #获取title值
    def get_title(self,node):
        return self.driver.title