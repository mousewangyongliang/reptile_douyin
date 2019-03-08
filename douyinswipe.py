#coding:utf-8

from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Douyin:
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'f175fc80'
        desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'
        desired_caps['appActivity'] = '.main.MainActivity'
        desired_caps['AppWaitActivity'] = '.main.MainActivity'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['noReset'] = 'True'
        desired_caps['autoGrantPermissions']='True'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def scoller(self):
        for i in range(100):
            self.driver.swipe(500, 1500, 500, 200)
            sleep(2)

    def target_click(self):
        """
        适配不同手机屏幕元素位置
        已iPhone6的屏幕作为比较
        x1,y1为编写时手机元素坐标
        :return:
        """

        x_win = self.driver.get_window_size()['width']
        y_win = self.driver.get_window_size()['height']
        x_scale = 0.8842592592592593  # x轴的比例
        y_scale = 0.041666666666666664  # y轴的比例
        x = x_win*x_scale
        y = y_win*y_scale
        return x, y



    def jump_banner(self):
        coo = self.target_click()
        print(coo)
        self.driver.tap([(coo)], 500)
        # banner_path = '//android.widget.TextView[@resource-id="com.ss.android.ugc.aweme:id/aze"]'
        # WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, banner_path)))


    def check_update(self):
        """
        检测抖音更新，如果出现更新，点击以后再说
        :return:
        """
        update_last_path = '//android.widget.TextView[@resource-id="com.ss.android.ugc.aweme:id/b3z"]'
        WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, update_last_path))).click()

    def main(self):
        self.jump_banner()
        sleep(5)
        self.scoller()

if __name__ == '__main__':
    douyin = Douyin()
    douyin.main()