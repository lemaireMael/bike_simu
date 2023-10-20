from parts.Part import Part


class Gearbox(Part):

    def __init__(self):
        super().__init__(20)
        self.gear = 0
        self.ratios = {
            0: 0,
            1: 3.3,
            2: 1.9,
            3: 1.3,
            4: 1,
            5: 0.8,
            6: 0.6
        }
        self.wheel_rpm = 0

    def shift_up(self):
        if self.gear < len(self.ratios) - 1:
            self.gear += 1
            return True
        else:
            return False

    def shift_down(self):
        if self.gear > 1:
            self.gear -= 1
            return True

        else:
            return False

    @property
    def get_ratio(self):
        try:
            return 1 / self.ratios[self.gear]
        except ZeroDivisionError:
            return 0

    @property
    def get_gear(self):
        return self.gear
