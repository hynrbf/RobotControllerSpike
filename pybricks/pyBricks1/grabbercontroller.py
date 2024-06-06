from pybricks.pupdevices import Motor
from pybricks.parameters import Port


class GrabberController:
    @staticmethod
    def grab_element_right_arm():
        gripper_motor = Motor(Port.B)
        gripper_motor.run_angle(200, 720, wait=True)
        print("right arm")

    @staticmethod
    def grab_element_left_arm():
        print('left')

    @staticmethod
    def grab_element_both_arm():
        print('both')
