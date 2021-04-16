import tkinter as tk

from tkinter import *
from tkinter.ttk import *

from controller.data import Data

from datetime import datetime


class Input_Window:
    root = None

    K_var = 8
    n_var = 0
    B_var = 0
    C_var = 0

    def __init__(self):
        self.K = 100
        self.n = 10000
        self.B = datetime.strptime("08:00", '%H:%M')
        self.C = datetime.strptime("23:00", '%H:%M')

        self.data = Data()
        self.data.init_demo(self.n)

    def display(self):
        self.root = Toplevel()

        self.K_var = tk.IntVar()
        self.n_var = tk.IntVar()
        self.B_var = tk.StringVar()
        self.C_var = tk.StringVar()

        self.K_var.set(100)
        self.n_var.set(1000)
        self.B_var.set("08:00")
        self.C_var.set("23:00")

        self.set_input()

    def submit_k(self):
        self.K = self.K_var.get()

    def submit_n(self):
        self.n = self.n_var.get()

    def submit_B(self):
        self.B = datetime.strptime(self.B_var.get(), "%H:%M")

    def submit_C(self):
        self.C = datetime.strptime(self.C_var.get(), "%H:%M")

    def close(self):
        self.root.destroy()

    def set_input(self):
        self.root.geometry("600x200")

        label = Label(self.root,
                      text="Please enter the data before we begin, \nsave the desired fields and finish closed")

        label.grid(row=0, column=0)

        K_label = tk.Label(self.root, text='Number of trial participants', font=('calibre', 10, 'bold'), justify=LEFT)
        K_entry = tk.Entry(self.root, textvariable=self.K_var, font=('calibre', 10, 'normal'))
        btn_K = Button(self.root, text="submit", command=self.submit_k)

        n_label = tk.Label(self.root, text='Number of measurements per participant', font=('calibre', 10, 'bold'))
        n_entry = tk.Entry(self.root, textvariable=self.n_var, font=('calibre', 10, 'normal'))
        btn_n = Button(self.root, text="submit", command=self.submit_n)

        B_label = tk.Label(self.root, text='Beginning time', font=('calibre', 10, 'bold'))
        B_entry = tk.Entry(self.root, textvariable=self.B_var, font=('calibre', 10, 'normal'))
        btn_B = Button(self.root, text="submit", command=self.submit_B)

        C_label = tk.Label(self.root, text='End time', font=('calibre', 10, 'bold'))
        C_entry = tk.Entry(self.root, textvariable=self.C_var, font=('calibre', 10, 'normal'))
        btn_C = Button(self.root, text="submit", command=self.submit_C)

        data_label = tk.Label(self.root, text='Edit the experiment data', font=('calibre', 10, 'bold'))
        data_btn = Button(self.root, text='Open', command=self.data.open_file)

        # placing the label and entry in
        # the required position using grid
        # method
        K_label.grid(row=1, column=0, sticky=W)
        K_entry.grid(row=1, column=1)
        btn_K.grid(row=1, column=3)

        n_label.grid(row=2, column=0, sticky=W)
        n_entry.grid(row=2, column=1)
        btn_n.grid(row=2, column=3)

        B_label.grid(row=3, column=0, sticky=W)
        B_entry.grid(row=3, column=1)
        btn_B.grid(row=3, column=3)

        C_label.grid(row=4, column=0, sticky=W)
        C_entry.grid(row=4, column=1)
        btn_C.grid(row=4, column=3)

        data_label.grid(row=5, column=0, sticky=W)
        data_btn.grid(row=5, column=1)

        close = Button(self.root, text="close", command=self.close)
        close.grid(row=7, column=4)
