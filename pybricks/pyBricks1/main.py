from colorcontroller import ColorController
from grippercontroller import GripperController
from pybricks.tools import wait
from wheelcontroller import WheelController


def main():
    # example of moving motors and it will stop when bump
    WheelController.move_forward_both_motors()

    # exampl of gripping when detecting yellow element
    while True:
        if ColorController.detect_yellow_vegetable():
            GripperController.reset_left_arm()
            GripperController.grip_element_using_left_arm()

        GripperController.reset_right_arm()
        wait(1000)

    # ignore below, tester only
    # print("Test simple run")


main()
