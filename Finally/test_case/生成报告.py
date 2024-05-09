import os
from test import TestCSR
from login import TestCSR1
from Lib import HTMLTestRunner
import unittest


dir = os.getcwd()
outfile = open(dir + "\myreport2.html", "wb+")
alltest = unittest.TestSuite()
loader = unittest.TestLoader()

# alltest.addTests(loader.loadTestsFromTestCase(TestCSR))
# mytest1 = unittest.TestLoader().loadTestsFromTestCase(TestCSR)

alltest.addTests(loader.loadTestsFromTestCase(TestCSR1))
mytest2 = unittest.TestLoader().loadTestsFromTestCase(TestCSR1)

runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title="my test report2",
    description='smoke tests'
)
runner.run(alltest)
outfile.close()