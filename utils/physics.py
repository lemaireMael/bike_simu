def get_torque(rpm):
    if rpm < 4500:
        return (120 / 4500) * rpm
    elif 4500 <= rpm <= 9000:
        return 120
    elif 9000 < rpm <= 10000:
        return 120  # - (20 / 1000) * (rpm - 9000)
    else:
        return 0


def to_rad_s(rpm):
    return (2 * math.pi * rpm) / 60


def get_power(rad, torque):
    return torque * rad
