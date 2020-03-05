from page.address_page import Address_Page
from page.login_page import Login_Page
from selenium import webdriver
import unittest
import HTMLTestRunner
import os
import time

class AddressCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://111.229.90.117/index.php?route=account/login')
        self.adp = Address_Page(self.driver)
        self.lgp = Login_Page(self.driver)

    def test_address_add(self):
        self.lgp.login_case('1131826605@qq.com','123456')
        time.sleep(2)
        self.adp.address_add_case('ming','xing','家庭地址','北京','China','Hong Kong')


    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join("D:\\Selenium_2020\\Register_Bokeyuan\\report\\"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

if __name__ == '__main__':
    base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    file_path = base_path + "/report/" + "address_case.html"
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(AddressCase('test_address_add'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is register_case report",description=u"这个是我们第一次测试报告",verbosity=2)
    runner.run(suite)