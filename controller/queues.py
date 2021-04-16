from collections import defaultdict


class Queues:
    was_hole = 0

    def __init__(self, K, n, data):
        self.waiting = defaultdict(list)
        self.ready = defaultdict(list)
        self.doing = []

        self.total_time_over = 0
        self.num_of_interval = n

        self.data = data.data

        a = int(self.data[0][0])
        b = [(i, 0) for i in range(0, K)]
        self.ready[a] = b

    def get_best_fit(self):

        if not self.ready:
            self.hole()

        time_interval = min(self.ready)

        participant, num_interval = self.ready[time_interval][0][0], self.ready[time_interval][0][1]

        self.update_queues(time_interval, participant, num_interval)

        return time_interval, participant, num_interval

    def hole(self):
        self.was_hole += 1

        key = min(self.waiting)
        vales = self.waiting[key]

        # update the total that I wait without interval
        self.update_time_over(key - self.total_time_over)

        # moved the smallest wait to ready

        a = ((self.data[0][val[1]], val) for val in vales)

        # merge dict (update_ready)
        for k, v in a:
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
            self.waiting[self.data[1][num_interval] + self.total_time_over].append(
                (participant, num_interval + 1))

        # Moving from the waiting to the ready queue
        can_ready = [(key, val) for key, val in self.waiting.items() if key - self.total_time_over <= 0]

        # delete from waiting
        for key, val in can_ready:
            self.waiting.pop(key)

        self.update_ready(time_interval, can_ready)

    def update_ready(self, time_interval, can_ready):
        # delete from ready
        self.doing.append(self.ready[time_interval].pop(0))
        if not self.ready[time_interval]:
            self.ready.pop(time_interval)

        # add to ready
        # merge dict (update_ready)
        for k, values in can_ready:
            for v in values:
                self.ready[self.data[0][v[1]]].append(v)
