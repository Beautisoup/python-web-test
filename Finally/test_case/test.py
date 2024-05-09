import json
import time
import unittest
import ddddocr
import requests
from ddt import data, unpack
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ddt

# 优化：改进强制等待为显示等待，减少等待时间，
# 选择更合适的定位方式
# 优化测试环境，保持更多的内存和CPU资源被使用
# 处理后期不再使用的文件读写方法-图片的资源的获取等
# 消除冗余代码

@ddt.ddt
class TestCSR(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    @classmethod
    def tearDownClass(self):
        print("Tear down...")
        self.driver.quit()

    def setUp(self):
        # 在每个测试用例开始之前都刷新页面，确保测试环境的一致性
        self.driver.get("https://vip.ceshiren.com/#/ui_study/frame")

    def tearDown(self):
        # 每个测试用例执行完成后关闭弹窗，以防止弹窗影响下一个测试用例
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
        except:
            pass

    def test_first(self):
        try:
            self.driver.find_element(By.ID, 'locate').click()
            time.sleep(3)

            self.driver.find_element(By.LINK_TEXT, 'link').click()
            wait = WebDriverWait(self.driver, 10)

            message = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/p')))
            assert message.text == 'link text定位', 'link text定位 does not match expected message'
        except Exception as e:
            print(e)

#键鼠操作（鼠标）
    def test_second(self):
        url = "https://vip.ceshiren.com/#/ui_study/frame"
        self.driver.get(url)

        # 点击【点击两次响应按钮】
        element = self.driver.find_element(By.ID, 'primary_btn')
        element.click()  # 第一次点击
        element.click()  # 第二次点击
        time.sleep(1)

        # 获取弹出框文本，这里应该是记录的点击次数，首次应该是2
        element1 = self.driver.find_element(By.CSS_SELECTOR, '.el-message-box__message > p:nth-child(1)').text
        time.sleep(1)

        # 断言
        assert element1 == '2', 'error'
        time.sleep(1)

        # 点击确定，关闭弹框
        self.driver.find_element(By.CSS_SELECTOR, '.el-button--default').click()
        time.sleep(2)

        # 点击触发弹窗的按钮
        self.driver.find_element(By.ID, 'warning_btn').click()
        time.sleep(1)

        # 等待弹窗出现
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        time.sleep(1)

        # 切换到弹窗上下文
        self.driver.switch_to.alert
        time.sleep(1)

        # 点击确定按钮，处理原生浏览器弹窗
        alert.accept()
        time.sleep(3)

#验证码识别
    def test_third(self):
        url = "https://vip.ceshiren.com/#/ui_study/code"
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.el-input__inner')))
        # 假设验证码识别需要点击获取验证码按钮，并保存验证码图片到本地

        # 这里优化掉保存图片的步骤，

        # 然后使用识别验证码的代码来获取验证码并输入
        code = self.get_verification_code()
        input_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input.el-input__inner[placeholder="请输入验证码"]')))
        input_element.send_keys(code)
        time.sleep(1)

        verify_button = self.driver.find_element(By.CSS_SELECTOR, 'div.code1:nth-child(1) > button:nth-child(3)')
        verify_button.click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.el-message')))
        message = self.driver.find_element(By.CSS_SELECTOR, '.el-message').text
        assert message == '验证成功', '验证码读取失败'

    def get_verification_code(self):
        # 在这里添加识别验证码的代码，返回识别出的验证码
        # 这里使用了示例代码，实际使用时需要根据具体情况进行替换
        with open("../resource/picture.png", 'rb') as f:
            img = f.read()
        p1 = ddddocr.DdddOcr(show_ad=False)
        code = p1.classification(img)
        print('code:', code)
        return code

#键鼠操作（键盘）
    def test_fourth(self):
        url = "https://vip.ceshiren.com/#/ui_study/keypress"
        self.driver.get(url)
        time.sleep(1)
        element1 = self.driver.find_element(By.CSS_SELECTOR, '#press_enter > div:nth-child(1) > input:nth-child(1)')
        element1.send_keys("enter is tapping")
        element1.click()
        time.sleep(2)
        element1.send_keys(Keys.ENTER)
        time.sleep(2)
        alert1 = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,'h1.mb-2'))).text
        assert alert1 == '键盘操作: enter is tapping', '没有enter后的信息'
        print(alert1)
        time.sleep(2)
        element2 = self.driver.find_element(By.CSS_SELECTOR, '#press_delete > div:nth-child(1) > input:nth-child(1)')
        element2.send_keys("delete is tapping")
        element2.click()
        time.sleep(2)
        element2.send_keys(Keys.DELETE)
        time.sleep(2)
        alert2 = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.mb-2'))).text
        assert alert2 == '键盘操作: delete is tapping', '没有delete后的信息'
        print(alert2)
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
