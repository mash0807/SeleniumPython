from util.readINI import ReadINI

class FindElement(object):
    def __init__(self):
        self.ri = ReadINI()

    #通过读取ini中的配置值区分定位元素方式
    def find_element(self,key):
        by = (self.ri.get_value(key)).split('>')[0]
        element = (self.ri.get_value(key)).split('>')[1]
        return by,element
