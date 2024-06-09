from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
from pybricks.pupdevices import ForceSensor

from shared import Shared, Speed


class WheelController:
    # I measured manually and the wheel diameter is 5.6cm and the axle distance is 11.7cm
    __wheel_diameter_in_mm = float(56)
    __axle_track_in_mm = float(117)

    __left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
    __right_motor = Motor(Port.F)
    __button = ForceSensor(Port.A)

    @staticmethod
    def move_wheels_forward_in_straight_line(distance_in_mm: float, speed: float = Speed.Medium):
        wheel_controller = Shared.get_wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                                       WheelController.__wheel_diameter_in_mm,
                                                       WheelController.__axle_track_in_mm)
        wheel_controller.settings(straight_speed=speed)
        wheel_controller.straight(distance_in_mm)

    @staticmethod
    def move_wheels_backward_in_straight_line(distance_in_mm: float, speed: float = Speed.Medium):
        distance_in_mm = distance_in_mm * -1
        wheel_controller = Shared.get_wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                                       WheelController.__wheel_diameter_in_mm,
                                                       WheelController.__axle_track_in_mm)
        wheel_controller.settings(straight_speed=speed)
        wheel_controller.straight(distance_in_mm)

    @staticmethod
    def wheel_right_turn():
        wheel_controller = Shared.get_wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                                       WheelController.__wheel_diameter_in_mm,
                                                       WheelController.__axle_track_in_mm)
        wheel_controller.turn(90)

    @staticmethod
    def wheel_left_turn():
        wheel_controller = Shared.get_wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                                       WheelController.__wheel_diameter_in_mm,
                                                       WheelController.__axle_track_in_mm)
        wheel_controller.turn(-90)

    @staticmethod
    def check_when_button_pressed():
        while True:
            res = WheelController.__button.touched()
            print("is touched: ", res)
            wait(500)
