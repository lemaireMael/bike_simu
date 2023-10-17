from parts.Part import Part


class Tank(Part):

    def __init__(self, capacity: int):
        self.capacity = capacity
        super().__init__(capacity+5)


class Frame(Part):

    def __init__(self, material: str):
        self.material = material
        self.stiffness = None

        super().__init__(20 if self.material == "steel" else 15)