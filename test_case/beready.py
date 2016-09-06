# coding=utf-8
import unittest
from time import sleep
from common import elements
from common.common import base_url
from common.common import driver_up
from common.common import getimage


class BeReady(unittest.TestCase):
    u"""游戏前准备"""

    def setUp(self):
        self.driver = driver_up()
        self.url = base_url()
        driver = self.driver
        driver.get(self.url)

    def test_arrival(self):
        u"""右侧菜单到达"""
        driver = self.driver
        elements.sign(driver).click()

    def test_start(self):
        u"""游戏开始"""
        driver = self.driver
        elements.start(driver).click()
        driver.save_screenshot(getimage("start"))

    def test_reject(self):
        u"""任性拒绝/不登陆进行游戏"""
        driver = self.driver
        elements.start(driver).click()
        elements.reject(driver).click()
        driver.save_screenshot(getimage("reject"))

    def tearDown(self):
        self.driver.quit()


# 任性拒绝/不登陆进行游戏 公共方法
def reject(self):
    elements.start(self).click()
    elements.reject(self).click()
    sleep(1)

if __name__ == "__main__":
    unittest.main()
