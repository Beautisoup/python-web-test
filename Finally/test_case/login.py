import json
import time
import unittest
import ddddocr
import requests
from ddt import data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ddt

# -*- coding: UTF-8 -*-
@ddt.ddt
class TestCSR1(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.driver = None
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.quit()

    @data(["wrong_nam_pas","12345", "12345"], ["wrong_pas","qwert", "12345"], ["right_nam_pas","1339549930@qq.com", "Rr002317"])
    @unpack
    def test_fifth0(self, title, name, password):
        print(name, password)
        url = "https://ceshiren.com/t/topic/30800"
        self.driver.get(url)
        # �����¼
        self.driver.find_element(By.CSS_SELECTOR, 'button.btn-primary:nth-child(2) > span:nth-child(2)').click()
        time.sleep(2)
        self.driver.find_element(By.ID, "login-account-name").send_keys(name)
        self.driver.find_element(By.ID, "login-account-password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button > span:nth-child(2)").click()
        time.sleep(2)
        alert = self.driver.find_element(By.ID, "modal-alert").text
        # ��д����
        if title == "wrong_nam_pas" or title == "wrong_pas":
            #assert alert == '�û����������ʼ������벻��ȷ', 'û�д�����ʾe'
            wait = WebDriverWait(self.driver, 10)
            alert_element = self.driver.find_element(By.ID, "modal-alert")
            self.assertTrue(alert_element.is_displayed(), "modal-alert not found")

        else:
            print(alert)


if __name__ == "__main__":
    # ����һ��TestCSR���ʵ��
    test = TestCSR1()
    # �ֶ�������������ò��Է���
    test.test_fifth0("tt","username", "password")
    unittest.main()
