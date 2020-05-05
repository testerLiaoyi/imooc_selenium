#_*_ coding: utf-8 _*_
from selenium import webdriver
from time import sleep
from PIL import Image
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#随机生成邮箱用户名
# for i in range(5):
#     user_name = ''.join(random.sample('12345678942344322',10)) + "@qq.com"
#     print(user_name)

#访问被测网址，并验证是否正常打开网址，正确获取用户名元素
driver = webdriver.Chrome()
driver.get("http://118.123.249.212:9011")
sleep(2)
print(EC.title_contains("欢迎访问")(driver))
locator = (By.ID,"u34_input")
element_exists = WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))
print(element_exists)

driver.find_element
#获取登录裁剪后的图片
driver.save_screenshot("E:/imooc.png")
code_element = driver.find_element_by_id("loginBut")
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open("E:/imooc.png")
img = im.crop((left,top,right,height))
img.save("E:/imooc1.png")
#识别图片


#获取用户名输入框文本及输入值做对比
user_element = driver.find_element_by_id("u34_input")
print(user_element.get_attribute("placeholder"))
user_element.send_keys("system")
print(user_element.get_attribute("value"))

#输入密码，点击登录
driver.find_element_by_id("u35_input").send_keys("123456")
driver.find_element_by_id("loginBut").click()

#退出
sleep(3)
driver.quit()