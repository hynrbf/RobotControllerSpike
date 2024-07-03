from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task
from pybricks.tools import wait, multitask


async def main():
    print("Start, pb version: ", version)
    #code to hook the element
    await GripperController.grip_element_using_both_arms()
    await WheelController.move_wheels_forward_in_straight_line(float(80))
    await multitask(GripperController.reset_left_arm(), WheelController.move_wheels_forward_in_straight_line(float(10)))
    print("DONE!")


run_task(main())
