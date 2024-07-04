from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task
from pybricks.tools import wait, multitask


async def main():
    print("Start, pb version: ", version)
    result = await GripperController.sleeping_using_both_arms()
    print("is_detected =", result)
    print("DONE!")


run_task(main())
