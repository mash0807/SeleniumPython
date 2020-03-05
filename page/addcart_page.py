from page.basepage import BasePage
import time

class AddCart_Page(BasePage):
    #加入购物车页面测试
    def __init__(self,driver):
        self.addcart = BasePage(driver,node='AddCartElement')

    def addcart_case(self):
        #先调用登录case后再运行
        self.addcart.find_element('book').click()
        self.addcart.find_element('literature').click()
        self.addcart.find_element('addcart').click()