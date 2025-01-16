import bisect

class WeightedIntervalScheduling:
    def __init__(self, events):
        self.events = sorted(events, key=lambda x: x[1]) 
        self.n = len(events)
        self.dp = [0] * self.n
        self.p = self.compute_p()

    def compute_p(self):
        """
        Compute the index of the last non-overlapping interval for each interval.
        """
        start_times = [event[0] for event in self.events]
        p = []
        for i in range(self.n):
            idx = bisect.bisect_right(start_times, self.events[i][0]) - 1
            p.append(idx)
        return p

    def compute_max_revenue(self):
        """
        Dynamic programming to compute the maximum revenue.
        """
        for i in range(self.n):
            include = self.events[i][2]
            if self.p[i] != -1:
                include += self.dp[self.p[i]]
            exclude = self.dp[i - 1] if i > 0 else 0
            self.dp[i] = max(include, exclude)
        return self.dp[-1]

    def find_solution(self):
        """
        Trace back the selected intervals.
        """
        solution = []
        i = self.n - 1
        while i >= 0:
            include = self.events[i][2] + (self.dp[self.p[i]] if self.p[i] != -1 else 0)
            if include >= (self.dp[i - 1] if i > 0 else 0):
                solution.append(self.events[i])
                i = self.p[i]
            else:
                i -= 1
        return solution[::-1] 
