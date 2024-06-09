# from colorcontroller import ColorController
# from grippercontroller import GripperController
# from pybricks.tools import wait
from shared import Speed
from wheelcontroller import WheelController


def main():
    # example of moving motors straight. e.g. float(1000) is 1 meter which is 1000mm
    WheelController.move_wheels_backward_in_straight_line(float(100), Speed.Slow)

    WheelController.move_wheels_forward_in_straight_line(float(100), Speed.Slow)
    WheelController.wheel_left_turn()
    WheelController.move_wheels_forward_in_straight_line(float(500))

    WheelController.move_wheels_backward_in_straight_line(float(200), Speed.Slow)
    WheelController.wheel_right_turn()
    WheelController.move_wheels_forward_in_straight_line(float(100), Speed.Slow)
    WheelController.wheel_left_turn()
    WheelController.move_wheels_forward_in_straight_line(float(200), Speed.Slow)

    WheelController.move_wheels_backward_in_straight_line(float(500))
    WheelController.wheel_right_turn()
    WheelController.move_wheels_forward_in_straight_line(float(2000), Speed.Fast)

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
