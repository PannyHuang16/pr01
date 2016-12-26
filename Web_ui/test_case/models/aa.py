from function import *
import os
import time
from selenium import webdriver
import smtplib  #邮件服务
from email.mime.text import MIMEText #邮件服务
import unittest
import HTMLTestRunner

#执行测试，并发送邮件
if __name__=="__main__":
    run_test()
    send_mail()