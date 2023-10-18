import random

from parts.Part import Part
import math


class Engine(Part):

    def __init__(self, bore, stroke, cylinder, architecture, rev_limit):
        super().__init__(70)
        self.stroke = stroke
        self.bore = bore

        self.volume = round((self.bore / 2) * (self.bore / 2) * math.pi * self.stroke * cylinder)
        self.number_cylinder = cylinder
        self.architecture = architecture

        self.rpm = 0
        self.rev_limit = rev_limit
        self.idle_rpm = round(rev_limit * 0.14)

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
