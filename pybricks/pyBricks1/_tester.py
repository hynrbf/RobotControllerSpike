from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task
from pybricks.tools import wait, multitask


async def main():
    print("Start, pb version: ", version)
    await GripperController.release_element_using_both_arms()
    await wait(500)
    await GripperController.grip_element_using_both_arms()
    print("DONE!")


run_task(main())
