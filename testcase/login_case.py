from page.login_page import Login_Page
from selenium import webdriver
import unittest
import HTMLTestRunner
import os
import time

class LoginCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://111.229.90.117/index.php?route=account/login')
        self.lgp = Login_Page(self.driver)


    def test_login_err(self):
        login_err = self.lgp.login_err('123@163.com','123')
        return self.assertTrue(login_err,'fail')

    def test_login_success(self):
        self.lgp.login_case('123@163.com','123456')

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
    file_path = base_path + "/report/" + "login_case.html"
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(LoginCase('test_login_err'))
    suite.addTest(LoginCase('test_login_success'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is register_case report",description=u"这个是我们第一次测试报告",verbosity=2)
    runner.run(suite)