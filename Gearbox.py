from parts.Part import Part


class Gearbox(Part):

    def __init__(self):
        super().__init__(20)
        self.gear = 1
        self.ratios = {
            1: 3,
            2: 50,
            3: 30,
            4: 15,
            5: 8,
        }
        self.wheel_rpm = 0

    def shift_up(self):
        if self.gear < len(self.ratios):
            self.gear += 1

    def shift_down(self):
        if self.gear > 1:
            self.gear -= 1

    @property
    def get_ratio(self):
        return 1 / self.ratios[self.gear]
