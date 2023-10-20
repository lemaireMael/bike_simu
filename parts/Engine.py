import random

from parts.Part import Part
import math


class Engine(Part):

    def __init__(self):
        super().__init__(70)
        self.rpm = 0
        self.idle_rpm = 1000
        self.rev_limit = 10000
        self.rpm_incr = 3000

    @property
    def get_rpm(self):
        return self.rpm

    def calculate_incr(self, stab, rising_coeff, low_coeff, limit):
        if (diff := abs(self.rpm - stab)) > 1 / limit:
            if self.rpm <= limit:
                return self.rpm + rising_coeff * diff
            else:
                return self.rpm - low_coeff * diff
        else:
            return self.rpm

    def rev_up(self):
        self.rpm = self.calculate_incr(self.rev_limit, 0.11, 0.5, 10000)

    def idle(self):
        self.rpm = self.calculate_incr(self.idle_rpm, 0.185, 0.075, 1000)

    def shift(self, rpm):
        self.rpm += rpm
