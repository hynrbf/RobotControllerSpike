from colorcontroller import ColorController
from grippercontroller import GripperController
from pybricks.tools import wait
from shared import Speed
from wheelcontroller import WheelController


def get_red_vegetable():
    try_count = 1

    while True:
        if ColorController.detect_red_vegetable() or try_count > 5:
            GripperController.grip_element_using_left_arm()
            break

        try_count = try_count + 1
        wait(500)


def main():
    print("Start.")
    GripperController.reset_left_arm()
    # example of moving motors straight. e.g. float(1000) is 1 meter which is 1000mm
    WheelController.move_wheels_backward_in_straight_line(float(100), Speed.Slow)

    # get red vegetable
    WheelController.move_wheels_forward_in_straight_line(float(100), Speed.Slow)
    WheelController.wheel_left_turn()
    WheelController.move_wheels_forward_in_straight_line(float(500))
    get_red_vegetable()

    # get another vegetable
    WheelController.move_wheels_backward_in_straight_line(float(200), Speed.Slow)
    WheelController.wheel_right_turn()
    WheelController.move_wheels_forward_in_straight_line(float(100), Speed.Slow)
    WheelController.wheel_left_turn()
    WheelController.move_wheels_forward_in_straight_line(float(200), Speed.Slow)

    WheelController.move_wheels_backward_in_straight_line(float(500))
    WheelController.wheel_right_turn()
    WheelController.move_wheels_forward_in_straight_line(float(1800), Speed.Fast)
    WheelController.wheel_slight_left_turn()
    WheelController.move_wheels_forward_in_straight_line(float(200))
    GripperController.reset_left_arm()
    WheelController.move_wheels_backward_in_straight_line(float(200))
    WheelController.wheel_slight_left_turn()
    GripperController.grip_element_using_left_arm()

    WheelController.move_wheels_backward_in_straight_line(float(900))
    WheelController.wheel_right_turn()
    WheelController.move_wheels_backward_in_straight_line(float(800))

    # reset all controllers
    GripperController.reset_left_arm()
    WheelController.reset_wheels()
    print("DONE!")

    # ignore below, tester only
    # print("Test simple run")


main()
