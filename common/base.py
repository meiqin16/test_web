from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def open_browser(browser="chrome"):
    """
    打开浏览器
    :param browser:
    :return:
    """
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "ie":
        driver = webdriver.Ie()
    else:
        driver = None
        print("请输入正确的浏览器,例如:Chrome,Firefox,IE")
    return driver

class Base(object):
    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        """
        打开网页
        :param url:
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self,locator,timeout=10):
        """
        定位一个元素
        :param locator:
        :param timeout:
        :return:
        """
        element = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):
        """定位一组元素,返回元素列表"""
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator, timeout=10):
        """
        点击元素
        :param locator: 定位器,是一个元组 ("id","id属性值")
        :param timeout: 最大等待时间
        :return:
        """
        element = self.find_element(locator=locator, timeout=timeout)
        element.click()

    def send_keys(self, locator, text, timeout=10):
        """
        元素输入
        :param locator:
        :param timeout:
        :return:
        """
        element = self.find_element(locator=locator, timeout=timeout)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self, locator, text, timeout=10):
        """
        判断文本是否存在于元素中,相等返回True,不相等返回False
        :param locator: 定位器
        :param text: 判断文本
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout=timeout).until(
                EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, value, timeout=10):
        """
        判断元素的value属性值是否与value是否相等,如果相等返回True,不相等返回False
        :param locator:
        :param value:
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout=timeout).until(
                EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    def sleep_time(self):
        """等待时间"""
        self.driver.implicitly_wait(30)


    def close_browser(self):
        """关闭浏览器"""
        self.driver.quit()

if __name__ == '__main__':
    driver = open_browser()
    base = Base(driver)
    url = "http://www.baidu.com/"
    base.open_url(url)
    time.sleep(3)
    locator_input = ("id", "kw")
    base.send_keys(locator=locator_input, text="测试")
    locator_button = ("id", "su")
    base.click(locator=locator_button)
    time.sleep(4)
    locator_news = ("link text", "新闻")
    text = '新闻'
    result = base.is_text_in_element(locator_news, text)
    print(result)
    base.close_browser()