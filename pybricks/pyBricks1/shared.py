from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase


class Speed:
    Slow = float(100)
    Medium = float(200)
    Fast = float(400)


# inspiration https://github.com/FLL-Team-24277/FLL-Fall-2023-Masterpiece/blob/main/samples/base_robot.py
class Shared:
    __hub = PrimeHub()
    __wheels_with_gyro = None

    @staticmethod
    def hub() -> PrimeHub:
        return Shared.__hub

    @staticmethod
    def wheels_with_gyro(left_motor: Motor, right_motor: Motor, wheel_diameter_in_mm: float,
                         axle_track_in_mm: float) -> DriveBase:
        if Shared.__wheels_with_gyro is None:
            # using gyro, https://github.com/pybricks/support/issues/989
            # changes in code https://github.com/pybricks/pybricks-code/blob/19a809b6df06da252d0ddf100a49f2e474b6d7d4/CHANGELOG.md?plain=1#L60
            Shared.__wheels_with_gyro = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter_in_mm,
                                                  axle_track=axle_track_in_mm)
            Shared.__wheels_with_gyro.use_gyro(True)
            Shared.__wheels_with_gyro.settings(straight_speed=Speed.Fast, straight_acceleration=None, turn_rate=360,
                                               turn_acceleration=None)
            return Shared.__wheels_with_gyro

        Shared.__wheels_with_gyro.settings(straight_speed=Speed.Fast, straight_acceleration=None, turn_rate=360,
                                           turn_acceleration=None)
        return Shared.__wheels_with_gyro
