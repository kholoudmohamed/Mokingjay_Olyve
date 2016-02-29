import xlrd
from selenium.webdriver.common.by import By

class DataReader:
    def get_data(self, file_name, row, column):
        try:
            # create an empty list to store rows
            rows = []
            # open the specified Excel spreadsheet as workbook
            book = xlrd.open_workbook(file_name)
            # get the first sheet
            sheet = book.sheet_by_index(0)
            return sheet.cell(row, column)
        except:
            raise Exception("The file is incorrect")
