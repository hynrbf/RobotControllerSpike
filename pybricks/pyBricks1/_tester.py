from colorcontroller import ColorController
from grippercontroller import GripperController
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task


async def main():
    print("Start, pb version: ", version)
    #await WheelController.move_wheels_forward_while_in_white_line()
    # await WheelController.move_wheels_backward_while_in_white_line()
    #await GripperController.grip_element_using_right_arm()
    #await GripperController.grip_element_using_left_arm()
    await GripperController.grip_element_using_both_arms()
    print("DONE!")


run_task(main())
