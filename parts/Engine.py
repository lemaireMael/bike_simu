import random

from parts.Part import Part
import math


class Engine(Part):

    def __init__(self):
        super().__init__(70)
        self.rpm = 0
        self.idle_rpm = 1000
        self.rev_limit = 10000

    @property
    def get_rpm(self):
        return self.rpm

    def rev_up(self):
        if self.rpm < self.rev_limit - 15:
            inc = 1 + round(math.exp(self.rpm / 1000))
            self.rpm += 15

    def idle(self):
        if self.rpm <= self.idle_rpm:
            self.rev_up()
        else:
            self.rpm -= random.randrange(20)

    def shift(self, rpm):
        self.rpm += rpm
