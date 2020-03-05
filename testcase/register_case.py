from page.register_page import Register_Page
from selenium import webdriver
import unittest
import HTMLTestRunner
import os
import time
import ddt
from util.readData import ReadData
from util.caselog import CaseLog

rd = ReadData("D:\\Selenium_2020\\Register_Bokeyuan\\config\\register_data.xls")
data = rd.get_data()
@ddt.ddt
class RegisterCase(unittest.TestCase):
    #定义日志
    @classmethod
    def setUpClass(cls):
        cls.log = CaseLog()
        cls.logger = cls.log.get_log()
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://111.229.90.117/index.php?route=account/register')
        self.rgp = Register_Page(self.driver)
        self.logger.info("开始数据执行")

    #def test_register_phone_err(self):
     #   phone_err = self.rgp.register_phone_err('zhang66666666666666666666666666666666666666666666666666666','san','1@163.com','8','123456')
      #  return self.assertFalse(phone_err,phone_err)
    #通过excel传入测试数据
    @ddt.data(*data)
    def test_register_success(self,data):
        firstname,lastname,email,phone,password = data
        err_text = self.rgp.register_case(firstname,lastname,email,phone,password)
        return self.assertFalse(err_text, err_text)

    def tearDown(self):
        time.sleep(2)
        #进行错误截图
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join("D:\\Selenium_2020\\Register_Bokeyuan\\report\\"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
if __name__ == '__main__':

    base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    file_path = base_path + "/report/" + "register_case.html"
    #file_path = 'D:\\Selenium_2020\\Register_Bokeyuan\\report\\register_case.html'
    #print(base_path)
    #print(111)
    f = open(file_path,'wb')
    #suite = unittest.TestSuite()
    #suite.addTest(RegisterCase('test_register_phone_err'))
    #suite.addTest(RegisterCase('test_register_success'))
    suite = unittest.TestLoader().loadTestsFromTestCase(RegisterCase)
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is register_case report",description=u"这个是我们第一次测试报告",verbosity=2)
    runner.run(suite)