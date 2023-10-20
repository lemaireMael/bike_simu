from parts import Engine, Frame, Gearbox, Suspension, Wheel
import math


class Bike:

    def __init__(self, tank_capacity, frame_material, time_tracker):
        self.time_tracker = time_tracker

        self.frame = Frame.Frame(frame_material)

        self.engine = Engine.Engine()
        self.gearbox = Gearbox.Gearbox()

        self.tank = Frame.Tank(tank_capacity)

        self.front_suspension = Suspension.Fork()
        self.rear_damper = Suspension.Damper()

        self.front_wheel = Wheel.Wheel()
        self.rear_wheel = Wheel.RearWheel(14)

        self.part_list = [
            self.frame,
            self.engine,
            self.gearbox,
            self.tank,
            self.front_suspension,
            self.rear_damper,
            self.front_wheel,
            self.rear_wheel
        ]

        self.weight = self.get_total_weight()
        self.def_time()
        self.speed = 0

        self._is_started = False

    def get_total_weight(self):
        print(self.part_list)

        weight = sum([part.get_weight for part in self.part_list])
        return weight

    def def_time(self):
        for part in self.part_list:
            part.time_tracker = self.time_tracker

    def brake(self):
        pass

    def turn(self, side):
        pass

    """
    -------------- STARTER ---------------
    """

    @property
    def is_started(self):
        return self._is_started

    @is_started.setter
    def is_started(self, value):
        self._is_started = value

    def start(self):
        print("Bike started")
        self.is_started = True

    """
    -------------- STARTER END ---------------
    """

    """
    -------------- ENGINE ---------------
    """

    def accelerate(self):
        if self.is_started:
            self.engine.rev_up()

    def idle(self):
        if self.is_started:
            self.engine.idle()

    """
    -------------- ENGINE END ---------------
    """

    """
    -------------- TRANSMISSION ---------------
    """

    def shift_up(self):
        if self.gearbox.shift_up():
            self.engine.shift(-3000)

    def shift_down(self):
        if self.gearbox.shift_down():
            self.engine.shift(3000)

    def calculate_linear_speed(self):
        motor_rpm = self.engine.get_rpm
        end_rpm = self.gearbox.get_ratio * self.rear_wheel.get_ratio * motor_rpm

        return end_rpm
        # return (self.rear_wheel.get_radius * 0.02 * math.pi) * end_rpm * 1000 / 216000

    """
    -------------- TRANSMISSION END ---------------
    """
    """
    -------------- "PHYSICS" ---------------
    """
    def get_accel(self, power):
        return power / self.rear_wheel.get_radius

    """
    -------------- PHYSICS END ---------------
    """

    """
    -------------- SECTION ---------------
    """

    """
    -------------- SECTION END ---------------
    """
