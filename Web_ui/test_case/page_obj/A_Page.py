from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base import Page
from time import sleep

class login(Page):
    '''
    用户登录页面
    '''
    url='/'

    #Action
    bbs_login_user_loc=(By.XPATH,"/html/body/div[1]/ng-include/div[1]/div/div[1]/div[1]/span[1]/a[1]")
    bbs_login_button_loc=(By.ID,"mzLogin")

    def bbs_login(self):
        self.find_element(*self.bbs_login_user_loc).click()

    login_username_loc=(By.NAME,"mobile")
    login_password_loc=(By.NAME,"password")
    login_button_loc=(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/form/div[4]/button")

    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)
    #登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)
    #登录按钮
    def login_button(self):
        self.find_elemnt(*self.login_button_loc).click()
    #定义统一登录入口
    def user_login(self,url,username,password):
        """ 获取的用户名密码登录"""
        self.open(url)
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    if __name__=="__main__":
        url1="https://www.shengcaijinrong.com/#/home"

        user_login(self,url=url1,username="13681946855",password="25%aaa")
