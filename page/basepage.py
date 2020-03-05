from util.readINI import ReadINI

class BasePage(object):
    def __init__(self,driver,node):
        self.driver = driver
        #初始化传入对应的ini中的节点值，查找对应页面元素信息
        self.ri = ReadINI(node=node)

    def find_element(self,key):
        by = (self.ri.get_value(key)).split('>')[0]
        element = (self.ri.get_value(key)).split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(element)
            elif by == 'name':
                return self.driver.find_element_by_name(element)
            elif by == 'classname':
                return self.driver.find_element_by_class_name(element)
            elif by == 'tagname':
                return self.driver.find_element_by_tag_name(element)
            elif by == 'linktext':
                return self.driver.find_element_by_link_text(element)
            elif by == 'palinktext':
                return self.driver.find_element_by_partial_link_text(element)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(element)
            else:
                return self.driver.find_element_by_css_selector(element)
        except:
            return None