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

    # await test_wheel()
    # await test_gripper()
    # await test_green_color()

    # get vegetable in a container
    await multitask(GripperController.reset_left_arm(), GripperController.reset_right_arm())
    await GripperController.grip_element_using_both_arms()

    # get vegetable in a container and detect color
    await WheelController.move_wheels_forward_in_straight_line(float(50))
    await WheelController.wheel_u_turn_right()
    await WheelController.move_wheels_forward_in_straight_line(float(50))
    await GripperController.reset_both_arms()
    await WheelController.wheel_right_turn_with_angle(float(20))
    await WheelController.move_wheels_forward_in_straight_line(float(70))
    is_red = await ColorController.detect_red_vegetable()
    print("is red:", is_red)

    # now grip the element
    await WheelController.move_wheels_backward_in_straight_line(float(70))
    await WheelController.wheel_right_turn_with_angle(float(70))
    await WheelController.move_wheels_forward_in_straight_line(float(110))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(70), with_brake=True)
    await GripperController.grip_element_using_left_arm()
    await WheelController.move_wheels_backward_in_straight_line(float(70))
    await WheelController.wheel_left_turn()

    print("DONE!")


run_task(main())
