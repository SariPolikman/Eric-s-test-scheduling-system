from datetime import timedelta
from tkinter import *

from controller.schedule import Schedule


class Schedule_Day:
    def __init__(self, _input):

        self.input = _input
        self.schedule_day = Tk()
        self.schedule_day.title("Daily to-do list")
        self.schedule_day.geometry("350x700")

        label1 = Label(self.schedule_day, text="TaskBoard for today :")
        label1.pack(side=TOP)

        label1 = Label(self.schedule_day, text="For any change in details,\n please change the details on the home "
                                               "screen")
        label1.pack(fill=BOTH)

        self.data = _input.data
        self.schedule = Schedule(self.data, self.input.K, self.input.n, self.input.B, self.input.C)

        self.curr_interval = 1

        next_day = Button(self.schedule_day, text='NEXT DAY', command=self.the_next_day, bg="gray", fg="purple")
        next_day.pack(side=RIGHT, pady=4, fill=X)

        self.scrollbar = Scrollbar(self.schedule_day, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.my_list = Listbox(self.schedule_day, yscrollcommand=self.scrollbar.set, width=80)

        time_str = (self.schedule.curr_date - timedelta(days=1)).strftime("%D")
        self.label2 = Label(self.schedule_day, text=f"date: {time_str}")

    def the_next_day(self):
        self.my_list.destroy()
        self.label2.destroy()

        if self.curr_interval < self.input.n * self.input.K:
            K, n, B, C = self.input.K, self.input.n, self.input.B, self.input.C

            data = self.data.get_data()

            sum_intervals_today = self.schedule.get_next_day(data, K, n, B, C)

            self.curr_interval += 1

            time_str = self.schedule.curr_date.strftime('%D')
            self.label2 = Label(self.schedule_day, text=f"{self.schedule.curr_date.strftime('%A')}, date: {time_str}")

            self.label2.pack(side=TOP)
            self.my_list = Listbox(self.schedule_day, yscrollcommand=self.scrollbar.set, width=80)
            i = 0

            for key, val in self.schedule.schedule[time_str].items():
                self.my_list.insert(END, key)
                self.my_list.insert(END, val)

                i += 1
            self.my_list.pack(side=LEFT, fill=BOTH, padx=50)
            self.scrollbar.config(command=self.my_list.yview)

            self.curr_interval += sum_intervals_today
