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

    await WheelController.move_wheels_forward_in_straight_line(float(1000))

    print("DONE!")


run_task(main())
