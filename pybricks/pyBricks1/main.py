from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import multitask, run_task


# Notes:
# 1) example of moving motors straight. e.g. float(1000) is 1 meter which is 1000mm
# 2) when getting vegetable, yung bigat could affect the gyro, so make sure to compute distance
#    via sensing the white color or ibangga sa edge

async def move():
    await WheelController.move_wheels_forward_in_straight_line(800)
    await WheelController.move_wheels_forward_in_straight_line(800)
    await WheelController.move_wheels_forward_in_straight_line(800)


async def main():
    print("Start, pb version: ", version)
    await multitask(ColorController.get_mat_color(), move())
    print("DONE!")


run_task(main())
