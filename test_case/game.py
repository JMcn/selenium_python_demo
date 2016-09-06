# coding=utf-8
import unittest
from time import sleep
from common import elements
from common.common import base_url
from common.common import driver_up
from common.common import getimage
from beready import reject


class Game(unittest.TestCase):
    u"""玩游戏"""

    def setUp(self):
        self.driver = driver_up()
        self.url = base_url()
        driver = self.driver
        driver.get(self.url)

    def test_hulu1_check(self):
        u"""检查第 1 个葫芦"""
        driver = self.driver
        reject(driver)
        elements.hulu(driver, "1").click()
        driver.save_screenshot(getimage("hulu1_check"))

    def test_hulu1_answer(self):
        u"""第 1 个葫芦,点击答题"""
        driver = self.driver
        reject(driver)
        elements.hulu(driver, "1").click()
        elements.btn(driver).click()
        driver.save_screenshot(getimage("hulu1_answer"))

    def test_hulu1_question(self):
        u"""第 1 个葫芦,重看秘密"""
        driver = self.driver
        reject(driver)
        elements.hulu(driver, "1").click()
        elements.btn(driver).click()
        elements.question(driver).click()
        driver.save_screenshot(getimage("hulu1_question"))


    def test_hulu1_close(self):
        u"""关闭第 1 个葫芦,回到选择葫芦娃"""
        driver = self.driver
        reject(driver)
        elements.hulu(driver, "1").click()
        elements.close(driver).click()
        driver.save_screenshot(getimage("hulu1_close"))

    def test_hulu1_choose(self):
        u"""第 1 个葫芦,选择答案"""
        driver = self.driver
        reject(driver)
        elements.hulu(driver, 1).click()
        elements.btn(driver).click()
        elements.choose(driver, 2).click()
        driver.save_screenshot(getimage("hulu1_choose"))

    def test_hulu1_submit(self):
        u"""第 1 个葫芦,提交答案,并返回"""
        driver = self.driver
        reject(driver)
        elements.hulu(driver, 1).click()
        elements.btn(driver).click()
        elements.choose(driver, 2).click()
        elements.submit(driver).click()
        elements.goback(driver).click()
        driver.save_screenshot(getimage("hulu1_submit"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
