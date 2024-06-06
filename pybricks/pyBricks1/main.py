from colorcontroller import ColorController
from pybricks.parameters import Port
from grabbercontroller import GrabberController


def main():
    ColorController.get_mat_color(Port.A)
    GrabberController.grab_element_right_arm()

    # ignore below, tester only
    # print("Test simple run")


main()
