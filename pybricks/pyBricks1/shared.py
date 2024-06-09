from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase


class Shared:
    __hub = PrimeHub()
    __wheels_with_gyro = None

    @staticmethod
    def hub() -> PrimeHub:
        return Shared.__hub

    @staticmethod
    def get_wheels_with_gyro(left_motor: Motor, right_motor: Motor, wheel_diameter_in_mm,
                             axle_track_in_mm) -> DriveBase:
        if Shared.__wheels_with_gyro is None:
            Shared.__wheels_with_gyro = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter_in_mm,
                                                  axle_track=axle_track_in_mm)
            Shared.__wheels_with_gyro.use_gyro(True)

        return Shared.__wheels_with_gyro
