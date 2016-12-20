from selenium import webdriver
from driver import browser
import os
import time
import smtplib  #邮件服务
from email.mime.text import MIMEText #邮件服务

#获取test_case目录的父目录
def base_adr():
    #base_dir=os.path.dirname(os.path.dirname(_file_))
    base_dir=os.path.dirname(os.path.abspath(__file__)) #,os.path.abspath(__file__)
    print(base_dir)
    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')
    print(base_dir)
    base_adr = base_dir.split('/test_case')[0]
    print(base_adr)
    return base_adr
#截图函数

def insert_img(driver,file_name):
    '''
    :param driver: 获取驱动函数
    :param file_name: 文件名，若为空，则去当前时间为文件名
    :return:
    '''
    if file_name=="":
        file_name=file_time()
    base=base_adr()
    file_path = base + "/result/image/" + file_name + '.jpg'
    driver.get_screenshot_as_file(file_path)
    print (file_path)

#获取当前时间 2016_12_13_09_57_29
def file_time():
    file_time=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
    return file_time

#获取最新的测试报告
def new_report():
    #result_dir = "E:\\PycharmProjects\\Web_ui\\pr01\\result\\report"
    base=base_adr()
    print(base)
    result_dir = base + "/result/report"
    print(result_dir)
    lists = os.listdir(result_dir) #获取该目录下的所有文件、文件夹，保存为列表
    #对目录下的文件按创建的时间进行排序
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
    #lists[-1]取到的是最新生成的文件或文件夹
    print(('最新的文件是：' + lists[-1]))
    test_report = os.path.join(result_dir,lists[-1])
#test_report=str(test_report).replace('\r','/')
    print(test_report)
    return test_report

#邮件服务
def send_mail(sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    '''
    :param to_list: 收件人
    :param sub:主题
    :param content: 邮件内容
    :return:
    '''
    #aaa
    to_list=["text97@163.com"]
    mail_host="smtp.163.com"  #设置服务器
    mail_user="text97"    #用户名
    mail_pass="data123"   #口令
    mail_postfix="163.com"  #发件箱的后缀
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,'html','utf-8')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    s = smtplib.SMTP()
    s.connect(mail_host)  #连接smtp服务器
    s.login(mail_user,mail_pass)  #登陆服务器
    s.sendmail(me,to_list, msg.as_string())  #发送邮件
    s.close()
if __name__=="__main__":

#    url1='http://www.baidu.com'
#     dr=browser(url=url1)
#     insert_img(dr,"")
#    new_report()
    send_mail("test","abc")

#dr.quit