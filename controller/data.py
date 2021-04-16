import os
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from openpyxl import load_workbook

from numpy.random import seed
from numpy.random import randint
import xlsxwriter


class Data:
    data = [[], []]
    path = r'C:\Users\User\Documents\שרי\Israel_It\model\Experimental_data.xlsx'

    def save_excel(self):
        import pandas as pd
        df = pd.read_excel(self.path)  # can also index sheet by name or fetch all sheets
        self.data[0] = df['A'].tolist()
        self.data[1] = df['B'].tolist()
        print(self.data)

    def open_file(self):
        filename = filedialog.askopenfilename(initialdir="C:/", title="select file",
                                              filetypes=[('Excel', ('*.xls', '*.xslm', '*.xlsx'))])
        os.system(filename)
        self.save_excel()

    def init_demo(self, n):
        # generate random integer values

        # seed random number generator
        seed(1)
        # generate some integers
        measures = randint(0, 10, n)
        intervals = randint(0, 20, n)

        self.data = [measures, intervals]
        self.write_to_excel()

    def write_to_excel(self):
        with xlsxwriter.Workbook(self.path) as workbook:
            worksheet = workbook.add_worksheet()

            for col_num, data in enumerate(zip(self.data[0], self.data[1])):
                worksheet.write_row(col_num, 0, data)

    def get_data(self):
        return self.data
