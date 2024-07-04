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
async def get_the_vegetables_at_the_market():
    await multitask(GripperController.release_element_using_both_arms(),
                    WheelController.move_wheels_backward_in_straight_line(float(560)))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_backward_in_straight_line(float(90), with_brake=True)
    await WheelController.move_wheels_forward_in_straight_line(float(80))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(100))
    is_red = await ColorController.detect_red_vegetable()
    is_yellow = await ColorController.detect_yellow_vegetable()
    is_red_got_first = is_red and not is_yellow

    await WheelController.wheel_right_turn_with_angle(float(20))
    await WheelController.move_wheels_forward_in_straight_line(float(50))
    await GripperController.grip_element_using_left_arm()
    await WheelController.wheel_left_turn_with_angle(float(20))

    await WheelController.move_wheels_forward_in_straight_line(float(40))
    await WheelController.wheel_left_turn_with_angle(float(20))
    await WheelController.move_wheels_forward_in_straight_line(float(60))
    await GripperController.grip_element_using_right_arm()
    await WheelController.wheel_right_turn_with_angle(float(20))

    if is_red_got_first:
        await WheelController.move_wheels_backward_in_straight_line(float(380))
        await GripperController.reset_left_arm()
        await WheelController.move_wheels_backward_in_straight_line(float(100))
        await WheelController.wheel_right_turn()
        await WheelController.move_wheels_backward_in_straight_line(float(150), with_brake=True)
        await WheelController.move_wheels_forward_in_straight_line(float(200))

        await WheelController.wheel_right_turn()
        await multitask(WheelController.move_wheels_forward_in_straight_line(float(900), Speed.Straight),
                        GripperController.grip_element_using_both_arms())
    else:
        await WheelController.wheel_u_turn_right()
        await multitask(WheelController.move_wheels_forward_in_straight_line(float(380)),
                        GripperController.reset_right_arm())
        await WheelController.move_wheels_backward_in_straight_line(float(150))
        await WheelController.wheel_left_turn()
        await WheelController.move_wheels_backward_in_straight_line(float(150), with_brake=True)
        await WheelController.move_wheels_forward_in_straight_line(float(200))

        await WheelController.wheel_right_turn()
        await multitask(WheelController.move_wheels_forward_in_straight_line(float(1100), Speed.Straight),
                        GripperController.grip_element_using_both_arms())

    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(470))
    await WheelController.wheel_slight_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(300))
    await multitask(GripperController.release_element_using_both_arms(),
                    WheelController.move_wheels_backward_in_straight_line(float(300)))


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
    await WheelController.move_wheels_forward_in_straight_line(float(140) + left_turn_variance_to_left_wheel)
    await GripperController.grip_element_using_both_arms()

    # get another set of vegetable
    await WheelController.move_wheels_backward_in_straight_line(float(150))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(180))
    await WheelController.wheel_left_turn()
    await multitask(GripperController.release_element_using_both_arms(),
                    WheelController.move_wheels_forward_in_straight_line(float(140), Speed.Slow))
    await GripperController.grip_element_using_both_arms()

    # going long straight to the compose area
    await WheelController.move_wheels_backward_in_straight_line(float(200))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(1670), Speed.Straight)
    await WheelController.wheel_slight_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(310))
    await multitask(GripperController.reset_left_arm(),
                    WheelController.move_wheels_backward_in_straight_line(float(400)))
    await multitask(WheelController.wheel_slight_left_turn(), GripperController.grip_element_using_left_arm())

    # going to red market
    await WheelController.move_wheels_backward_in_straight_line(float(400))
    await WheelController.move_wheels_backward_in_straight_line(float(170), with_brake=True)
    await WheelController.move_wheels_forward_in_straight_line(float(60))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_backward_in_straight_line(float(475))


# Alfeo's code
async def water_if_green_plant() -> bool:
    is_green_detected = False

    if await ColorController.detect_green_vegetable():
        await WheelController.move_wheels_backward_in_straight_line(float(30))
        await multitask(GripperController.reset_left_arm(),
                        WheelController.move_wheels_backward_in_straight_line(float(100)))
        await GripperController.grip_element_using_left_arm()
        await WheelController.move_wheels_towards_element_then_stop_at_marker()
        await WheelController.move_wheels_backward_in_straight_line(float(130))
        is_green_detected = True
    else:
        await multitask(GripperController.grip_element_using_both_arms(),
                        WheelController.move_wheels_forward_in_straight_line(float(120)))
        await WheelController.move_wheels_backward_in_straight_line(float(220))

    return is_green_detected


async def water_the_green_plants_and_move_decay_plants():
    await WheelController.wheel_left_turn_with_angle(float(20))
    await WheelController.move_wheels_forward_in_straight_line(float(210))
    await multitask(GripperController.grip_element_using_left_arm(),
                    WheelController.wheel_right_turn_with_angle(float(20)))
    await WheelController.move_wheels_forward_in_straight_line(float(305))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(60))
    await WheelController.move_wheels_towards_element_then_stop_at_marker()
    is_green_detected = await water_if_green_plant()

    if is_green_detected:
        await WheelController.wheel_right_turn()
        await multitask(GripperController.release_element_using_both_arms(),
                        WheelController.move_wheels_backward_in_straight_line(float(500), Speed.Straight))
        await WheelController.move_wheels_backward_in_straight_line(float(150), with_brake=True)
        return

    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(165))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(30))
    await WheelController.move_wheels_towards_element_then_stop_at_marker()

    is_green_detected = await water_if_green_plant()

    if is_green_detected:
        await WheelController.wheel_right_turn()
        await multitask(GripperController.release_element_using_both_arms(),
                        WheelController.move_wheels_backward_in_straight_line(float(600), Speed.Straight))
        await WheelController.move_wheels_backward_in_straight_line(float(150), with_brake=True)
        return

    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(165))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(30))
    await WheelController.move_wheels_towards_element_then_stop_at_marker()

    await water_if_green_plant()
    await WheelController.wheel_right_turn()
    await multitask(GripperController.release_element_using_both_arms(),
                    WheelController.move_wheels_backward_in_straight_line(float(800), Speed.Straight))
    await WheelController.move_wheels_backward_in_straight_line(float(150), with_brake=True)


# 1) example of moving motors straight. e.g. float(1000) is 1 meter which is 1000mm
# 2) when getting vegetable, yung bigat could affect the gyro, so make sure to compute distance
#    via sensing the white color or ibangga sa edge

async def main():
    print("Start, pb version: ", version)
    await water_the_green_plants_and_move_decay_plants()
    await get_the_vegetables()
    await get_the_vegetables_at_the_market()
    # await multitask(get_the_vegetables(), WheelController.debug())
    print("DONE!")

    # ignore below, tester only
    # print("Test simple run")


run_task(main())
