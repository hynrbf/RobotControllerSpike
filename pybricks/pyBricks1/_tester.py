from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task
from pybricks.tools import wait, multitask


async def main():
    print("Start, pb version: ", version)

    await WheelController.wheel_right_turn()
    await wait(500)
    await WheelController.wheel_left_turn()

    print("DONE!")


run_task(main())
