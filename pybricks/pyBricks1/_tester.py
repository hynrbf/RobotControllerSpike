from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task
from pybricks.tools import wait, multitask


async def main():
    print("Start, pb version: ", version)
    await WheelController.move_wheels_towards_element_then_stop_at_marker()
    print("DONE!")


run_task(main())
