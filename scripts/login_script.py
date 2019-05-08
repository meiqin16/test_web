from common.base import open_browser
from page.login_page import LoginPage, login_url


class LoginScript(object):
    def __init__(self,driver):
        """导入浏览器"""
        self.login_page = LoginPage(driver)
        self.login_page.open_url(login_url)

    def login_flow(self,username,password):
        """登录不记住密码"""
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_submit()

    def login_flow_remember(self,username,password):
        """登录记住密码"""
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_remember()
        self.login_page.click_submit()

    def password_question(self):
        """通过密码问题找回密码"""
        self.login_page.click_password_question()

    def password_email(self):
        """通过邮件找回密码"""
        self.login_page.click_email()

    def password_message(self):
        """通过短信验证找回密码"""
        self.login_page.click_message()

    def skip_register(self):
        """跳转到立即注册页面"""
        self.login_page.click_register()

    def skip_home_page(self):
        """跳转到首页"""
        self.login_page.click_home_page()

    def is_login_success(self,username):
        """判断是否登录成功"""
        login_success_loc = ("class name","f4_b")
        result = self.login_page.is_text_in_element(login_success_loc,username)
        return result

if __name__ == '__main__':
    driver = open_browser()
    login = LoginScript(driver)
    login.login_flow_remember("adminq","123456")
    login.is_login_success("adminq")