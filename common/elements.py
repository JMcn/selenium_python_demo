# coding=utf-8
# 按钮元素


def sign(self):
    # 游戏报名
    e = self.find_element_by_css_selector(".item2")
    return e


def start(self):
    # Start!
    e = self.find_element_by_css_selector(".start")
    return e


def reject(self):
    # 任性拒绝
    e = self.find_element_by_css_selector(".to-reject")
    return e


def hulu(self, num):
    # 选择葫芦,例如: .hulu.hulu1
    e = self.find_element_by_css_selector(".hulu.hulu" + str(num))
    return e


def close(self):
    # 关闭按钮
    e = self.find_element_by_css_selector(".close")
    return e


def btn(self):
    # 点击答题、提交、返回
    e = self.find_element_by_css_selector(".btn")
    return e


def question(self):
    # 重看秘密
    e = self.find_element_by_css_selector(".question>span")
    return e


def choose(self, option):
    # 选择答案
    n = str(option+1)
    choose_path = '//div[@class="question"]/div[' + n + ']'
    e = self.find_element_by_xpath(choose_path)
    return e


def submit(self):
    # 提交答案
    e = self.find_element_by_xpath('//div[@class="question"]/div[@class="btn"]')
    return e


def btn_n(self, num):
    # 点击答题
    path = '//div[@class="qt"][' + str(num) + ']/div[@class="secret"]/div[@class="btn"]'
    e = self.find_element_by_xpath(path)
    return e


def choose_n(self, num, option):
    # 点击答题
    n = str(option + 1)
    path = '//div[@class="qt"][' + str(num) + ']/div[2]/div[' + n + ']'
    e = self.find_element_by_xpath(path)
    return e


def submit_n(self, num):
    # 点击答题
    path = '//div[@class="qt"][' + str(num) + ']/div[2]/div[@class="btn"]'
    e = self.find_element_by_xpath(path)
    return e


def goback(self, num):
    # 返回
    path='//div[@class="qt"][' + str(num) + ']/div[@class="cpop"]/div[@class="btn"]'
    e = self.find_element_by_xpath(path)
    return e


def gohome(self, num):
    # 返回
    path = '//div[@class="qt"][' + str(num) + ']//div[@class="wpop"]/div[@class="btn"]'
    e = self.find_element_by_xpath(path)
    return e
