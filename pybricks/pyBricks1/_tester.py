from colorcontroller import ColorController
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task


async def main():
    print("Start, pb version: ", version)
    await WheelController.move_wheels_towards_element_using_sensor()
    print("DONE!")


run_task(main())
