from parts.Bike import Bike

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
        self.bike = Bike(15, "steel")

        self.shift_up_flag = False
        self.shift_down_flag = False

    def accelerate(self):
        self.bike.accelerate()

    def idle(self):
        self.bike.idle()

    def shift_up(self):
        self.bike.shift_up()

    def shift_down(self):
        self.bike.shift_down()

    def handle_actions(self, pressed_keys):

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

        print(self.bike.calculate_speed())

