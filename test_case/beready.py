# coding=utf-8
import unittest
from common.common import base_url
from common.common import driver_up
from common.common import getimage
from common.action import BeReady
from common import assertion
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class TestBeReady(unittest.TestCase):
    u"""游戏前准备"""

    def setUp(self):
        self.driver = driver_up()
        self.url = base_url()
        driver = self.driver
        driver.get(self.url)

    def test_arrival(self):
        u"""右侧菜单到达"""
        driver = self.driver
        action = BeReady(driver)
        action.arrival()
        try:
            self.assertEquals(u"游戏报名", assertion.sign(driver))
        except AssertionError, msg:
            driver.save_screenshot(getimage("arrival"))
            self.fail(msg)

    def test_start(self):
        u"""游戏开始"""
        driver = self.driver
        action = BeReady(driver)
        action.start()
        driver.save_screenshot(getimage("start"))
        try:
            self.assertEquals("display: block;", assertion.login(driver))
        except AssertionError, msg:
            self.fail(msg)

    def test_reject(self):
        u"""任性拒绝/不登陆进行游戏"""
        driver = self.driver
        action = BeReady(driver)
        action.reject()
        driver.save_screenshot(getimage("reject"))
        try:
            self.assertEquals("display: none;", assertion.login(driver))
        except AssertionError, msg:
            self.fail(msg)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
