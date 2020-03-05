import xlrd
from xlutils.copy import copy
import time

class ReadData(object):
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.excel_path = "D:\\Selenium_2020\\Register_Bokeyuan\\config\\register_data.xls"
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]

    #获取excel中数据
    def get_data(self):
        result = []
        for i in range(self.get_lines()):
            col = self.table.row_values(i)
            result.append(col)
        return result

    #获取行数
    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    #获取单元格的数据
    def get_col_value(self,row,col):
        if self.get_lines() > row :
            data = self.table.cell(row,col).value
            return data
        return None

    #写入数据
    def write_value(self,row,col,value):
        #写数据之前复制excel内原有内容
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, col, value)
        write_data.save(self.excel_path)
        time.sleep(1)



