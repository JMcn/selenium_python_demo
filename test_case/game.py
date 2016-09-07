# coding=utf-8
import unittest
from time import sleep
from common import elements
from common.common import base_url
from common.common import driver_up
from common.common import getimage
from common.action import Game, BeReady
from common import assertion


class TestGame(unittest.TestCase):
    u"""玩游戏"""

    def setUp(self):
        self.driver = driver_up()
        self.url = base_url()
        driver = self.driver
        driver.get(self.url)

    def test_hulu1_check(self):
        u"""检查第 1 个葫芦"""
        driver = self.driver
        num = 1
        action = Game(driver, num)
        action.hulu_check()
        driver.save_screenshot(getimage("hulu1_check"))
        sleep(5)
        try:
            self.assertEquals("display: block;", assertion.hulu_qt(driver, num))
        except AssertionError, msg:
            self.fail(msg)

    def test_hulu1_answer(self):
        u"""第 1 个葫芦,点击答题"""
        driver = self.driver
        num = 1
        action = Game(driver, num)
        action.hulu_answer()
        driver.save_screenshot(getimage("hulu1_answer"))
        try:
            self.assertEquals("display: none;", assertion.hulu_secret(driver, num))
        except AssertionError, msg:
            self.fail(msg)

        try:
            self.assertEquals("display: block;", assertion.hulu_question(driver, num))
        except AssertionError, msg:
            self.fail(msg)

    def test_hulu1_question(self):
        u"""第 1 个葫芦,重看秘密"""
        driver = self.driver
        num = 1
        action = Game(driver, num)
        action.hulu_question()
        driver.save_screenshot(getimage("hulu1_question"))
        try:
            self.assertEquals("display: block;", assertion.hulu_secret(driver, num))
        except AssertionError, msg:
            self.fail(msg)

        try:
            self.assertEquals("display: none;", assertion.hulu_question(driver, num))
        except AssertionError, msg:
            self.fail(msg)

    def test_hulu1_close(self):
        u"""关闭第 1 个葫芦,回到选择葫芦娃"""
        driver = self.driver
        num = 1
        action = Game(driver, num)
        action.hulu_close()
        driver.save_screenshot(getimage("hulu1_close"))
        try:
            self.assertEquals("display: none;", assertion.hulu_qt(driver, num))
        except AssertionError, msg:
            self.fail(msg)

    def test_hulu1_choose(self):
        u"""第 1 个葫芦,选择答案"""
        driver = self.driver
        num = 1
        option = 2
        action = Game(driver, num)
        action.hulu_choose(option)
        driver.save_screenshot(getimage("hulu1_choose"))

    def test_hulu1_submit(self):
        u"""第 1 个葫芦,提交答案,并返回"""
        driver = self.driver
        num = 1
        option = 2
        action = Game(driver, num)
        action.hulu_submit(option)
        driver.save_screenshot(getimage("hulu1_submit"))
        assert_str = "hulu hulu" + str(num) + " cor"
        try:
            self.assertEquals(assert_str, assertion.hulu_choose(driver, num))
        except AssertionError, msg:
            self.fail(msg)

    def test_hulu_submit_all(self):
        u"""完成全部葫芦游戏"""
        driver = self.driver
        action1 = BeReady(driver)
        action1.reject()
        answer = []
        for num in [1, 2, 3, 4, 5, 6]:
            action = Game(driver, num)
            for option in [1, 2, 3]:
                result = action.hulu_goback(option)
                if result == "YES":
                    answer.append(str(num) + ":" + str(option))
                    break
        print answer
        driver.save_screenshot(getimage("hulu_submit_all"))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
