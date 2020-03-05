import configparser
class ReadINI(object):
    def __init__(self,filename=None,node=None):
        #初始化，如果调用没有传入读取的ini文件地址和节点，则默认读取config.ini中的RegisterElement节点配置
        if filename == None:
            self.filename = 'D:\Selenium_2020\Register_Bokeyuan\config\config.ini'
        else:
            self.filename = filename
        if node == None:
            self.node = 'RegisterElement'
        else:
            self.node = node
        #加载ini文件
        self.cf = self.loadINI(self.filename)

    #根据文件名字加载ini配置内容
    def loadINI(self,filename):
        cf = configparser.ConfigParser()
        cf.read(filename)
        return cf

    #获取对应配置值
    def get_value(self,key):
        element = self.cf.get(self.node,key)
        return element
