from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task, multitask


async def hook_element():
    print("Start, pb version: ", version)
    await WheelController.move_wheels_backward_in_straight_line(float(50))
    await WheelController.move_wheels_forward_in_straight_line(float(30))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(70))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(1161), Speed.Medium)
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(100), Speed.Slow)
    await WheelController.move_wheels_towards_water_tower_stop_at_brown_marker()
    await GripperController.hook_element_using_left_arm()
    await WheelController.move_wheels_backward_in_straight_line(float(100))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_backward_in_straight_line(float(30), Speed.Slow)
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(40), Speed.Slow)
    await WheelController.wheel_right_turn()


# Anton's code
async def get_the_vegetables():
    # await GripperController.reset_left_arm()
    # await GripperController.reset_right_arm()
    # wheel_to_butt_distance = float(50)
    # left_turn_variance_to_left_wheel = float(60)
    # right_turn_variance_to_right_wheel = float(60)
    # await WheelController.move_wheels_backward_in_straight_line(float(170) - wheel_to_butt_distance, Speed.Medium)

    # get red vegetable and yellow
    left_turn_variance_to_left_wheel = float(60)
    await WheelController.move_wheels_forward_in_straight_line(float(50))
    await WheelController.wheel_left_turn()
    # original float(250)
    await WheelController.move_wheels_forward_in_straight_line(float(200) + left_turn_variance_to_left_wheel)
    await GripperController.grip_element_using_both_arms()

    # get another set of vegetable
    await WheelController.move_wheels_backward_in_straight_line(float(150))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(180))
    await WheelController.wheel_left_turn()
    await multitask(GripperController.release_element_using_both_arms(),
                    WheelController.move_wheels_forward_in_straight_line(float(135)))
    await GripperController.grip_element_using_both_arms()

    # going long straight to the compose area
    await WheelController.move_wheels_backward_in_straight_line(float(200))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(1670))
    await WheelController.wheel_slight_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(240))
    await multitask(GripperController.reset_left_arm(),
                    WheelController.move_wheels_backward_in_straight_line(float(430)))
    await multitask(WheelController.wheel_slight_left_turn(), GripperController.grip_element_using_left_arm())

    # going to red market
    await WheelController.move_wheels_backward_in_straight_line(float(570))
    await WheelController.move_wheels_forward_in_straight_line(float(60))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_backward_in_straight_line(float(800))
    await GripperController.release_element_using_both_arms()


async def get_the_vegetables_at_the_market():
    print("start")
    await WheelController.move_wheels_backward_in_straight_line(float(170))
    await WheelController.wheel_u_turn_left()
    await WheelController.move_wheels_forward_in_straight_line(float(160))
    is_red = await ColorController.detect_red_vegetable()

    if is_red:
        await WheelController.wheel_right_turn_with_angle(float(20))
        await WheelController.move_wheels_forward_in_straight_line(float(20))
        await GripperController.grip_element_using_left_arm()

    await WheelController.wheel_left_turn_with_angle(float(20))
    await WheelController.move_wheels_forward_in_straight_line(float(30))
    is_yellow = await ColorController.detect_yellow_vegetable()

    if is_yellow:
        await WheelController.wheel_left_turn_with_angle(float(20))
        await WheelController.move_wheels_forward_in_straight_line(float(50))
        await GripperController.grip_element_using_right_arm()

    await WheelController.wheel_right_turn_with_angle(float(20))
    await WheelController.move_wheels_backward_in_straight_line(float(400))
    await GripperController.reset_left_arm()


# Alfeo's code
async def water_if_green_plant() -> bool:
    is_green_detected = False

    if await ColorController.detect_green_vegetable():
        await WheelController.move_wheels_backward_in_straight_line(float(30))
        await multitask(GripperController.reset_left_arm(),
                        WheelController.move_wheels_backward_in_straight_line(float(100)))
        await GripperController.grip_element_using_left_arm()
        await WheelController.move_wheels_forward_in_straight_line(float(60))
        await WheelController.move_wheels_towards_element_then_stop_at_marker()
        await WheelController.move_wheels_backward_in_straight_line(float(150))
        is_green_detected = True
    else:
        await multitask(GripperController.grip_element_using_both_arms(),
                        WheelController.move_wheels_forward_in_straight_line(float(90)))
        await WheelController.move_wheels_backward_in_straight_line(float(220))

    return is_green_detected


async def water_the_green_plants():
    await WheelController.move_wheels_forward_in_straight_line(float(50))
    await GripperController.grip_element_using_left_arm()
    await WheelController.wheel_left_turn_with_angle(float(30))
    await WheelController.move_wheels_forward_in_straight_line(float(160))
    await WheelController.wheel_right_turn_with_angle(float(30))
    await WheelController.move_wheels_forward_in_straight_line(float(305))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(60))
    await WheelController.move_wheels_towards_element_then_stop_at_marker()
    is_green_detected = await water_if_green_plant()

    if is_green_detected:
        await WheelController.wheel_right_turn()
        await multitask(GripperController.release_element_using_both_arms(),
                        WheelController.move_wheels_backward_in_straight_line(float(650)))
        return

    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(165))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(60))
    await WheelController.move_wheels_towards_element_then_stop_at_marker()

    is_green_detected = await water_if_green_plant()

    if is_green_detected:
        await WheelController.wheel_right_turn()
        await multitask(GripperController.release_element_using_both_arms(),
                        WheelController.move_wheels_backward_in_straight_line(float(750)))
        return

    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(165))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(60))
    await WheelController.move_wheels_towards_element_then_stop_at_marker()

    await water_if_green_plant()
    await WheelController.wheel_right_turn()
    await multitask(GripperController.release_element_using_both_arms(),
                    WheelController.move_wheels_backward_in_straight_line(float(950)))


# 1) example of moving motors straight. e.g. float(1000) is 1 meter which is 1000mm
# 2) when getting vegetable, yung bigat could affect the gyro, so make sure to compute distance
#    via sensing the white color or ibangga sa edge

async def main():
    print("Start, pb version: ", version)
    await water_the_green_plants()
    await get_the_vegetables()
    await get_the_vegetables_at_the_market()
    # await multitask(get_the_vegetables(), WheelController.debug())
    print("DONE!")

    # ignore below, tester only
    # print("Test simple run")


run_task(main())
