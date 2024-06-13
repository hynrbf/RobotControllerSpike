from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from shared import Shared


class GripperController:
    __right_motor = Motor(Port.B)
    __left_motor = Motor(Port.A)
    __both_motors = DriveBase(__left_motor, __right_motor, 56, 117)
    __grip_turn_angle = 90

    @staticmethod
    def reset_right_arm():
        Shared.hub().display.icon(Icon.EMPTY)
        GripperController.__get_right_arm_angle()
        wait(100)

        GripperController.__right_motor.run_target(500, 0)
        wait(100)

        GripperController.__get_right_arm_angle()

    @staticmethod
    def grip_element_using_right_arm():
        GripperController.__right_motor.run_angle(500, GripperController.__grip_turn_angle, wait=True)
        Shared.hub().display.icon(Icon.SAD)
        wait(500)

        GripperController.__get_right_arm_angle()

    @staticmethod
    def reset_left_arm():
        Shared.hub().display.icon(Icon.EMPTY)
        GripperController.__get_left_arm_angle()
        wait(100)

        GripperController.__left_motor.run_target(500, 0)
        wait(100)

        GripperController.__get_left_arm_angle()

    @staticmethod
    def grip_element_using_left_arm():
        GripperController.__left_motor.run_angle(500, -GripperController.__grip_turn_angle, wait=True)
        Shared.hub().display.icon(Icon.SAD)
        wait(500)

        GripperController.__get_left_arm_angle()

    @staticmethod
    def grip_element_using_both_arms():
        GripperController.__both_motors.turn(GripperController.__grip_turn_angle / 2)
        Shared.hub().display.icon(Icon.SAD)
        wait(500)

    @staticmethod
    def release_element_using_both_arms():
        GripperController.__both_motors.turn(-(GripperController.__grip_turn_angle / 2))
        Shared.hub().display.icon(Icon.SAD)
        wait(500)

    @staticmethod
    def __get_right_arm_angle() -> int:
        current_angle = GripperController.__right_motor.angle()
        print("right arm current angle", current_angle)
        return current_angle

    @staticmethod
    def __get_left_arm_angle() -> int:
        current_angle = GripperController.__left_motor.angle()
        print("left arm current angle", current_angle)
        return current_angle
