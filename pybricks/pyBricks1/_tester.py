from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task, multitask
from pybricks.tools import wait


async def move_gripper():
    while True:
        await GripperController.grip_element_using_both_arms()
        await wait(100)
        await GripperController.release_element_using_both_arms()
        await wait(100)


async def main():
    print("Start, pb version: ", version)
    # await WheelController.move_wheels_forward_while_in_white_line()
    # await WheelController.move_wheels_backward_while_in_white_line()
    # await GripperController.grip_element_using_right_arm()
    # await GripperController.grip_element_using_left_arm()

    await multitask(WheelController.move_wheels_forward_while_in_white_line(Speed.Medium), move_gripper())
    print("DONE!")


run_task(main())
