from appium import webdriver


class Test_xueqiu:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "mumu"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True
        caps["automationName"] = "uiautomator2"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)
    def test_homepage(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')
        self.driver.find_element_by_id('name').click()
        # self.driver.find_element_by_name('阿里巴巴')
        price=self.driver.find_element_by_xpath('//*[contains(@resource-id,"stockCode") and @text="BABA"]/../../..'
                                          '//*[contains(@resource-id,"current_price")]').text
        assert float(price)>100