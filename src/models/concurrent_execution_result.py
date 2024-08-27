class ConcurrentExecutionResult:
    def __init__(self, results, total_requests, error_requests, durations, total_time):
        self.results = results
        self.total_requests = total_requests
        self.error_requests = error_requests
        self.durations = durations
        self.total_time = total_time

    def average_time(self):
        return sum(self.durations) / self.total_requests if self.total_requests > 0 else 0

    def max_time(self):
        return max(self.durations) if self.durations else 0

    def p90_time(self):
        return sorted(self.durations)[int(0.9 * len(self.durations))] if self.durations else 0

    def error_rate(self):
        return self.error_requests / self.total_requests * 100 if self.total_requests > 0 else 0

    def to_dict(self):
        return {
            "total_requests": self.total_requests,
            "error_requests": self.error_requests,
            "average_time": self.average_time(),
            "max_time": self.max_time(),
            "p90_time": self.p90_time(),
            "error_rate": self.error_rate(),
            "results": self.results,
        }
