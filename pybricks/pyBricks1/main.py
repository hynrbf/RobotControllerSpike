from colorcontroller import ColorController
from grippercontroller import GripperController


def main():
    if ColorController.detect_yellow_vegetable():
        GripperController.reset_right_arm()
        GripperController.grip_element_using_right_arm()

    if ColorController.detect_red_vegetable():
        GripperController.reset_left_arm()
        GripperController.grip_element_using_left_arm()

    GripperController.reset_left_arm()
    GripperController.reset_right_arm()
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
