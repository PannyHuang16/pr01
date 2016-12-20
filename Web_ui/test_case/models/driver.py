from selenium.webdriver import Remote
from selenium import webdriver
#启动浏览器驱动

def browser(url):
    driver=webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get(url)
#    driver.quit()
    return driver

#     host='www.shengcaijinrong.com' #运行主机：端口号 （本机默认：127.0.0.1:4444)
#     dc={'browserName':'firefox'} #指定浏览器（‘chrome’，‘firefox’）
#     driver=Remote(command_executor= host,
#                   desired_capabilities=dc)

if __name__=="__main__":
    url1='http://www.baidu.com'
    browser(url=url1)
