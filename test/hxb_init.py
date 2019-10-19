from time import sleep

from appium import webdriver

import appium
class TestHxb:
    appPackage = "com.hoomsun.hxb"
    appActivity=".module.welcome.WelcomeActivity"

    def setup_class(self):
        caps={}
        caps["platformName"]="android"
        caps["deviceName"]="aa"
        caps["appPackage"]=self.appPackage
        caps["appActivity"]=self.appActivity
        caps["autoGrantPermissions"]=True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)
        width = self.driver.get_window_size().get('width')
        print(width)
        height = self.driver.get_window_size().get('height')
        print(height)
        sleep(2)
        self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 200)
        sleep(2)
        self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 200)
        sleep(2)
        self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 200)
        self.driver.find_element_by_id('com.hoomsun.hxb:id/ensure').click()
    #每次执行完用例回到首页
    def setup(self):
        pass
    def teardown(self):
        self.driver.start_activity(self.appPackage,self.appActivity)
    def test_login(self):

        # self.driver.find_element_by_xpath('//*[@text="我的"]').click()
        self.driver.find_element_by_xpath('//*[@text="我的"]').click()
        username=self.driver.find_element_by_id('com.hoomsun.hxb:id/login_userName')
        username.clear()
        username.send_keys('13552360596')
        password=self.driver.find_element_by_id('com.hoomsun.hxb:id/login_password')
        password.clear()
        password.send_keys('11111mcp')
        self.driver.find_element_by_id('com.hoomsun.hxb:id/login_button').click()

    def  test_buy(self):
        self.driver.find_element_by_id('com.hoomsun.hxb:id/tab_plan_and_loan').click()
        self.driver.find_element_by_xpath('//*[contains(@resource-id,"state") and @index="0"]').click()
        sleep(5)
        # print(self.driver.page_source)
    def teardown_class(self):
        sleep(5)
        print("aaa")
        self.driver.quit()
