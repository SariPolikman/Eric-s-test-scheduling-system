from tkinter import *

from view.input_window import Input_Window
from view.schedule_day import Schedule_Day


class Welcome:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x400")

        import tkinter as tk
        from PIL import Image, ImageTk
        file = r"C:\Users\User\Documents\שרי\Israel_It\view\images.jpg"
        image = Image.open(file)
        photo_image = ImageTk.PhotoImage(image)
        label = Label(self.root, image=photo_image)
        label.pack()

        label = Label(self.root,
                      text="Welcome \n Eric's test scheduling system", font=('calibre', 15, 'bold'))

        label.pack(side=TOP)

        btn = Button(self.root,
                     text="EDIT DATA",
                     command=self.edit, padx=85, bg="gray", fg="purple")

        btn.pack(side=BOTTOM, pady=8)

        btn = Button(self.root,
                     text="Have an effective task plan for me :)",
                     command=self.start, padx=20, bg="gray", fg="purple")

        btn.pack(side=BOTTOM, pady=8)
        self.new_input = Input_Window()
        self.root.mainloop()

    def edit(self):
        self.new_input.display()

    def start(self):
        self.schedule_day = Schedule_Day(self.new_input)
        self.schedule_day.the_next_day()
