from selenium import webdriver
import time
from selenium.webdriver.common.by import By
'''
使用py自动化的模拟用户操作，控制chrome浏览器，需要driver支持
实例化一个，随后访问，通过find_element指定元素，需导入selenium.webdriver.common.by
用于规定以什么规则查找元素，可像爬虫一样获取当前页面的各类资源，（获取的是当前页面）
不必重复请求
'''
try:
    web = webdriver.Chrome()
    web.get('http://cms15/zb_system/login.php')
    time.sleep(2)
    web.find_element(By.ID,"edtUserName").send_keys('admin')#通过元素id
    web.find_element(By.CSS_SELECTOR,"#edtPassWord").send_keys('mima')#css选择，依旧是id
    time.sleep(2)
    web.find_element(By.XPATH,"//*[@id='btnPost']").click();#通过xpath
    time.sleep(2)
    print("请求成功")
except:
    print("请求失败")
##
if "后台首页" in web.page_source:
    print("登陆成功")
else:
    print("登陆失败")