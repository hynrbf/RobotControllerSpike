from grippercontroller import GripperController
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task


async def main():
    print("Start, pb version: ", version)

    # reset all controllers
    # gripper should be in reset position to know to set in start that the arms is in release=0 position
    await GripperController.reset_both_arms()
    await WheelController.reset_wheels()
    print("DONE!")


run_task(main())
