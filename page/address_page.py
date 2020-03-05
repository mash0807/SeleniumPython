from page.basepage import BasePage
from selenium.webdriver.support.select import Select
import time

class Address_Page(BasePage):
    #地址管理页面测试
    def __init__(self,driver):
        self.address = BasePage(driver,node='AddressElement')

    def address_add_case(self,firstname,lastname,address,city,country,zone):

        #调用登录后，选择右侧地址管理按钮进入地址管理页面
        self.address.find_element('addressmanage').click()
        time.sleep(2)
        self.address.find_element('newaddress').click()
        time.sleep(2)
        self.address.find_element('firstname').send_keys(firstname)
        self.address.find_element('lastname').send_keys(lastname)
        self.address.find_element('address').send_keys(address)
        self.address.find_element('city').send_keys(city)
        countryElement = self.address.find_element('country')
        selCountry = Select(countryElement)
        selCountry.select_by_visible_text(country)
        zoneElement = self.address.find_element('zone')
        selZone = Select(zoneElement)
        selZone.select_by_visible_text(zone)
        self.address.find_element('addbutton').click()


