from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version


def main():
    print("Start, pb version: ", version)
    GripperController.reset_left_arm()
    GripperController.reset_right_arm()
    # example of moving motors straight. e.g. float(1000) is 1 meter which is 1000mm
    WheelController.move_wheels_backward_in_straight_line(float(100), Speed.Medium)

    # when getting vegetable, yung bigat could affect the gyro, so make sure to compute distance
    # via sensing the white color or ibangga sa edge
    # get red vegetable and yellow
    WheelController.move_wheels_forward_in_straight_line(float(90))
    WheelController.wheel_left_turn()
    WheelController.move_wheels_forward_in_straight_line(float(260))
    GripperController.grip_element_using_both_arms()

    # get another set of vegetable
    WheelController.move_wheels_backward_in_straight_line(float(120))
    WheelController.wheel_right_turn()
    WheelController.move_wheels_forward_in_straight_line(float(140))
    WheelController.wheel_left_turn()
    GripperController.release_element_using_both_arms()
    WheelController.move_wheels_forward_in_straight_line(float(120))
    GripperController.grip_element_using_both_arms()

    # going long straight
    WheelController.move_wheels_backward_in_straight_line(float(160))
    WheelController.wheel_right_turn()
    WheelController.move_wheels_forward_in_straight_line(float(1600))
    WheelController.wheel_slight_left_turn()
    WheelController.move_wheels_forward_in_straight_line(float(210))
    GripperController.reset_left_arm()
    WheelController.move_wheels_backward_in_straight_line(float(210))
    WheelController.wheel_slight_left_turn()
    GripperController.grip_element_using_left_arm()

    # going to red market
    WheelController.move_wheels_backward_in_straight_line(float(800))
    WheelController.move_wheels_forward_in_straight_line(float(120))
    WheelController.wheel_right_turn()
    WheelController.move_wheels_backward_in_straight_line(float(600))
    GripperController.release_element_using_both_arms()

    # go back to starting point
    WheelController.move_wheels_backward_in_straight_line(float(1600))
    WheelController.move_wheels_forward_in_straight_line(float(200))
    WheelController.wheel_left_turn()
    WheelController.move_wheels_forward_in_straight_line(float(800))
    WheelController.wheel_right_turn()

    # reset all controllers
    GripperController.reset_left_arm()
    GripperController.reset_right_arm()
    WheelController.reset_wheels()
    print("DONE!")

    # ignore below, tester only
    # print("Test simple run")


main()
