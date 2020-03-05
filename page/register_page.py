from page.basepage import BasePage
#from util.readINI import ReadINI

class Register_Page(BasePage):
    def __init__(self,driver):
        self.rg = BasePage(driver,node='RegisterElement')
        #self.ri = ReadINI(node='ErrInfo')
    def register_case(self,firstname,lastname,email,telephone,password):
        self.rg.find_element('lastname').send_keys(lastname)
        self.rg.find_element('firstname').send_keys(firstname)
        self.rg.find_element('email').send_keys(email)
        self.rg.find_element('telephone').send_keys(telephone)
        self.rg.find_element('password').send_keys(password)
        self.rg.find_element('confirmPassword').send_keys(password)
        self.rg.find_element('checkbox').click()
        self.rg.find_element('sliderButton').click()
        err_text = []
        #如果对应输入框存在错误提示信息，则拼接到err_text中返回
        if self.rg.find_element('firstname_err') is not None:
            err_text.append(['firstname_err', self.rg.find_element('firstname_err').text])
        if self.rg.find_element('lastname_err') is not None:
            err_text.append(['lastname_err', self.rg.find_element('lastname_err').text])
        if self.rg.find_element('email_err') is not None:
            err_text.append(['email_err', self.rg.find_element('email_err').text])
        if self.rg.find_element('phone_err') is not None:
            err_text.append(['phone_err', self.rg.find_element('phone_err').text])
        if self.rg.find_element('password_err') is not None:
            err_text.append(['password_err', self.rg.find_element('password_err').text])
        return err_text

    def register_phone_err(self,firstname,lastname,email,telephone,password):
        self.register_case(firstname,lastname,email,telephone,password)
        #text = self.rg.find_element('phone_err').text
        #if text is not None:
         #   return text
        #else:
         #   return True




