from colorcontroller import ColorController
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task


async def main():
    print("Start, pb version: ", version)
    await WheelController.move_wheels_towards_element_then_stop_at_marker()
    print("DONE!")


run_task(main())
