from parts import Engine, Frame, Gearbox, Suspension, Wheel
import math


class Bike:

    def __init__(self, tank_capacity, frame_material):
        self.frame = Frame.Frame(frame_material)

        self.engine = Engine.Engine()
        self.gearbox = Gearbox.Gearbox()

        self.tank = Frame.Tank(tank_capacity)

        self.front_suspension = Suspension.Fork()
        self.rear_damper = Suspension.Damper()

        self.front_wheel = Wheel.Wheel()
        self.rear_wheel = Wheel.Wheel()

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
        self.speed = 0

        self._is_started = False

    def get_total_weight(self):
        print(self.part_list)

        weight = sum([part.get_weight for part in self.part_list])
        return weight

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
        self.gearbox.shift_up()
        self.engine.shift(-3000)

    def shift_down(self):
        self.gearbox.shift_down()

    def calculate_speed(self, delta_t):
        if (motor_rpm := self.engine.get_rpm) > 1:

            end_ratio = self.gearbox.get_ratio
            rpm_rad_per_s = self.to_rad_s(motor_rpm)

            torque = self.get_torque(motor_rpm)
            power = self.get_power(rpm_rad_per_s, torque)

            force_motrice = power / rpm_rad_per_s

            air_resistance = 0.3
            rolling_resistance = 0.02

            # Calcul de la force de résistance au roulement
            rolling_force = rolling_resistance * self.weight * 9.81  # F = C * M * g

            # Air resistance
            force_air = 0.5 * air_resistance * self.speed ** 2  # F = 0.5 * C * A * rho * V^2

            # F = ma
            # force motrice - force air - force frottement = ma
            acceleration = (force_motrice - force_air - rolling_force) / self.weight
            print(f"{acceleration}, {motor_rpm}")

            """print(f"Actual motor rpm : {motor_rpm}, with gear ratio : {end_ratio}.\n"
                  f"Engine stats :\n"
                  f"Torque : {torque}@{motor_rpm} rpm\n"
                  f"Power : {power/745.7}HP / {power}kW @ {motor_rpm} rpm\n"
                  f"Physics:\n"
                  f"Rolling force: {rolling_force}, Air resistance: {force_air}, acceleration force : {acceleration}\n"
                  f"Speed data:\n"
                  f"Acceleration is {acceleration} and final speed is {self.speed}\n"
                  f"Delta time for calculation : {delta_t}s\n")"""

            return self.speed


        # return 250 * math.log(temp_speed + 1) / math.log(251)

    def calculate_wheel_speed(self, delta_t):
        motor_rpm = self.engine.get_rpm
        motor_rad = self.to_rad_s(motor_rpm)

        torque = self.get_torque(motor_rpm)
        power_w = self.get_power(motor_rad, torque)

        wheel_torque = torque / self.gearbox.get_ratio
        wheel_force = wheel_torque / (self.rear_wheel.get_radius * 0.01)

        # Calcul de la force de résistance au roulement
        rolling_resistance = 0.02
        rolling_force = rolling_resistance * self.weight * 9.81  # F = C * M * g

        # Air resistance
        cx = 0.9
        surface = 0.7
        rho = 1.292
        # force_air = 0.5 * cx * surface * rho * self.speed**2

        acceleration = (wheel_force - rolling_force) / self.weight

        self.speed = self.speed + acceleration * delta_t

        print(motor_rpm)
        # print(self.speed*1000/3600)

    """
    -------------- TRANSMISSION END ---------------
    """
    """
    -------------- "PHYSICS" ---------------
    """
    def get_torque(self, rpm):
        if rpm < 4500:
            return (120 / 4500) * rpm
        elif rpm >= 4500 and rpm <= 9000:
            return 120
        elif rpm > 9000 and rpm <= 10000:
            return 120 # - (20 / 1000) * (rpm - 9000)
        else:
            return 0

    def to_rad_s(self, rpm):
        return (2 * math.pi * rpm) / 60

    def get_power(self, rad, torque):
        power = torque * rad
        return power

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
