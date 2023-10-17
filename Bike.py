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

    def shift_down(self):
        self.gearbox.shift_down()

    def calculate_speed(self):
        end_ratio = self.gearbox.get_ratio
        motor_speed = self.engine.get_rpm
        motor_speed = 1000

        torque = self.get_torque(motor_speed)
        power = self.get_power(motor_speed, torque)

        air_resistance = 0.3
        rolling_resistance = 0.02
        acceleration = 0

        power_watts = power * 745.7  # 1 HP = 745.7 watts

        acceleration_force = self.get_accel(power_watts)

        # Calcul de la force de résistance au roulement
        rolling_force = rolling_resistance * self.weight * 9.81  # F = C * M * g

        # Air resistance
        speed = 0
        time = 0
        delta_t = 0.1

        while speed < 30:  # Limite de vitesse (30 m/s)
            force_air = 0.5 * air_resistance * speed ** 2  # F = 0.5 * C * A * rho * V^2
            total_force = acceleration_force - rolling_force - force_air
            acceleration = total_force / self.weight
            speed += acceleration * delta_t
            time += delta_t


        # return 250 * math.log(temp_speed + 1) / math.log(251)

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
            return 120 - (20 / 1000) * (rpm - 9000)
        else:
            return 0

    def get_power(self, rpm, torque):
        power = (2 * math.pi * torque * rpm) / 60
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
