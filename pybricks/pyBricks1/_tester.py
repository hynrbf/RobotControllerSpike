from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task


async def main():
    print("Start, pb version: ", version)
    await WheelController.move_wheels_forward_in_straight_line(float(600))
    print("DONE!")


run_task(main())
