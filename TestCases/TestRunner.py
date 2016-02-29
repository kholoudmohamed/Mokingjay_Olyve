import unittest
from TestCases.HTMLTestRunner import HTMLTestRunner
import os
from TestCases.HomePageTest import HomePageTest

# Get the directory path to output report file
dir = os.getcwd()

# Get all the test cases from HomePageTest file
HomePage_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# Create a test suite
All_tests = unittest.TestSuite([HomePage_tests])

# Open the report file
outfile = open(dir + "\AllTestsReport.html", "w")

# Configure HTMLTestRunner options
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='All Tests')

# run the suite
runner.run(All_tests)


