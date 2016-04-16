import unittest
import datetime as dt
import sys
sys.path.append("/Mokingjay_Olyve/")
from TestCases.HomePageTest import HomePageTest
from TestCases.PlaceOrderTest import PlaceOrderTest
from Utilities import HTMLTestRunner
from Utilities import FileLocator as FL


# get all test from  HomePageTest and PlaceOrderTest
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
place_order_page_tests = unittest.TestLoader().loadTestsFromTestCase(PlaceOrderTest)

# create a test Suite combining the tests
tests = unittest.TestSuite([home_page_tests, place_order_page_tests])

# Create Test Report Name
report_name = 'TestReport_' + dt.datetime.now().strftime("%Y-%m-%d_%H %M %S")

# Set the test report file location
file_location = FL.get_file_location('TestReports')

# Open the report file
outfile = open(file_location + '\\' + report_name + '.html',
               'x')
# Configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                       title='Test Report',
                                       description='Test Suite Report'
                                       )

# run the suite using HTMLTEstRunner
runner.run(tests)
