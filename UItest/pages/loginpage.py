from selenium import webdriver
from UItest.pages.basepage import BasePage
from selenium.webdriver.common.by import By
from UItest.common.loggen import LogGen
from UItest.common.geturl import GetUrl
logger = LogGen(logger="LoginPage").getlog()
#创建登录操作类，页面中的元素通过name方式识别
class LoginPage(BasePage):
    #设置登录操作中所用到的三个元素属性，并以元组形式保存
    username = (By.NAME,'username')
    password = (By.ID,'pwd')
    submit = (By.XPATH,".//*[@id='loginForm']/ul/li[3]/div/input")
    #定义用户名元素识别及输入函数，并将此操作写入日志
    def input_username(self,username):
        self.find_element(*self.username).send_keys(username)
        logger.info("输入用户名：%s" % username)
    #定义密码元素识别及输入函数，并将此操作写入日志
    def input_password(self,password):
        self.find_element(*self.password).send_keys(password)
        logger.info("输入密码：%s" % password)
    #定义提交按钮元素识别及输入函数，并将此操作写入日志
    def click_submit(self):
        self.find_element(*self.submit).click()
        logger.info("点击登录按钮")