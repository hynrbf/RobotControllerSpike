# from colorcontroller import ColorController
# from grippercontroller import GripperController
# from pybricks.tools import wait
from wheelcontroller import WheelController


def main():
    # example of moving motors straight for 1 meter which is 1000mm
    distance_in_mm = float(1000)
    WheelController.move_wheel_in_straight_line(distance_in_mm)

    WheelController.wheel_right_turn()
    distance_in_mm = float(200)
    WheelController.move_wheel_in_straight_line(distance_in_mm)

    WheelController.wheel_left_turn()
    distance_in_mm = float(500)
    WheelController.move_wheel_in_straight_line(distance_in_mm)

    # exampl of gripping when detecting yellow element
    # while True:
    #     if ColorController.detect_yellow_vegetable():
    #         GripperController.reset_left_arm()
    #         GripperController.grip_element_using_left_arm()
    #
    #     GripperController.reset_right_arm()
    #     wait(1000)

    # ignore below, tester only
    # print("Test simple run")


main()
