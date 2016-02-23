import xlrd
from selenium.webdriver.common.by import By

class DataReader:
    def get_data(file_name):
        try:
            # create an empty list to store rows
            rows = []
            # open the specified Excel spreadsheet as workbook
            book = xlrd.open_workbook(file_name)
            # get the first sheet
            sheet = book.sheet_by_index(0)
            # iterate through the sheet and get data from rows in list
            for row_idx in range(1, sheet.nrows):
                rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
            return rows
        except:
            raise Exception("The file is incorrect")
