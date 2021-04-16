import os
from tkinter import filedialog

from numpy.random import seed
from numpy.random import randint
import xlsxwriter


class Data:
    data = [[], []]
    # path = r'..\Israel_It\model\Experimental_data.xlsx'
    path = r'C:\Users\User\Documents\שרי\Israel_It\model\Experimental_data.xlsx'

    def save_excel(self, filename):
        import pandas as pd
        df = pd.read_excel(filename)
        print(filename)
        print(df)
        self.data[0] = df['A'].tolist()
        self.data[1] = df['B'].tolist()

    def open_file(self):
        filename = filedialog.askopenfilename(initialdir="r'..\Israel_It\model\Experimental_data.xlsx'", title="select experimental data",
                                              filetypes=[('Excel', ('*.xls', '*.xslm', '*.xlsx'))])
        os.system(filename)
        self.save_excel(filename)

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
