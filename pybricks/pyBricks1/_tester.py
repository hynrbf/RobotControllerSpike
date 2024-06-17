from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task
from pybricks.tools import wait


async def main():
    print("Start, pb version: ", version)
    await WheelController.move_wheels_towards_water_tower_stop_at_brown_marker()
    await GripperController.hook_element_using_left_arm()
    await WheelController.move_wheels_backward_in_straight_line(float(100), Speed.Slow)
    await WheelController.wheel_slight_left_turn(20)
    await WheelController.move_wheels_forward_in_straight_line(float(100), Speed.Slow)
    await WheelController.move_wheels_backward_in_straight_line(float(100), Speed.Slow)
    print("DONE!")


run_task(main())
