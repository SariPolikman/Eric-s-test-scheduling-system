from controller.queues import Queues
from datetime import datetime, date, timedelta

FIRST = 0

TEST_TIME = 0
WAIT_TIME = 1

PARTICIPANT = 0
INTERVAL = 1

MAX = 0
MIN = 1


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

        self.update_schedule(FIRST, FIRST)
        self.curr_time += timedelta(minutes=int(self.data.data[TEST_TIME][FIRST]))

    def set_details(self, data, K, n, B, C):
        self.data = data
        self.K = K
        self.n = n
        self.B = B
        self.C = C

    def get_next_day(self, data, K, n, B, C):
        # if change details
        self.set_details(data, K, n, B, C)
        self.curr_time = self.B

        # Works only on weekdays
        if self.curr_date.weekday() == 4:
            self.curr_date += timedelta(days=2)

        else:
            self.curr_date += timedelta(days=1)

        date_str = self.curr_date.strftime("%D")
        self.schedule[date_str] = {}

        sum_intervals_today = 0

        # Choosing the longest test at each stage
        self.time_interval, self.participant, self.num_interval = self.queues.get_best_fit(MAX)
        sum_intervals_today += self.get_best_fit(MAX)

        # The next big one doesn’t come in, we put in little ones until the end of the day
        self.time_interval, self.participant, self.num_interval = self.queues.get_best_fit(MIN)
        sum_intervals_today += self.get_best_fit(MIN)

        return sum_intervals_today

    def get_best_fit(self, flag):
        sum_intervals_today = 0
        while self.curr_time + timedelta(minutes=int(self.time_interval)) < self.C:
            sum_intervals_today += 1

            self.time_interval, self.participant, self.num_interval = self.queues.get_best_fit(flag)
            self.update_schedule(self.num_interval, self.participant)
            self.curr_time += timedelta(minutes=int(self.time_interval))
        return sum_intervals_today

    def update_schedule(self, interval, participant):
        date_str = self.curr_date.strftime("%D")
        time_str = self.curr_time.strftime("%H:%M")

        self.schedule[date_str][time_str] = f'participant {participant} interval {interval} '
