import unittest,ddt
from common.base import open_browser,Base
from common.operation_excel import OperationExcel
from scripts.login_script import LoginScript

#准备数据
oper_excel = OperationExcel("./data/test_data.xlsx")
test_data = oper_excel.get_data_info()

@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        """打开浏览器进入登录页面"""
        self.driver = open_browser()
        self.login = LoginScript(self.driver)
        self.base = Base(self.driver)

    @ddt.data(*test_data)
    def test_login(self,data):
        """登录不记住密码"""
        self.login.login_flow(data["username"],data["password"])
        result = self.login.is_login_success(data["username"])
        self.assertEqual(result,data["expect"])

    @ddt.data(*test_data)
    def test_login_remember(self,data):
        """登录记住密码"""
        self.login.login_flow_remember(data["username"],data["password"])
        result = self.login.is_login_success(data["username"])
        self.assertEqual(result,data["expect"])

    def test_password_question(self):
        """通过密码问题找回密码"""
        self.login.password_question()

    def test_password_email(self):
        """通过邮件找回密码"""
        self.login.password_email()

    def test_password_message(self):
        """通过短信验证找回密码"""
        self.login.password_message()

    def test_skip_register(self):
        """跳转到注册页面"""
        self.login.skip_register()

    def test_skip_home_page(self):
        """跳转到首页"""
        self.login.skip_home_page()

    def tearDown(self):
        """关闭浏览器"""
        self.base.close_browser()