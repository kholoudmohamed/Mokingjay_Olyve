import unittest
from TestCases.HTMLTestRunner import HTMLTestRunner
import datetime as dt
import os
from TestCases.HomePageTest import HomePageTest
from TestCases.PlaceOrderTest import PlaceOrderTest

# Get the directory path to output report files
dir = os.getcwd()

# Get all the test cases from HomePageTest file
HomePage_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
PlaceOrder_test = unittest.TestLoader().loadTestsFromTestCase(PlaceOrderTest)

# Create a test suite
All_tests = unittest.TestSuite([HomePage_tests, PlaceOrder_test])

# Open the report file
outfile = open(dir + "\AllTestsReport.html", "w")

# Configure HTMLTestRunner options
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Olyve Tests')

# run the suite
runner.run(All_tests)


