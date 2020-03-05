from page.basepage import BasePage


class Login_Page(BasePage):
    def __init__(self,driver):
        self.login = BasePage(driver,node='LoginElement')

    def login_case(self,email,password):
        self.login.find_element('email').send_keys(email)
        self.login.find_element('password').send_keys(password)
        self.login.find_element('loginbutton').click()

    def login_err(self,email,password):
        self.login_case(email,password)
        text = self.login.find_element('loginerr').text
        if text is not None:
            return True
        else:
            return False

