import xlrd
from selenium.webdriver.common.by import By


class DataReader:
    @staticmethod
    def get_data(sheet_name, row, column):
        try:
            # Create an empty list to store rows
            rows = []
            # Open the specified Excel spreadsheet as workbook
            book = xlrd.open_workbook("C:\\Users\\Syoussef\\PycharmProjects\\Mokingjay_Olyve\\Olyve.xlsx")
            # Get the appropriate sheet
            sheet = book.sheet_by_name(sheet_name)
            # Return the desired cell value
            return (sheet.cell(row, column)).value
        except:
            raise Exception("The file is incorrect")
