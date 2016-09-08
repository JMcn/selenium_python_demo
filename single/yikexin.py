# coding=utf-8
import sys
import os
import time
import unittest
import random
from time import sleep
from selenium import webdriver


class Common:
    # 通用方法
    def __init__(self):
        pass

    @staticmethod
    def driver_up():
        driver = webdriver.PhantomJS(service_args=["--webdriver-loglevel=DEBUG"], service_log_path=sys.argv[1])
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver

    @staticmethod
    def base_url():
        url = "http://act.mama.cn/home/v6/yikexin/index/index"
        return url

    @staticmethod
    def getimage(name):
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        image = os.path.dirname(__file__) + "/" + name + "_" + now + ".png"
        sleep(1)
        print image
        return image


class Elements:
    # 按钮元素
    def __init__(self, driver):
        self.driver = driver

    def sign(self):
        # 游戏报名
        e = self.driver.find_element_by_css_selector(".item2")
        return e

    def start(self):
        # Start!
        e = self.driver.find_element_by_css_selector(".start")
        return e

    def reject(self):
        # 任性拒绝
        e = self.driver.find_element_by_css_selector(".to-reject")
        return e

    def hulu(self, num):
        # 选择葫芦,例如: .hulu.hulu1
        e = self.driver.find_element_by_css_selector(".hulu.hulu" + str(num))
        return e

    def close(self, num):
        # 关闭按钮
        path = '//div[@class="qt"][' + str(num) + ']/div[@class="secret"]/a[@class="close"]'
        e = self.driver.find_element_by_xpath(path)
        return e

    def question(self, num):
        # 重看秘密
        path = '//div[@class="qt"][' + str(num) + ']/div[2]/span'
        e = self.driver.find_element_by_xpath(path)
        return e

    def btn_n(self, num):
        # 点击答题
        path = '//div[@class="qt"][' + str(num) + ']/div[@class="secret"]/div[@class="btn"]'
        e = self.driver.find_element_by_xpath(path)
        return e

    def choose_n(self, num, option):
        # 点击答题
        n = str(option + 1)
        path = '//div[@class="qt"][' + str(num) + ']/div[2]/div[' + n + ']'
        e = self.driver.find_element_by_xpath(path)
        return e

    def submit_n(self, num):
        # 点击答题
        path = '//div[@class="qt"][' + str(num) + ']/div[2]/div[@class="btn"]'
        e = self.driver.find_element_by_xpath(path)
        return e

    def goback(self, num):
        # 返回
        path = '//div[@class="qt"][' + str(num) + ']/div[@class="cpop"]/div[@class="btn"]'
        e = self.driver.find_element_by_xpath(path)
        return e

    def gohome(self, num):
        # 返回
        path = '//div[@class="qt"][' + str(num) + ']//div[@class="wpop"]/div[@class="btn"]'
        e = self.driver.find_element_by_xpath(path)
        return e


class Assertion:
    # 断言元素
    def __init__(self, driver):
        self.driver = driver

    def sign(self):
        # 游戏报名
        e = self.driver.find_element_by_xpath('//div[@class="mod-1"]/div/h2')
        t = e.get_attribute("innerHTML")
        return t

    def login(self):
        # 登陆界面样式
        e = self.driver.find_element_by_css_selector('.mod-game>.login')
        attribute = e.get_attribute("style")
        return attribute

    def hulu_qt(self, num):
        path = '//div[@class="qt"][' + str(num) + ']'
        e = self.driver.find_element_by_xpath(path)
        attribute = e.get_attribute("style")
        return attribute

    def hulu_secret(self, num):
        path = '//div[@class="qt"][' + str(num) + ']/div[@class="secret"]'
        e = self.driver.find_element_by_xpath(path)
        attribute = e.get_attribute("style")
        return attribute

    def hulu_question(self, num):
        path = '//div[@class="qt"][' + str(num) + ']/div[2]'
        e = self.driver.find_element_by_xpath(path)
        attribute = e.get_attribute("style")
        return attribute

    def hulu_choose(self, num):
        path = '//div[@class="choose"]/div[' + str(num) + ']'
        e = self.driver.find_element_by_xpath(path)
        class_name = e.get_attribute("class")
        return class_name

    def all_c(self):
        # 全部答对
        e = self.driver.find_element_by_css_selector(".all-c")
        attribute = e.get_attribute("style")
        return attribute


class BeReady:
    # 游戏前准备
    def __init__(self, driver):
        self.driver = driver
        pass

    def arrival(self):
        Elements(self.driver).sign().click()

    def start(self):
        BeReady(self.driver).arrival()
        Elements(self.driver).start().click()

    def reject(self):
        # 任性拒绝/不登陆进行游戏
        BeReady(self.driver).start()
        Elements(self.driver).reject().click()
        sleep(1)


class Game:
    # 玩游戏
    def __init__(self, driver, num):
        # num = 葫芦编号
        self.driver = driver
        self.num = num
        pass

    def hulu_check(self):
        # 点击葫芦
        action = BeReady(self.driver)
        action.reject()
        Elements(self.driver).hulu(self.num).click()

    def hulu_answer(self):
        # 点击答题
        Game(self.driver, self.num).hulu_check()
        Elements(self.driver).btn_n(self.num).click()

    def hulu_question(self):
        # 重看秘密
        Game(self.driver, self.num).hulu_answer()
        Elements(self.driver).question(self.num).click()

    def hulu_close(self):
        # 关闭葫芦
        Game(self.driver, self.num).hulu_question()
        Elements(self.driver).close(self.num).click()

    def hulu_choose(self, option):
        # 选择答案
        Game(self.driver, self.num).hulu_answer()
        Elements(self.driver).choose_n(self.num, option).click()
        sleep(1)

    def hulu_submit(self, option):
        # 第 ? 个葫芦,提交答案
        Game(self.driver, self.num).hulu_choose(option)
        Elements(self.driver).submit_n(self.num).click()

    def hulu_submit_and_back(self, option):
        # 第 ? 个葫芦,提交答案,并返回
        Game(self.driver, self.num).hulu_submit(option)
        assert_str = "hulu hulu" + str(self.num) + " cor"
        if assert_str == Assertion(self.driver).hulu_choose(self.num):
            Elements(self.driver).goback(self.num).click()
            return "YES"
        else:
            Elements(self.driver).gohome(self.num).click()
            return "NO"

    def hulu_goback(self, option):
        # 根据结果返回主界面
        Elements(self.driver).hulu(self.num).click()
        sleep(1)
        Elements(self.driver).btn_n(self.num).click()
        Elements(self.driver).choose_n(self.num, option).click()
        Elements(self.driver).submit_n(self.num).click()
        assert_str = "hulu hulu" + str(self.num) + " cor"
        if Assertion(self.driver).all_c() == "display: block;":
            return "YES"
        if assert_str == Assertion(self.driver).hulu_choose(self.num):
            Elements(self.driver).goback(self.num).click()
            return "YES"
        else:
            Elements(self.driver).gohome(self.num).click()
            return "NO"


class TestBeReady(unittest.TestCase):
    u"""游戏前准备"""
    def setUp(self):
        self.driver = Common.driver_up()
        self.url = Common.base_url()
        driver = self.driver
        driver.get(self.url)

    def test_arrival(self):
        u"""右侧菜单到达"""
        driver = self.driver
        action = BeReady(driver)
        action.arrival()
        try:
            self.assertEquals(u"游戏报名", Assertion(driver).sign())
        except AssertionError, msg:
            driver.save_screenshot(Common.getimage("arrival"))
            self.fail(msg)

    def test_start(self):
        u"""游戏开始"""
        driver = self.driver
        action = BeReady(driver)
        action.start()
        driver.save_screenshot(Common.getimage("start"))
        try:
            self.assertEquals("display: block;", Assertion(driver).login())
        except AssertionError, msg:
            self.fail(msg)

    def test_reject(self):
        u"""任性拒绝/不登陆进行游戏"""
        driver = self.driver
        action = BeReady(driver)
        action.reject()
        driver.save_screenshot(Common.getimage("reject"))
        try:
            self.assertEquals("display: none;", Assertion(driver).login())
        except AssertionError, msg:
            self.fail(msg)

    def tearDown(self):
        self.driver.quit()


class TestGame(unittest.TestCase):
    u"""玩游戏"""
    def setUp(self):
        self.driver = Common.driver_up()
        self.url = Common.base_url()
        driver = self.driver
        driver.get(self.url)

    def test_hulu_check(self):
        u"""检查第 ? 个葫芦"""
        driver = self.driver
        num = random.randint(1, 6)
        action = Game(driver, num)
        action.hulu_check()
        driver.save_screenshot(Common.getimage("hulu_check"))
        sleep(5)
        try:
            self.assertEquals("display: block;", Assertion(driver).hulu_qt(num))
        except AssertionError, msg:
            self.fail(msg)

    def test_hulu_answer(self):
        u"""第 ? 个葫芦,点击答题"""
        driver = self.driver
        num = random.randint(1, 6)
        action = Game(driver, num)
        action.hulu_answer()
        driver.save_screenshot(Common.getimage("hulu_answer"))
        try:
            self.assertEquals("display: none;", Assertion(driver).hulu_secret(num))
        except AssertionError, msg:
            self.fail(msg)

        try:
            self.assertEquals("display: block;", Assertion(driver).hulu_question(num))
        except AssertionError, msg:
            self.fail(msg)

    def test_hulu_question(self):
        u"""第 ? 个葫芦,重看秘密"""
        driver = self.driver
        num = random.randint(1, 6)
        action = Game(driver, num)
        action.hulu_question()
        driver.save_screenshot(Common.getimage("hulu_question"))
        try:
            self.assertEquals("display: block;", Assertion(driver).hulu_secret(num))
        except AssertionError, msg:
            self.fail(msg)

        try:
            self.assertEquals("display: none;", Assertion(driver).hulu_question(num))
        except AssertionError, msg:
            self.fail(msg)

    def test_hulu_close(self):
        u"""关闭第 ? 个葫芦,回到选择葫芦娃"""
        driver = self.driver
        num = random.randint(1, 6)
        action = Game(driver, num)
        action.hulu_close()
        driver.save_screenshot(Common.getimage("hulu_close"))
        try:
            self.assertEquals("display: none;", Assertion(driver).hulu_qt(num))
        except AssertionError, msg:
            self.fail(msg)

    def test_hulu_choose(self):
        u"""第 1 个葫芦,选择答案"""
        driver = self.driver
        num = random.randint(1, 6)
        option = random.randint(1, 3)
        action = Game(driver, num)
        action.hulu_choose(option)
        driver.save_screenshot(Common.getimage("hulu_choose"))

    def test_hulu_submit(self):
        u"""第 ? 个葫芦,提交答案"""
        driver = self.driver
        num = random.randint(1, 6)
        option = random.randint(1, 3)
        action = Game(driver, num)
        action.hulu_submit(option)
        driver.save_screenshot(Common.getimage("hulu_submit"))
        assert_str = "hulu hulu" + str(num) + " cor"
        try:
            self.assertEquals(assert_str, Assertion(driver).hulu_choose(num))
        except AssertionError:
            pass

    def test_hulu_submit_and_back(self):
        u"""第 ? 个葫芦,提交答案,再返回"""
        driver = self.driver
        num = random.randint(1, 6)
        option = random.randint(1, 3)
        action = Game(driver, num)
        action.hulu_submit_and_back(option)
        driver.save_screenshot(Common.getimage("hulu_submit_and_back"))
        try:
            self.assertEquals("display: none;", Assertion(driver).login())
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
        driver.save_screenshot(Common.getimage("hulu_submit_all"))

    def test_hulu_random_submit(self):
        u"""随机点 ? 个葫芦,提交答案,再返回"""
        driver = self.driver
        action1 = BeReady(driver)
        action1.reject()
        answer = []
        # 总次数
        i = 0
        total = random.randint(1, 10)
        while i < total:
            num = random.randint(1, 6)
            action = Game(driver, num)
            option = random.randint(1, 3)
            result = action.hulu_submit_and_back(option)
            if result == "YES":
                answer.append(str(num) + ":" + str(option) + ":YES")
            else:
                answer.append(str(num) + ":" + str(option) + ":NO")
            i += 1
        print "total:" + str(total)
        print answer
        driver.save_screenshot(Common.getimage("hulu_random_submit"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    u"""
    伊可新脚本

    :Usage:
        传入PhantomJS log 地址
    """

    try:
        sys.argv[1] is None
        case_list = os.path.dirname(__file__)


        def creatsuite():
            testunit = unittest.TestSuite()
            discover = unittest.defaultTestLoader.discover(case_list,
                                                           pattern='*.py',
                                                           top_level_dir=None)
            for test_suite in discover:
                for test_case in test_suite:
                    testunit.addTests(test_case)
            return testunit


        alltestnames = creatsuite()
        print alltestnames
        runner = unittest.TextTestRunner()
        runner.run(alltestnames)
    except IndexError:
        print u"请添加参数: PhantomJS log 路径\n" \
              u"exmaple:\n" \
              u"  python yikexin.py ghostdriver.log"



