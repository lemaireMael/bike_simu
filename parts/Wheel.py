from parts.Part import Part


class Wheel(Part):

    def __init__(self, radius: int = 17):
        super().__init__(12)
        self.radius = radius

    @property
    def get_radius(self):
        return self.radius * 2.54 / 2
