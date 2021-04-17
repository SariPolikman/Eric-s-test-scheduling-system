from collections import defaultdict

# from main import MAX, MIN, FIRST, TEST_TIME, WAIT_TIME, PARTICIPANT, INTERVAL
FIRST = 0

TEST_TIME = 0
WAIT_TIME = 1

PARTICIPANT = 0
INTERVAL = 1

MAX = 0
MIN = 1


# A flag that keeps whether is now the best choice is minimum or maximum
def dispatch_dict(flag, _dict):
    return {
        MAX: lambda: max(_dict),
        MIN: lambda: min(_dict),
    }.get(flag)()


class Queues:

    def __init__(self, K, n, data):
        self.waiting = defaultdict(list)
        self.ready = defaultdict(list)
        self.doing = []

        self.total_time_over = 0
        self.num_of_interval = n

        self.data = data.data

        a = int(self.data[TEST_TIME][FIRST])
        b = [(i, 0) for i in range(0, K)]
        self.ready[a] = b

    def get_best_fit(self, flag=MAX):

        # if all the relevant tests in waiting state
        if not self.ready:
            self.hole()

        # get nax or min time_interval
        time_interval = dispatch_dict(flag, self.ready)

        participant = self.ready[time_interval][FIRST][PARTICIPANT]
        num_interval = self.ready[time_interval][FIRST][INTERVAL]

        self.update_queues(time_interval, participant, num_interval)

        return time_interval, participant, num_interval

    def hole(self):

        key = min(self.waiting)
        vales = self.waiting[key]

        # update the total that I wait without interval
        self.update_time_over(key - self.total_time_over)

        # moved the smallest wait to ready
        smallest = ((self.data[TEST_TIME][val[INTERVAL]], val) for val in vales)

        # merge dict (update_ready)
        for k, v in smallest:
            self.ready[k].append(v)

        # removed from wait
        self.waiting.pop(key)
        # self.waiting.pop(key)

    # def update_total_time_over(self, time_to_add):

    def update_queues(self, time_interval, participant, num_interval):

        self.update_time_over(time_interval)

        self.update_waiting(time_interval, participant, num_interval)

    def update_time_over(self, time_interval):
        self.total_time_over += time_interval

    def update_waiting(self, time_interval, participant, num_interval):

        # insert the wait if it isn't the last
        if num_interval + 1 < self.num_of_interval:
            self.waiting[self.data[WAIT_TIME][num_interval] + self.total_time_over].append(
                (participant, num_interval + 1))

        # Moving from the waiting to the ready queue
        can_ready = [(key, val) for key, val in self.waiting.items() if key - self.total_time_over <= 0]

        # delete from waiting
        for key, val in can_ready:
            self.waiting.pop(key)

        self.update_ready(time_interval, can_ready)

    def update_ready(self, time_interval, can_ready):
        # delete from ready
        self.doing.append(self.ready[time_interval].pop(FIRST))
        if not self.ready[time_interval]:
            self.ready.pop(time_interval)

        # add to ready
        # merge dict (update_ready)
        for k, values in can_ready:
            for v in values:
                self.ready[self.data[TEST_TIME][v[INTERVAL]]].append(v)
