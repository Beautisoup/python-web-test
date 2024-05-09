import json
import os
import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

class TestAutoLogin(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_save(self):
        self.driver.get('https://ceshiren.com/t/topic/30800')
        # 人工扫码
        time.sleep(20)
        self.driver.implicitly_wait(10)
        cookies = self.driver.get_cookies()
        self.driver.quit()
        print(cookies)
        with open('../resource/cookies.json', 'w') as f:
            json.dump(cookies, f)

    def test_login(self):
        url = "https://ceshiren.com/t/topic/30800"
        self.driver.get(url)

        with open('../resource/cookies.json', 'r', encoding='utf-8') as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
            print(cookie)

        self.driver.refresh()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
