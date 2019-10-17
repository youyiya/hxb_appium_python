from appium import webdriver
class Setting:
    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "aa"
        caps["appPackage"] = "com.hoomsun.hxb"
        caps["appActivity"] = ".module.welcome.WelcomeActivity"
        caps["autoGrantPermissions"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)
        width = self.driver.get_window_size().get('width')
        print(width)
        height = self.driver.get_window_size().get('height')

