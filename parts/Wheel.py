from parts.Part import Part


class Wheel(Part):

    def __init__(self, radius: int = 17):
        super().__init__(12)
        self.radius = radius

    @property
    def get_radius(self):
        return self.radius * 2.54 / 2


class RearWheel(Wheel):

    def __init__(self, pignon):
        super().__init__()
        self.pignon = pignon
        self.rpm = 0

    @property
    def get_ratio(self):
        return self.pignon
