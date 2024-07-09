from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task
from pybricks.tools import wait, multitask


async def main():
    print("Start, pb version: ", version)
    # code to hook the element
    # await GripperController.grip_element_using_both_arms()
    # await WheelController.move_wheels_forward_in_straight_line(float(80))
    # await multitask(GripperController.reset_left_arm(), WheelController.move_wheels_forward_in_straight_line(float(10)))

    # await WheelController.wheel_right_turn()
    # await wait(1000)
    # await WheelController.wheel_left_turn()
    # await wait(1000)
    # await WheelController.wheel_left_turn()
    # await wait(1000)
    # await WheelController.wheel_left_turn()
    # await wait(1000)
    # await WheelController.wheel_right_turn()
    # await wait(1000)
    # await WheelController.wheel_right_turn()

    await WheelController.move_wheels_forward_in_straight_line(float(30), Speed.Slow)
    await GripperController.hook_element_upwards(angle=25)
    await WheelController.move_wheels_backward_in_straight_line(float(50), Speed.Slow)
    await WheelController.move_wheels_forward_in_straight_line(float(60), Speed.Slow)
    await WheelController.move_wheels_backward_in_straight_line(float(50), Speed.Slow)
    await GripperController.hook_element_downwards(angle=25)
    await WheelController.move_wheels_backward_in_straight_line(float(20), Speed.Slow)
    await WheelController.wheel_right_turn_with_angle(15)
    await multitask(GripperController.reset_left_arm(), GripperController.reset_right_arm())
    await GripperController.grip_element_using_both_arms()

    await multitask(GripperController.hook_element_upwards_using_left(angle=20),
                    WheelController.move_wheels_forward_in_straight_line(float(120)))

    await GripperController.hook_element_downwards_using_left(angle=20)
    await WheelController.move_wheels_backward_in_straight_line(float(90))
    await WheelController.wheel_right_turn_with_angle(75)

    print("DONE!")


run_task(main())
