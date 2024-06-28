from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task
from pybricks.tools import wait, multitask


async def main():
    print("Start, pb version: ", version)
    result = await ColorController.detect_brown_mat_color()
    print("result: ", result)
    print("DONE!")


run_task(main())
