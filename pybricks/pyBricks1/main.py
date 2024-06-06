# from colorcontroller import ColorController
# from pybricks.parameters import Port
from grippercontroller import GripperController


def main():
    # ColorController.get_mat_color(Port.A)
    GripperController.reset_right_arm()
    GripperController.grip_element_using_right_arm()
    GripperController.release_element_using_right_arm()

    # ignore below, tester only
    # print("Test simple run")


main()
