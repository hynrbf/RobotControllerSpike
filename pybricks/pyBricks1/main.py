from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version


def main():
    print("Start pyb version:", version)
    GripperController.reset_left_arm()
    GripperController.reset_right_arm()
    # example of moving motors straight. e.g. float(1000) is 1 meter which is 1000mm
    WheelController.move_wheels_backward_in_straight_line(float(100), Speed.Slow)

    WheelController.move_wheels_forward_in_straight_line(float(1600), Speed.Fast)

    # reset all controllers
    GripperController.reset_left_arm()
    GripperController.reset_right_arm()
    WheelController.reset_wheels()
    print("DONE!")

    # ignore below, tester only
    # print("Test simple run")


main()
