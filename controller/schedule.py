from controller.queues import Queues
from datetime import datetime, date, timedelta


class Schedule:
    schedule = {}

    data = [[], []]
    K = 100
    n = 10000
    B = datetime.strptime("08:00", '%H:%M')
    C = datetime.strptime("23:00", '%H:%M')

    curr_time = datetime.strptime("08:00", '%H:%M')
    curr_date = date.today()

    def __init__(self, data, K, n, B, C, _date=date.today()):
        self.curr_date = _date
        date_str = self.curr_date.strftime("%D")
        self.schedule[date_str] = {}

        self.time_interval = 0
        self.participant = 0
        self.num_interval = 0

        self.set_details(data, K, n, B, C)

        self.queues = Queues(K, n, data)

        self.curr_time = self.B

        self.update_schedule(0, 0)
        self.curr_time += timedelta(minutes=int(self.data.data[0][0]))

    def set_details(self, data, K, n, B, C):
        self.data = data
        self.K = K
        self.n = n
        self.B = B
        self.C = C

    def get_next_day(self, data, K, n, B, C):
        self.set_details(data, K, n, B, C)

        self.time_interval, self.participant, self.num_interval = self.queues.get_best_fit(0)
        sum_interval_today = 0

        # Choosing the longest test at each stage
        while self.curr_time + timedelta(minutes=int(self.time_interval)) < self.C:
            sum_interval_today += 1

            self.time_interval, self.participant, self.num_interval = self.queues.get_best_fit(0)
            self.update_schedule(self.num_interval, self.participant)
            self.curr_time += timedelta(minutes=int(self.time_interval))

        self.curr_date += timedelta(days=1)
        date_str = self.curr_date.strftime("%D")
        self.schedule[date_str] = {}

        # The next big one doesn’t come in, we put in little ones until the end of the day
        self.time_interval, self.participant, self.num_interval = self.queues.get_best_fit(1)
        while self.curr_time + timedelta(minutes=int(self.time_interval)) < self.C:

            sum_interval_today += 1

            self.time_interval, self.participant, self.num_interval = self.queues.get_best_fit(1)
            self.update_schedule(self.num_interval, self.participant)
            self.curr_time += timedelta(minutes=int(self.time_interval))

        self.curr_time = self.B
        return sum_interval_today

    def update_schedule(self, interval, participant):
        date_str = self.curr_date.strftime("%D")
        time_str = self.curr_time.strftime("%H:%M")

        self.schedule[date_str][time_str] = f'participant {participant} interval {interval} '
