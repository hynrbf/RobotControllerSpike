from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait


class GripperController:
    motor = Motor(Port.B)

    @staticmethod
    def reset_right_arm():
        GripperController.__get_right_arm_angle()
        wait(100)

        GripperController.motor.reset_angle(0)
        wait(100)

        GripperController.__get_right_arm_angle()

    @staticmethod
    def grip_element_using_right_arm():
        GripperController.motor.run_angle(200, 180, wait=True)
        wait(100)

        GripperController.__get_right_arm_angle()

    @staticmethod
    def release_element_using_right_arm():
        GripperController.motor.run_angle(200, -180, wait=True)
        wait(100)

        GripperController.__get_right_arm_angle()

    @staticmethod
    def grab_element_left_arm():
        print('left')

    @staticmethod
    def grab_element_both_arm():
        print('both')

    @staticmethod
    def __get_right_arm_angle() -> int:
        current_angle = GripperController.motor.angle()
        print("right arm current angle", current_angle)
        return current_angle
