from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Icon
from pybricks.robotics import DriveBase
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
        WheelController.__left_motor.run_target(Speed.Fast, 0)
        WheelController.__right_motor.run_target(Speed.Fast, 0)
        wait(100)

        state = WheelController.__object().state()
        print("State of robot is: ", state)

    @staticmethod
    def move_wheels_forward_in_straight_line(distance_in_mm: float, speed: float = Speed.Medium):
        Shared.hub().display.icon(Icon.ARROW_UP)
        wheel_controller = WheelController.__object()
        wheel_controller.settings(straight_speed=speed)
        wheel_controller.straight(distance_in_mm)

        travelled_distance = WheelController.__get_distance_in_mm()
        print("Travelled distance in mm: ", travelled_distance)

    @staticmethod
    def move_wheels_backward_in_straight_line(distance_in_mm: float, speed: float = Speed.Medium):
        Shared.hub().display.icon(Icon.ARROW_DOWN)
        distance_in_mm = distance_in_mm * -1
        wheel_controller = WheelController.__object()
        wheel_controller.settings(straight_speed=speed)
        wheel_controller.straight(distance_in_mm)

        travelled_distance = WheelController.__get_distance_in_mm()
        print("Travelled distance in mm: ", travelled_distance)

    @staticmethod
    def wheel_right_turn():
        Shared.hub().display.icon(Icon.ARROW_RIGHT)
        wheel_controller = WheelController.__object()
        wheel_controller.turn(90)

    @staticmethod
    def wheel_left_turn():
        Shared.hub().display.icon(Icon.ARROW_LEFT)
        wheel_controller = WheelController.__object()
        wheel_controller.turn(-90)

    @staticmethod
    def wheel_slight_left_turn():
        Shared.hub().display.icon(Icon.ARROW_LEFT)
        wheel_controller = WheelController.__object()
        wheel_controller.turn(-45)

    @staticmethod
    def __get_distance_in_mm() -> int:
        wheel_controller = WheelController.__object()
        return wheel_controller.distance()

    @staticmethod
    def __object() -> DriveBase:
        return Shared.wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                       WheelController.__wheel_diameter_in_mm,
                                       WheelController.__axle_track_in_mm)
