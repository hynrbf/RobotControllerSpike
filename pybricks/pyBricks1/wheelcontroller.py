from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Icon
from pybricks.tools import wait
from shared import Shared, Speed


class WheelController:
    # I measured manually and the wheel diameter is 5.6cm and the axle distance is 11.7cm
    __wheel_diameter_in_mm = float(56)
    __axle_track_in_mm = float(117)

    __left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
    __right_motor = Motor(Port.F)

    @staticmethod
    def reset_wheels():
        WheelController.__left_motor.run_target(500, 0)
        WheelController.__right_motor.run_target(500, 0)
        wait(100)

    @staticmethod
    def move_wheels_forward_in_straight_line(distance_in_mm: float, speed: float = Speed.Medium):
        Shared.hub().display.icon(Icon.ARROW_UP)
        wheel_controller = Shared.get_wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                                       WheelController.__wheel_diameter_in_mm,
                                                       WheelController.__axle_track_in_mm)
        wheel_controller.settings(straight_speed=speed)
        wheel_controller.straight(distance_in_mm)

    @staticmethod
    def move_wheels_backward_in_straight_line(distance_in_mm: float, speed: float = Speed.Medium):
        Shared.hub().display.icon(Icon.ARROW_DOWN)
        distance_in_mm = distance_in_mm * -1
        wheel_controller = Shared.get_wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                                       WheelController.__wheel_diameter_in_mm,
                                                       WheelController.__axle_track_in_mm)
        wheel_controller.settings(straight_speed=speed)
        wheel_controller.straight(distance_in_mm)

    @staticmethod
    def wheel_right_turn():
        Shared.hub().display.icon(Icon.ARROW_RIGHT)
        wheel_controller = Shared.get_wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                                       WheelController.__wheel_diameter_in_mm,
                                                       WheelController.__axle_track_in_mm)
        wheel_controller.turn(90)

    @staticmethod
    def wheel_left_turn():
        Shared.hub().display.icon(Icon.ARROW_LEFT)
        wheel_controller = Shared.get_wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                                       WheelController.__wheel_diameter_in_mm,
                                                       WheelController.__axle_track_in_mm)
        wheel_controller.turn(-90)

    @staticmethod
    def wheel_slight_left_turn():
        Shared.hub().display.icon(Icon.ARROW_LEFT)
        wheel_controller = Shared.get_wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                                       WheelController.__wheel_diameter_in_mm,
                                                       WheelController.__axle_track_in_mm)
        wheel_controller.turn(-45)
