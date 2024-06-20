from grippercontroller import GripperController
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task


async def main():
    print("Start, pb version: ", version)

    # reset all controllers
    await GripperController.reset_left_arm()
    await GripperController.reset_right_arm()
    await WheelController.reset_wheels()

    # put gripper to close
    # await GripperController.grip_element_using_both_arms()
    print("DONE!")


run_task(main())
