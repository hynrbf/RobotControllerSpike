# from colorcontroller import ColorController
# from grippercontroller import GripperController
# from pybricks.tools import wait
from wheelcontroller import WheelController


def main():
    WheelController.move_forward_left_motor()

    # while True:
    # if ColorController.detect_yellow_vegetable():
    #  GripperController.reset_left_arm()
    # GripperController.grip_element_using_left_arm()

    # GripperController.reset_right_arm()
    # wait(1000)

    # if ColorController.detect_red_vegetable():
    #     GripperController.reset_right_arm()
    #     GripperController.grip_element_using_right_arm()
    #
    #     GripperController.reset_right_arm()
    #     wait(1000)
    # GripperController.reset_left_arm()
    # GripperController.reset_right_arm()
    # GripperController.reset_right_arm()
    # GripperController.grip_element_using_right_arm()
    # GripperController.reset_right_arm()
    #
    # GripperController.reset_left_arm()
    # GripperController.grip_element_using_left_arm()
    # GripperController.reset_left_arm()

    # ignore below, tester only
    # print("Test simple run")


main()
