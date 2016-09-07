# coding=utf-8
# 断言元素


def sign(self):
    # 游戏报名
    e = self.find_element_by_xpath('//div[@class="mod-1"]/div/h2')
    t = e.get_attribute("innerHTML")
    return t


def login(self):
    # 登陆界面样式
    e = self.find_element_by_css_selector('.mod-game>.login')
    attribute = e.get_attribute("style")
    return attribute


def hulu_qt(self, num):
    path = '//div[@class="qt"][' + str(num) + ']'
    e = self.find_element_by_xpath(path)
    attribute = e.get_attribute("style")
    return attribute


def hulu_secret(self, num):
    path = '//div[@class="qt"][' + str(num) + ']/div[@class="secret"]'
    e = self.find_element_by_xpath(path)
    attribute = e.get_attribute("style")
    return attribute


def hulu_question(self, num):
    path = '//div[@class="qt"][' + str(num) + ']/div[@class="question"]'
    e = self.find_element_by_xpath(path)
    attribute = e.get_attribute("style")
    return attribute


def hulu_choose(self, num):
    path = '//div[@class="choose"]/div[' + str(num) + ']'
    e = self.find_element_by_xpath(path)
    class_name = e.get_attribute("class")
    return class_name


def all_c(self):
    # 全部答对
    e = self.find_element_by_css_selector(".all-c")
    attribute = e.get_attribute("style")
    return attribute
