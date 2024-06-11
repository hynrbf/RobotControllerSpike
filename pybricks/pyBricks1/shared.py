from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase, GyroDriveBase


class Speed:
    Slow = float(100)
    Medium = float(250)
    Fast = float(400)


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
            # https://github.com/pybricks/support/issues/989
            Shared.__wheels_with_gyro = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter_in_mm,
                                                  axle_track=axle_track_in_mm)
            Shared.__wheels_with_gyro.use_gyro(True)
            Shared.__wheels_with_gyro.settings(straight_speed=Speed.Medium)
        return Shared.__wheels_with_gyro
