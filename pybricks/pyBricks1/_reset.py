from grippercontroller import GripperController
from wheelcontroller import WheelController
from pybricks import version


def main():
    print("Start, pb version: ", version)

    # reset all controllers
    GripperController.reset_left_arm()
    GripperController.reset_right_arm()
    WheelController.reset_wheels()
    print("DONE!")


main()
