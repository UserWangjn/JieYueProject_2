import os.path
from .basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from UItest.common.loggen import LogGen
from selenium import webdriver
from time import sleep
logger = LogGen(logger="MainPage").getlog()
#定义主页面中所涉及到的元素，userid及退出按钮，通过xpath方式识别
class MainPage(BasePage):
    userid_loc = (By.XPATH,'.//*[@id=\'top\']/div[3]/ul/li[6]')
    #exit_btn_loc = (By.XPATH,'.//*[@id=\'ECS_MEMBERZONE\']/font/a[2]')
    exit_btn_loc = (By.XPATH, './/*[ @id=\'top\']/div[3]/ul/li[1]/a/span')
    xitongguanli_loc = (By.ID,'firstMenu0')
    yewuzhunbeizhanghu_loc = (By.ID,'firstMenu12')
    #定义打开超链接方法，并将此操作写入日志
    def open(self,base_url):
        self.open(self.base_url,self.pagetitle)
        logger.info("打开连接: %s " % base_url)
    #定义显示userid信息，并将此操作写入日志
    def show_userid(self):
        userid = self.find_element(*self.userid_loc).text
        logger.info("当前用户id是: %s " % userid)
        return userid
    def open_page(self,driver):
        self.find_element(*self.xitongguanli_loc).click()
        print('DEBUG_已经点击了系统管理')
        sleep(3)
        self.find_element(*self.yewuzhunbeizhanghu_loc).click()
        print('DEBUG_已经点击了业务准备账户')
        #driver = webdriver.Chrome()
        sleep(2)
        driver.find_element_by_xpath("//span[text()=' 业务准备账户垫付']").click()
        sleep(3)
        print('DEBUG_已经点击了业务准备账户垫付')
        target = driver.find_element_by_xpath("//*[text()='逾期明细手工垫付']")
        driver.execute_script("arguments[0].scrollIntoView();", target)
        print('DEBUG_移动滚动条到“逾期明细手工垫付”')
        sleep(2)
        driver.find_element_by_xpath("//li[text()='逾期明细手工垫付']").click()
        logger.info('打开“逾期明细手工垫付”页面')

    #定义退出操作，点击退出按钮，并写入日志
    def exit_sys(self):
        self.find_element(*self.exit_btn_loc).click()
        logger.info("注销测试系统")
