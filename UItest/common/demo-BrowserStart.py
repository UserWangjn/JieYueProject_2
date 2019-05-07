from UItest.common.readconfig import *
from selenium import webdriver
from UItest.common.cappic import CapPic
from UItest.common.loggen import LogGen
import time
import os

logger = LogGen(logger='浏览器启动加载').getlog()
def BrowserStart():
    browsername = getbrowsername('browsername')
    url = geturl('url')
    if browsername=='firefox':
        driver = webdriver.Firefox()
        driver.get(url)
    if browsername=='chrome':
        logger.info('启动Chrome浏览器')
        driver = webdriver.Chrome()
        driver.maximize_window()
        time.sleep(2)
        logger.info('打开测试网页')
        driver.get(url)
    CapPic(driver)
BrowserStart()
