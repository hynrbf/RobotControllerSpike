from colorcontroller import ColorController
from grippercontroller import GripperController
from pybricks.tools import wait


def main():
    while True:
        if ColorController.detect_yellow_vegetable():
            GripperController.reset_right_arm()
            GripperController.grip_element_using_right_arm()

        GripperController.reset_right_arm()
        wait(1000)

    # if ColorController.detect_red_vegetable():
    #   GripperController.reset_left_arm()
    #   GripperController.grip_element_using_left_arm()

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
