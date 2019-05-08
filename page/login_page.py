from common.base import Base
from common.base import open_browser

login_url = "http://ecshop.itsoso.cn/user.php"
class LoginPage(Base):
    """封装表现层--制作定位器"""
    username_loc = ("name","username")#用户名输入框
    password_loc = ("name","password")#密码输入框
    remember_loc = ("id","remember")#记住密码
    submit_loc = ("name","submit")#立即登录按钮
    password_question_loc = ("link text","密码问题")#找回密码--密码问题链接
    email_loc = ("link text","邮件")#找回密码--邮件链接
    message_loc = ("link text","短信验证")#找回密码--短信验证
    register_loc = ("css selector","div.usTxt>a>img")#立即注册
    home_page_loc = ("link text","首页")#首页链接

    def input_username(self,text):
        """输入用户名"""
        self.send_keys(self.username_loc,text)

    def input_password(self,text):
        """输入密码"""
        self.send_keys(self.password_loc,text)

    def click_submit(self):
        """点击登录"""
        self.click(self.submit_loc)

    def click_remember(self):
        """点击记住密码"""
        self.click(self.remember_loc)

    def click_password_question(self):
        """点击密码问题"""
        self.click(self.password_question_loc)

    def click_email(self):
        """点击邮件"""
        self.click(self.email_loc)

    def click_message(self):
        """点击短信验证"""
        self.click(self.message_loc)

    def click_register(self):
        """点击立即注册"""
        self.click(self.register_loc)

    def click_home_page(self):
        """点击首页链接"""
        self.click(self.home_page_loc)

if __name__ == '__main__':

    driver = open_browser()
    login = LoginPage(driver)
    login.open_url(login_url)
    login.input_username("adminq")
    login.input_password("123456")
    login.close_browser()