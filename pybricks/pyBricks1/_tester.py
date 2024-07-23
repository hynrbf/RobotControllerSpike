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
    await wait(1000)
    await GripperController.reset_left_arm()
    await GripperController.reset_right_arm()
    await wait(1000)
    await GripperController.grip_element_using_both_arms()
    await wait(1000)
    await GripperController.release_element_using_both_arms()


async def test_green_color():
    is_green = await ColorController.detect_green_vegetable()
    print("Is green: ", is_green)


async def main():
    print("Start, pb version: ", version)
    await GripperController.reset_both_arms()

    # await test_gripper()
    # await test_wheel()
    # await test_green_color()

    await WheelController.move_wheels_forward_in_straight_line(float(290))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(50))
    await WheelController.wheel_left_turn_with_angle(20)
    is_red = await ColorController.detect_red_vegetable()
    await WheelController.wheel_right_turn_with_angle(40)
    is_red_again = await ColorController.detect_red_vegetable()
    await WheelController.wheel_left_turn_with_angle(20)
    await WheelController.move_wheels_forward_in_straight_line(float(100), Speed.Slow)
    await GripperController.grip_element_using_both_arms()
    print("result ", is_red, is_red_again)

    if is_red and is_red_again:
        await WheelController.move_wheels_backward_in_straight_line(float(100))
        await WheelController.wheel_left_turn()
        await WheelController.move_wheels_forward_in_straight_line(float(320))
        await WheelController.wheel_right_turn()
        await multitask(WheelController.move_wheels_forward_in_straight_line(float(150)),
                        GripperController.reset_both_arms())

    print("DONE!")


run_task(main())
