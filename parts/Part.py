class Part:

    def __init__(self, weight: int):
        self.weight = weight
        self.time_tracker = None

    @property
    def get_weight(self):
        return self.weight

    @property
    def time(self):
        return self.time_tracker.get_time
