from parts.Bike import Bike
from utils.StatTracker import StatTracker
from utils.TimeTracker import TimeTracker
import time

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_s,
    K_c,
    K_v,
    KEYDOWN,
    QUIT,
)


class Manager:

    def __init__(self):
        self.time_tracker = TimeTracker()
        self.bike = Bike(15, "steel", self.time_tracker)

        self.shift_up_flag = False
        self.shift_down_flag = False

        self.stat_tracker = StatTracker()

        self.current_time = time.time()
        self.previous_time = time.time()

    def accelerate(self):
        self.bike.accelerate()

    def idle(self):
        self.bike.idle()

    def shift_up(self):
        self.bike.shift_up()

    def shift_down(self):
        self.bike.shift_down()

    def handle_actions(self, pressed_keys) -> StatTracker:
        self.time_tracker.set_time()
        delta_t = self.time_tracker.get_time

        if delta_t > 0.05:

            if pressed_keys[K_UP]:
                self.accelerate()
            else:
                self.idle()

            if pressed_keys[K_DOWN]:
                self.brake()

            if pressed_keys[K_RIGHT]:
                self.turn("RIGHT")

            if pressed_keys[K_LEFT]:
                self.turn("LEFT")

            if pressed_keys[K_c] and not self.shift_down_flag:
                self.shift_down()
                self.shift_down_flag = True

            elif not pressed_keys[K_c]:
                self.shift_down_flag = False

            if pressed_keys[K_v] and not self.shift_up_flag:
                self.shift_up()
                self.shift_up_flag = True

            elif not pressed_keys[K_v]:
                self.shift_up_flag = False

            if pressed_keys[K_s] and not self.bike.is_started:
                self.bike.start()

            speed_kph = self.bike.calculate_linear_speed()

            self.stat_tracker.log_data(self.bike.engine.get_rpm)
            self.stat_tracker.log_time(delta_t)

            self.time_tracker.reset()

        return self.stat_tracker
        # time.sleep(0.2)

