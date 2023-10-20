import numpy as np


class StatTracker:

    def __init__(self):
        self.time = np.zeros(101)
        self.speed = 0
        self.accel = 0

        self.turning_angle = 0
        self.angle = 0

        self.actual_gear = 0

        self.brake_pressure = 0
        self.brake_temperature = 0

        self.engine_temperature = 0
        self.engine_rev = np.zeros(101)

    @property
    def times(self):
        return self.time[-100:]

    def log_time(self, delta):
        last_time = self.time[-1]
        self.time = np.append(self.time, last_time + delta)

    @property
    def data(self):
        return self.engine_rev[-100:]

    def log_data(self, data):
        self.engine_rev = np.append(self.engine_rev, data)

