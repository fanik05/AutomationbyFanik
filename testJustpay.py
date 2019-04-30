import unittest
from appium import webdriver
import time
import os
import HtmlTestRunner


class JustPayTest(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            "automationName": "UiAutomator2",
            "platformName": "Android",
            "platformVersion": "8.0",
            "deviceName": "Galaxy J4",
            "udid": "42002e57ce412557",
            "newCommandTimeout": "500",
            "noReset": "true",
            "app": "C:\\Users\\Fatin Nur\\Desktop\\Staging2.2.0.apk",
            "appPackage": "com.justpaybd.app",
            "appActivity": "com.justpaybd.app.MainActivity",
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        time.sleep(5)

    def test_a_login(self):
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='+880']").send_keys("1716642408")
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='PIN']").send_keys("123123")
        self.driver.find_element_by_xpath("//android.widget.EditText[@bounds='[26,676][694,769]']").click()
        self.driver.execute_script('mobile: performEditorAction', {'action': 'done'})
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='SIGN-IN']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Menu']").click()
        time.sleep(5)

    def test_b_send(self):
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='PIN']").send_keys("123123")
        self.driver.find_element_by_xpath("//android.widget.EditText[@bounds='[26,608][540,702]']").click()
        self.driver.execute_script('mobile: performEditorAction', {'action': 'done'})
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Authorize']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Menu']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@bounds='[129,550][340,630]']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@bounds='[581,268][654,336]']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Jamuna Bank-7260']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='Amount']").send_keys("100")
        self.driver.find_element_by_xpath("//android.widget.EditText[@bounds='[26,502][694,596]']").click()
        self.driver.execute_script('mobile: performEditorAction', {'action': 'done'})
        self.driver.find_element_by_xpath("//android.widget.TextView[@bounds='[581,740][654,808]']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Bebesh Barua']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Now']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='PIN Code']").send_keys("123123")
        self.driver.find_element_by_xpath("//android.widget.EditText[@bounds='[26,576][540,669]']").click()
        self.driver.execute_script('mobile: performEditorAction', {'action': 'done'})
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Authorize']").click()
        time.sleep(5)

    def test_c_request(self):
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='PIN']").send_keys("123123")
        self.driver.find_element_by_xpath("//android.widget.EditText[@bounds='[26,608][540,702]']").click()
        self.driver.execute_script('mobile: performEditorAction', {'action': 'done'})
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Authorize']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Menu']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@bounds='[129,676][340,756]']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.view.ViewGroup[@bounds='[26,248][694,355]']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Jamuna Bank-7260']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='Amount']").send_keys("100")
        self.driver.find_element_by_xpath("//android.widget.EditText[@bounds='[26,502][694,596]']").click()
        self.driver.execute_script('mobile: performEditorAction', {'action': 'done'})
        self.driver.find_element_by_xpath("//android.widget.TextView[@bounds='[581,740][654,808]']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Bebesh Barua']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Request Money']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='PIN Code']").send_keys("123123")
        self.driver.find_element_by_xpath("//android.widget.EditText[@bounds='[26,576][540,669]']").click()
        self.driver.execute_script('mobile: performEditorAction', {'action': 'done'})
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Authorize']").click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\smoke_test.html', report_name='Ver 2.2.0', report_title='SPP V2 Smoke Test Result'))
