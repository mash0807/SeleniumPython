from page.basepage import BasePage
import time

class Buy_Page(BasePage):
    def __init__(self,driver):
        self.buy = BasePage(driver,node='BuyElement')

    def buy_case(self):
        #先调用登录case后再运行
        self.buy.find_element('cart').click()
        self.buy.find_element('gobuy').click()
        time.sleep(1)
        self.buy.find_element('payaddresscontinue').click()
        time.sleep(1)
        self.buy.find_element('shopaddresscontinue').click()
        time.sleep(1)
        self.buy.find_element('methodcontinue').click()
        time.sleep(1)
        self.buy.find_element('agree').click()
        time.sleep(1)
        self.buy.find_element('paymethod').click()
        time.sleep(1)
        self.buy.find_element('confirm').click()