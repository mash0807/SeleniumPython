from util.readData import ReadData
from keywordmethod.keywordMethod import KeyWordMethod

class KeyWordCase(object):
    def run_case(self):
        self.keywordmethod = KeyWordMethod()
        case_excel = ReadData('D:\\Selenium_2020\\Register_Bokeyuan\\config\\register_case.xls')
        case_lines = case_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                is_run = case_excel.get_col_value(i,3)
                if is_run == 'yes':
                    method = case_excel.get_col_value(i, 4)
                    handle_element = case_excel.get_col_value(i, 5)
                    send_value = case_excel.get_col_value(i, 6)
                    except_result_method = case_excel.get_col_value(i, 7)
                    except_result = case_excel.get_col_value(i, 8)
                    self.run_method(method, handle_element,send_value)
                    #判断是否有预期结果，如果有，根据预期结果比对后回写实际结果字段
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                case_excel.write_value(i,9,'pass')
                            else:
                                case_excel.write_value(i,9,'fail')


    def run_method(self,method,handle_element='',send_value=''):
        #根据excel中的method来获取kewordmethod中的实际方法
        method_value = getattr(self.keywordmethod, method)
        #通过四种情况，来判断传入的参数值
        if handle_element == '' and send_value != '':
            result = method_value(send_value,node='RegisterElement')
        elif handle_element != '' and send_value != '':
            result = method_value(handle_element, send_value,node='RegisterElement')
        elif handle_element != '' and send_value == '':
            result = method_value(handle_element,node='RegisterElement')
        else:
            result = method_value(node='RegisterElement')
        return result

    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')

if __name__ == '__main__':
    test = KeyWordCase()
    test.run_case()