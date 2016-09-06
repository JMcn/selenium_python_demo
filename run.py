# coding=utf-8
import unittest
import HTMLTestRunner
import time

case_list = 'test_case'


def creatsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_list,
                                                   pattern='*.py',
                                                   top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    print testunit
    return testunit


alltestnames = creatsuite()

now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

filename = 'report/'+now+'-result.html'
fp = file(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'伊可新测试报告',
    description=u'主要是玩游戏,全部用例执行情况:'
)

runner.run(alltestnames)
