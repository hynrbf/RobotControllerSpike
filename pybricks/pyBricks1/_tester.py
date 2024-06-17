from colorcontroller import ColorController
from grippercontroller import GripperController
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task


async def main():
    print("Start, pb version: ", version)
    await GripperController.hook_element_using_left_arm()
    print("DONE!")


run_task(main())
