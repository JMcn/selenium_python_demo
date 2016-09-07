# coding=utf-8
import time
from time import sleep
from selenium import webdriver
from find_dir import report_dir


def driver_up():
    driver = webdriver.PhantomJS()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def base_url():
    url = "http://act.mama.cn/home/v6/yikexin/index/index"
    return url


def getimage(name):
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = report_dir()
    image = report_path + name + "_" + now + ".png"
    sleep(1)
    print image
    return image
