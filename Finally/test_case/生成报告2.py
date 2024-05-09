import os
import unittest
from login import TestCSR1
from Lib import HTMLTestRunner
# -*- coding: UTF-8 -*-

dir = os.getcwd()
outfile = open(dir + "\myreport2.html", "wb+", encoding='utf-8')  # 指定编码方式为 UTF-8
alltest = unittest.TestSuite()
loader = unittest.TestLoader()

alltest.addTests(loader.loadTestsFromTestCase(TestCSR1))
mytest2 = unittest.TestLoader().loadTestsFromTestCase(TestCSR1)

runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title="my test report2",
    description='smoke tests'
)
runner.run(alltest)
outfile.close()
