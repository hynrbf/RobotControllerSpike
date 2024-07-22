from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task, multitask


async def water_green_plant_only():
    if await ColorController.detect_green_vegetable():
        await WheelController.move_wheels_backward_in_straight_line(float(30))
        await multitask(GripperController.reset_left_arm(),
                        WheelController.move_wheels_backward_in_straight_line(float(100)))
        await GripperController.grip_element_using_left_arm()
        await WheelController.move_wheels_towards_element_then_stop_at_marker()
        await WheelController.move_wheels_backward_in_straight_line(float(110))
    else:
        await WheelController.move_wheels_backward_in_straight_line(float(100))


async def move_rotten_plant() -> bool:
    is_green_detected = False

    if await ColorController.detect_green_vegetable():
        await WheelController.move_wheels_backward_in_straight_line(float(115), Speed.Straight)
        is_green_detected = True
    else:
        await WheelController.move_wheels_forward_in_straight_line(float(110), Speed.Straight)
        await WheelController.move_wheels_backward_in_straight_line(float(225), Speed.Straight)

    return is_green_detected


async def get_water_elements():
    # go to 1st green square
    position_of_green = 0
    await WheelController.move_wheels_forward_in_straight_line(float(450), Speed.Straight)
    await WheelController.wheel_right_turn()
    await multitask(GripperController.grip_element_using_both_arms(),
                    WheelController.move_wheels_forward_in_straight_line(float(115)))

    if await move_rotten_plant():
        position_of_green = 1

    # go to 2nd green square
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(175), Speed.Straight)
    await WheelController.wheel_right_turn()
    await multitask(GripperController.grip_element_using_both_arms(),
                    WheelController.move_wheels_forward_in_straight_line(float(115)))

    if await move_rotten_plant():
        position_of_green = 2

    # go to 3rd green square
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(180), Speed.Straight)
    await WheelController.wheel_right_turn()
    await multitask(GripperController.grip_element_using_both_arms(),
                    WheelController.move_wheels_forward_in_straight_line(float(115)))

    if await move_rotten_plant():
        position_of_green = 3

    # get vegetable in a container and detect color
    await GripperController.grip_element_using_both_arms()
    await WheelController.move_wheels_forward_in_straight_line(float(30))
    await WheelController.wheel_u_turn_right()
    await WheelController.move_wheels_forward_in_straight_line(float(50))
    await GripperController.reset_both_arms()
    await WheelController.wheel_right_turn_with_angle(float(20))
    await WheelController.move_wheels_forward_in_straight_line(float(55))
    is_red = await ColorController.detect_red_vegetable()

    # now grip the element inside container
    await WheelController.move_wheels_backward_in_straight_line(float(50))
    await WheelController.wheel_right_turn_with_angle(float(70))
    await WheelController.move_wheels_forward_in_straight_line(float(100))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(39), with_brake=True)
    await GripperController.grip_element_using_left_arm()
    await WheelController.move_wheels_backward_in_straight_line(float(70))
    await WheelController.wheel_left_turn()

    if is_red:
        await multitask(WheelController.move_wheels_forward_in_straight_line(float(500), Speed.Straight),
                        GripperController.grip_element_using_both_arms())
        await WheelController.wheel_right_turn()
        await WheelController.move_wheels_forward_in_straight_line(float(500), Speed.Straight)
        await WheelController.wheel_u_turn_right()
        await WheelController.move_wheels_backward_in_straight_line(float(240), with_brake=True)
        await WheelController.move_wheels_forward_in_straight_line(float(60))
        await WheelController.wheel_left_turn()
        await WheelController.move_wheels_forward_in_straight_line(float(200))
        await GripperController.reset_both_arms()
        await WheelController.move_wheels_backward_in_straight_line(float(50))
    else:
        await multitask(WheelController.move_wheels_forward_in_straight_line(float(600), Speed.Straight),
                        GripperController.grip_element_using_both_arms())
        await WheelController.wheel_slight_left_turn()
        await WheelController.move_wheels_forward_in_straight_line(float(210))
        await WheelController.wheel_left_turn()
        await WheelController.wheel_right_turn()
        await GripperController.reset_both_arms()
        await WheelController.move_wheels_backward_in_straight_line(float(100))


# Anton's code
async def get_the_vegetables_at_the_market():
    await WheelController.wheel_left_turn_with_angle(float(180))
    await WheelController.wheel_right_turn_with_angle(float(180))
    await multitask(GripperController.release_element_using_both_arms(),
                    WheelController.move_wheels_backward_in_straight_line(float(520)))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_backward_in_straight_line(float(95), with_brake=True)
    await WheelController.move_wheels_forward_in_straight_line(float(60))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(115))
    is_red = await ColorController.detect_red_vegetable()
    is_yellow = await ColorController.detect_yellow_vegetable()
    is_red_got_first = is_red and not is_yellow

    # get first vegetable
    await WheelController.wheel_right_turn_with_angle(float(15))
    await WheelController.move_wheels_forward_in_straight_line(float(65))
    await multitask(GripperController.grip_element_using_left_arm(),
                    WheelController.wheel_left_turn_with_angle(float(30)))
    await WheelController.wheel_right_turn_with_angle(float(15))

    # get 2nd vegetable
    await WheelController.move_wheels_forward_in_straight_line(float(20))
    await WheelController.wheel_left_turn_with_angle(float(20))
    await WheelController.move_wheels_forward_in_straight_line(float(75))
    await GripperController.grip_element_using_right_arm()

    if is_red_got_first:
        await WheelController.wheel_right_turn_with_angle(float(15))
        await WheelController.move_wheels_backward_in_straight_line(float(380))
        await GripperController.reset_left_arm()
        await WheelController.move_wheels_backward_in_straight_line(float(150))
        await WheelController.wheel_right_turn()
        await WheelController.move_wheels_backward_in_straight_line(float(150), with_brake=True)
        await WheelController.move_wheels_forward_in_straight_line(float(200))

        await WheelController.wheel_right_turn()
        await multitask(WheelController.move_wheels_forward_in_straight_line(float(800)),
                        GripperController.grip_element_using_both_arms())
    else:
        await WheelController.wheel_right_turn_with_angle(float(195))
        await multitask(WheelController.move_wheels_forward_in_straight_line(float(380), Speed.Straight),
                        GripperController.reset_right_arm())
        await WheelController.move_wheels_backward_in_straight_line(float(150))
        await WheelController.wheel_left_turn()
        await WheelController.move_wheels_backward_in_straight_line(float(150), with_brake=True)
        await WheelController.move_wheels_forward_in_straight_line(float(200))

        await WheelController.wheel_right_turn()
        await multitask(WheelController.move_wheels_forward_in_straight_line(float(1100)),
                        GripperController.grip_element_using_both_arms())

    # putting in compose area
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(470))
    await WheelController.wheel_slight_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(230))
    await multitask(GripperController.release_element_using_both_arms(), WheelController.wheel_slight_right_turn())

    # postion wall near compose area
    await WheelController.wheel_slight_left_turn()
    await WheelController.move_wheels_backward_in_straight_line(float(230))
    await WheelController.wheel_slight_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(150))
    await WheelController.wheel_u_turn_right()
    await multitask(WheelController.move_wheels_backward_in_straight_line(float(185), with_brake=True),
                    GripperController.grip_element_using_both_arms())


async def get_the_vegetables():
    # get the 1st red vegetable and yellow
    await WheelController.move_wheels_forward_in_straight_line(float(45))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(200), Speed.Medium)
    await GripperController.grip_element_using_both_arms()

    # get 2nd set of vegetables
    await WheelController.move_wheels_backward_in_straight_line(float(150))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(175))
    await WheelController.wheel_left_turn()
    await multitask(GripperController.release_element_using_both_arms(),
                    WheelController.move_wheels_forward_in_straight_line(float(145), float(100)))
    await GripperController.grip_element_using_both_arms()

    # going long straight to the compose area
    await WheelController.move_wheels_backward_in_straight_line(float(195))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(1050), Speed.Straight)
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(30), Speed.Straight)
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(620), Speed.Straight)
    await WheelController.wheel_slight_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(220))
    await multitask(GripperController.reset_left_arm(), WheelController.wheel_slight_right_turn())
    await WheelController.wheel_slight_left_turn()
    await WheelController.move_wheels_backward_in_straight_line(float(400))
    await multitask(WheelController.wheel_right_turn_with_angle(float(135)),
                    GripperController.grip_element_using_left_arm())

    # going to red market
    await WheelController.move_wheels_forward_in_straight_line(float(400), Speed.Straight)
    await WheelController.wheel_u_turn_right()
    await WheelController.move_wheels_backward_in_straight_line(float(280), with_brake=True)
    await WheelController.move_wheels_forward_in_straight_line(float(60))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_backward_in_straight_line(float(475))


# Alfeo's code
async def water_if_green_plant(count_tries_to_detect_green: int) -> bool:
    is_green_detected = False

    if await ColorController.detect_green_vegetable():
        # from color detect position 120 forward. 125 backward, 125 forward, then backward 120
        await WheelController.move_wheels_backward_in_straight_line(float(25), Speed.Straight)
        await multitask(GripperController.reset_left_arm(), GripperController.reset_right_arm(),
                        WheelController.move_wheels_backward_in_straight_line(float(100), Speed.Straight))
        await GripperController.grip_element_using_both_arms()
        await WheelController.move_wheels_forward_in_straight_line(float(125), Speed.Straight)
        await WheelController.move_wheels_backward_in_straight_line(float(120), Speed.Straight)
        is_green_detected = True
    else:
        # from color detect position 110 forward, then 225 backward
        await WheelController.move_wheels_forward_in_straight_line(float(110), Speed.Straight)

        if count_tries_to_detect_green >= 2:
            await multitask(GripperController.reset_left_arm(), GripperController.reset_right_arm(),
                            WheelController.move_wheels_backward_in_straight_line(float(230), Speed.Straight))
        else:
            await WheelController.move_wheels_backward_in_straight_line(float(230), Speed.Straight)

    return is_green_detected


async def water_the_green_plants_and_move_rotten_plants():
    count_tries_to_detect_green = 0
    await WheelController.wheel_left_turn_with_angle(float(20))
    await WheelController.move_wheels_forward_in_straight_line(float(210))
    await multitask(GripperController.grip_element_using_both_arms(),
                    WheelController.wheel_right_turn_with_angle(float(20)))

    # go to 1st green square
    await WheelController.move_wheels_forward_in_straight_line(float(305))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(120))
    await water_if_green_plant(count_tries_to_detect_green)
    count_tries_to_detect_green = count_tries_to_detect_green + 1

    # go to 2nd green square
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(160), Speed.Straight)
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(120))
    await water_if_green_plant(count_tries_to_detect_green)
    count_tries_to_detect_green = count_tries_to_detect_green + 1

    # go to 3rd green square
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(165), Speed.Straight)
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(130))
    await water_if_green_plant(count_tries_to_detect_green)
    count_tries_to_detect_green = count_tries_to_detect_green + 1

    # going to base
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(800), Speed.Straight)
    await WheelController.wheel_u_turn_right()
    await multitask(GripperController.release_element_using_both_arms(),
                    WheelController.move_wheels_backward_in_straight_line(float(150), with_brake=True))


# 1) example of moving motors straight. e.g. float(1000) is 1 meter which is 1000mm
# 2) when getting vegetable, yung bigat could affect the gyro, so make sure to compute distance
#    via sensing the white color or ibangga sa edge


async def main():
    print("Start, pb version: ", version)
    await multitask(GripperController.reset_left_arm(), GripperController.reset_right_arm())

    await water_the_green_plants_and_move_rotten_plants()
    await get_the_vegetables()
    await get_the_vegetables_at_the_market()
    await get_water_elements()
    # await multitask(get_the_vegetables(), WheelController.debug())
    print("DONE!")

    # ignore below, tester only
    # print("Test simple run")


run_task(main())
