from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task
from pybricks.tools import wait, multitask


async def test_wheel():
    await WheelController.wheel_left_turn()
    await wait(1000)
    await WheelController.wheel_right_turn()


async def test_gripper():
    await GripperController.reset_left_arm()
    await GripperController.grip_element_using_left_arm()
    await wait(1000)
    await GripperController.reset_right_arm()
    await GripperController.grip_element_using_right_arm()


async def main():
    print("Start, pb version: ", version)
    await multitask(WheelController.move_wheels_backward_in_straight_line(float(400), float(100)),
                    ColorController.detect_white_or_black_mat_color())
    # await WheelController.move_wheels_back_then_stop_at_center_line()

    print("DONE!")


run_task(main())
