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
    await wait(1000)
    await WheelController.wheel_right_turn()
    await wait(1000)
    await WheelController.wheel_left_turn()


async def test_gripper():
    await GripperController.reset_left_arm()
    await GripperController.grip_element_using_left_arm()
    await wait(1000)
    await GripperController.reset_right_arm()
    await GripperController.grip_element_using_right_arm()


async def test_green_color():
    is_green = await ColorController.detect_green_vegetable()
    print("Is green: ", is_green)


async def main():
    print("Start, pb version: ", version)

    # await test_wheel()
    # await test_gripper()
    # await test_green_color()

    await WheelController.move_wheels_forward_in_straight_line(float(2000))

    print("DONE!")


run_task(main())
