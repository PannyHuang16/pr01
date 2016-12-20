import function
import os
import time
from selenium import webdriver
import unittest
import HTMLTestRunner
import mail

class Baidu(unittest.TestCase):
    '''百度测试'''
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url="http://www.baidu.com"
    def test_baidu_search(self):
        '''百度查询功能'''
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTML")
        driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))

    #定义报告存放路径
#定义报告存放路径，支持相对路径
    now=function.file_time()
    filename ="E:\\PycharmProjects\\Web_ui\\pr01\\result\\report\\" + now + "_result.html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(
    fp,
    title = u"百度搜索测试报告",
    description = u"用例执行情况")
    runner.run(testunit)
    fp.close()



