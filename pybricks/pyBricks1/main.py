from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version


# Notes:
# 1) example of moving motors straight. e.g. float(1000) is 1 meter which is 1000mm
# 2) when getting vegetable, yung bigat could affect the gyro, so make sure to compute distance
#    via sensing the white color or ibangga sa edge

def main():
    print("Start, pb version: ", version)
    ColorController.get_mat_color()
    print("DONE!")

    # ignore below, tester only
    # print("Test simple run")


main()
