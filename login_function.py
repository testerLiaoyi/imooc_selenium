from selenium import webdriver
from time import sleep
from find_element import FindElement

class LoginFunction():
    """登录功能的类"""

    def __init__(self,url):
        self.driver = self.get_driver(url)

    def get_driver(self,url):
        """获取driver并且打开url"""
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    def get_user_element(self,key):
        """定位用户信息，获取element"""
        find_elemnt = FindElement(self.driver)
        user_elemnt = find_elemnt.get_element(key)
        return user_elemnt

    def send_user_info(self,key,data):
        """输入用户信息"""
        self.get_user_element(key).send_keys(data)

    def main(self):
        """登录实例"""
        self.send_user_info('user_name','dub1')
        self.send_user_info('password','123456')
        self.get_user_element('check_box').click()
        sleep(3)
        self.get_user_element('Login_box').click()
        code_error = self.get_user_element('code_text_error')
        if code_error == None:
            print("登录成功")
        else:
            self.driver.save_screenshot("D:/imooc_selenium/images/test.png")
        sleep(5)
        self.driver.close()

if __name__ == '__main__':
    login_function = LoginFunction("http://118.123.249.212:9011")
    login_function.main()