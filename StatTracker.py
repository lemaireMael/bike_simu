class StatTracker:

    def __init__(self):
        self.speed = 0
        self.accel = 0

        self.turning_angle = 0
        self.angle = 0

        self.actual_gear = 0

        self.brake_pressure = 0
        self.brake_temperature = 0

        self.engine_temperature = 0
        self.engine_rev = 0