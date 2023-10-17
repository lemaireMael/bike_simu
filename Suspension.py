from parts.Part import Part


class Suspension(Part):

    def __init__(self, weight: int):
        super().__init__(weight)


class Fork(Suspension):

    def __init__(self):
        super().__init__(7)


class Damper(Suspension):

    def __init__(self):
        super().__init__(4)