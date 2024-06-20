from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task
from pybricks.tools import wait, multitask


async def main():
    print("Start, pb version: ", version)
    await WheelController.move_wheels_forward_in_straight_line(float(60))
    await WheelController.move_wheels_towards_element_then_stop_at_marker()
    await WheelController.move_wheels_backward_in_straight_line(float(20))
    await multitask(GripperController.reset_left_arm(),
                    WheelController.move_wheels_backward_in_straight_line(float(100)))
    await GripperController.grip_element_using_left_arm()
    await WheelController.move_wheels_forward_in_straight_line(float(60))
    await WheelController.move_wheels_towards_element_then_stop_at_marker()
    await WheelController.move_wheels_backward_in_straight_line(float(60))

    print("DONE!")


run_task(main())
