from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Icon
from pybricks.tools import wait

from shared import Shared


class GripperController:
    __right_motor = Motor(Port.B)

    @staticmethod
    def reset_right_arm():
        Shared.hub().display.icon(Icon.EMPTY)
        GripperController.__get_right_arm_angle()
        wait(100)

        GripperController.__right_motor.reset_angle(0)
        wait(100)

        GripperController.__get_right_arm_angle()

    @staticmethod
    def grip_element_using_right_arm():
        GripperController.__right_motor.run_angle(500, 270, wait=True)
        Shared.hub().display.icon(Icon.HEART)
        wait(100)

        GripperController.__get_right_arm_angle()

    @staticmethod
    def release_element_using_right_arm():
        GripperController.__right_motor.run_angle(500, -270, wait=True)
        Shared.hub().display.icon(Icon.SAD)
        wait(500)

        GripperController.__get_right_arm_angle()

    @staticmethod
    def grab_element_left_arm():
        print('left')

    @staticmethod
    def grab_element_both_arm():
        print('both')

    @staticmethod
    def __get_right_arm_angle() -> int:
        current_angle = GripperController.__right_motor.angle()
        print("right arm current angle", current_angle)
        return current_angle
