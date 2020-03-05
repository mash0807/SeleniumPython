import unittest
import os
import HTMLTestRunner
class RunAllCase(unittest.TestCase):
    #运行文件夹下所有以_case结尾的用例
    def test_case(self):
        case_path = os.path.join(os.getcwd())
        suite = unittest.defaultTestLoader.discover(case_path,'*_case.py')
        #unittest.TextTestRunner().run(suite)
        base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        file_path = base_path + "/report/" + "run_case.html"
        f = open(file_path, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is register_case report",
                                               description=u"这个是我们第一次测试报告", verbosity=2)
        runner.run(suite)

if __name__ == '__main__':
    unittest.main()