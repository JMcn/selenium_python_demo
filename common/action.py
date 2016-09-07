# coding=utf-8
# 页面动作
from time import sleep
import elements
import assertion


class BeReady:
    # 公共方法
    def __init__(self, driver):
        self.driver = driver
        pass

    def arrival(self):
        elements.sign(self.driver).click()

    def start(self):
        BeReady.arrival(self)
        elements.start(self.driver).click()

    def reject(self):
        # 任性拒绝/不登陆进行游戏
        BeReady.start(self)
        elements.reject(self.driver).click()
        sleep(1)


class Game:
    # 公共方法
    def __init__(self, driver, num):
        # num = 葫芦编号
        self.driver = driver
        self.num = num
        pass

    def hulu_check(self):
        # 点击葫芦
        action = BeReady(self.driver)
        action.reject()
        elements.hulu(self.driver, self.num).click()

    def hulu_answer(self):
        # 点击答题
        Game.hulu_check(self)
        elements.btn(self.driver).click()


    def hulu_question(self):
        # 重看秘密
        Game.hulu_answer(self)
        elements.question(self.driver).click()

    def hulu_close(self):
        # 关闭葫芦
        Game.hulu_question(self)
        elements.close(self.driver).click()

    def hulu_choose(self, option):
        # 选择答案
        Game.hulu_answer(self)
        elements.choose(self.driver, option).click()
        sleep(1)

    def hulu_submit(self, option):
        # 第 1 个葫芦,提交答案,并返回
        Game.hulu_choose(self, option)
        elements.submit(self.driver).click()

    def hulu_goback(self, option):
        # 根据结果返回主界面
        elements.hulu(self.driver, self.num).click()
        sleep(1)
        elements.btn_n(self.driver, self.num).click()
        elements.choose_n(self.driver, self.num, option).click()
        elements.submit_n(self.driver, self.num).click()
        assert_str = "hulu hulu" + str(self.num) + " cor"
        print assert_str
        if assertion.all_c(self.driver) == "display: block;":
            return "YES"
        if assert_str == assertion.hulu_choose(self.driver, self.num):
            elements.goback(self.driver, self.num).click()
            return "YES"
        else:
            elements.gohome(self.driver, self.num).click()
            return "NO"
