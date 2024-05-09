# encoding: utf-8
import csv
import unittest
import time
from selenium import webdriver
import ddt
from selenium.webdriver.common.by import By


def get_csv_data(file_name):
    rows = []
    with open(file_name, "r") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            rows.append(row)
    return rows

@ddt.ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    @ddt.data(*get_csv_data("../resource//123.csv"))
    @ddt.unpack
    def test_data_driven_by_obj(self, name, password):
        url = "https://ceshiren.com/t/topic/30800"
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        try:
            # 点击登录
            self.driver.find_element(By.CSS_SELECTOR, 'button.btn-primary:nth-child(2) > span:nth-child(2)').click()
            time.sleep(2)
            self.driver.find_element(By.ID, "login-account-name").send_keys(name)
            self.driver.find_element(By.ID, "login-account-password").send_keys(password)
            self.driver.find_element(By.CSS_SELECTOR, "#login-button > span:nth-child(2)").click()
            time.sleep(2)
            alert = self.driver.find_element(By.ID, "modal-alert").text
        except Exception as e:
            print(e)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
