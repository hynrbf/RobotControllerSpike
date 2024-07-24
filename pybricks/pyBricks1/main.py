from colorcontroller import ColorController
from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task, multitask, wait


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


async def get_elements_at_greenhouse():
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
    await WheelController.move_wheels_forward_in_straight_line(float(40))
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
    # drop the 2 red vegetables
    await WheelController.wheel_left_turn()
    await WheelController.wheel_right_turn()
    await multitask(GripperController.release_element_using_both_arms(),
                    WheelController.move_wheels_backward_in_straight_line(float(520)))

    # position to get the 2 new vegetables
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_backward_in_straight_line(float(95), with_brake=True)
    await WheelController.move_wheels_forward_in_straight_line(float(250))
    await WheelController.wheel_left_turn()

    # go to the 2 new vegetables
    await WheelController.move_wheels_forward_in_straight_line(float(260))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(50))
    await WheelController.wheel_left_turn_with_angle(20)
    is_red = await ColorController.detect_red_vegetable()
    await WheelController.wheel_right_turn_with_angle(40)
    is_red_again = await ColorController.detect_red_vegetable()
    await WheelController.wheel_left_turn_with_angle(20)
    await WheelController.move_wheels_forward_in_straight_line(float(100), Speed.Slow)
    await GripperController.grip_element_using_both_arms()
    is_go_to_compose_area = True
    print("result ", is_red, is_red_again)

    # both red
    if is_red and is_red_again:
        await WheelController.move_wheels_backward_in_straight_line(float(100))
        await WheelController.wheel_left_turn()
        await WheelController.move_wheels_forward_in_straight_line(float(320))
        await WheelController.wheel_right_turn()
        await multitask(WheelController.move_wheels_forward_in_straight_line(float(150)),
                        GripperController.reset_both_arms())
        await WheelController.move_wheels_backward_in_straight_line(float(250))
        await multitask(WheelController.wheel_left_turn(), GripperController.grip_element_using_both_arms())
        await WheelController.move_wheels_forward_in_straight_line(float(1110), Speed.Straight)
        is_go_to_compose_area = False

    # both yellow
    if not is_red and not is_red_again:
        await WheelController.wheel_u_turn_right()
        await WheelController.move_wheels_backward_in_straight_line(float(105), with_brake=True)
        await WheelController.move_wheels_forward_in_straight_line(float(250))
        await WheelController.wheel_right_turn()
        await WheelController.move_wheels_forward_in_straight_line(float(1430), Speed.Straight)

    # red and yellow
    if is_red and not is_red_again:
        await WheelController.move_wheels_backward_in_straight_line(float(100))
        await WheelController.wheel_left_turn()
        await WheelController.move_wheels_forward_in_straight_line(float(320))
        await WheelController.wheel_right_turn()
        await multitask(WheelController.move_wheels_forward_in_straight_line(float(150)),
                        GripperController.reset_left_arm())
        await WheelController.move_wheels_backward_in_straight_line(float(250))
        await multitask(WheelController.wheel_left_turn(), GripperController.grip_element_using_both_arms())
        await GripperController.reset_right_arm()
        await WheelController.move_wheels_forward_in_straight_line(float(1110), Speed.Straight)

    # yellow and red
    if not is_red and is_red_again:
        await WheelController.move_wheels_backward_in_straight_line(float(100))
        await WheelController.wheel_left_turn()
        await WheelController.move_wheels_forward_in_straight_line(float(320))
        await WheelController.wheel_right_turn()
        await multitask(WheelController.move_wheels_forward_in_straight_line(float(150)),
                        GripperController.reset_right_arm())
        await WheelController.move_wheels_backward_in_straight_line(float(250))
        await multitask(WheelController.wheel_left_turn(), GripperController.grip_element_using_both_arms())
        await WheelController.move_wheels_forward_in_straight_line(float(1110), Speed.Straight)

    # going to center line
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(400))

    if not is_go_to_compose_area:
        await WheelController.wheel_left_turn()
        await multitask(WheelController.move_wheels_backward_in_straight_line(float(265), with_brake=True),
                        GripperController.grip_element_using_both_arms())
        return

    await WheelController.wheel_slight_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(230))
    await multitask(GripperController.release_element_using_both_arms(), WheelController.wheel_slight_right_turn())

    # position wall near compose area
    await WheelController.wheel_slight_left_turn()
    await WheelController.move_wheels_backward_in_straight_line(float(190))
    await WheelController.wheel_slight_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(150))
    await WheelController.wheel_u_turn_right()
    await multitask(WheelController.move_wheels_backward_in_straight_line(float(145), with_brake=True),
                    GripperController.grip_element_using_both_arms())


async def get_the_vegetables():
    # get the 1st red vegetable and yellow
    await WheelController.move_wheels_forward_in_straight_line(float(45))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(220), Speed.Medium)
    await GripperController.grip_element_using_both_arms()

    # get 2nd set of vegetables
    await WheelController.move_wheels_backward_in_straight_line(float(150))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(185))
    await WheelController.wheel_left_turn()
    await multitask(GripperController.release_element_using_both_arms(),
                    WheelController.move_wheels_forward_in_straight_line(float(145), Speed.Slow))
    await GripperController.grip_element_using_both_arms()

    # going long straight to the compose area
    await WheelController.move_wheels_backward_in_straight_line(float(210))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(1055), Speed.Straight)
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(60), Speed.Straight)
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
    await WheelController.move_wheels_forward_in_straight_line(float(500), Speed.Straight)
    await WheelController.wheel_u_turn_right()
    await WheelController.move_wheels_backward_in_straight_line(float(180), with_brake=True)
    await WheelController.move_wheels_forward_in_straight_line(float(60))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_backward_in_straight_line(float(475))


# Alfeo's code
async def water_if_green_plant(count_tries_to_detect_green: int, is_water_plant: bool) -> bool:
    is_green_detected = False

    if await ColorController.detect_green_vegetable():
        # from color detect position 130 forward, move backward 130
        if not is_water_plant:
            await WheelController.move_wheels_backward_in_straight_line(float(130), Speed.Straight)
            is_green_detected = True
            return is_green_detected

        # from color detect position 130 forward. 125 backward, 125 forward, then backward 130
        await WheelController.move_wheels_backward_in_straight_line(float(25), Speed.Straight)
        await multitask(GripperController.reset_left_arm(), GripperController.reset_right_arm(),
                        WheelController.move_wheels_backward_in_straight_line(float(100), Speed.Straight))
        await GripperController.grip_element_using_both_arms()
        await WheelController.move_wheels_forward_in_straight_line(float(125), Speed.Straight)
        await WheelController.move_wheels_backward_in_straight_line(float(130), Speed.Straight)
        is_green_detected = True
    else:
        # from color detect position 130 forward, then 240 backward
        await WheelController.move_wheels_forward_in_straight_line(float(110), Speed.Straight)

        if count_tries_to_detect_green >= 2:
            await multitask(GripperController.reset_left_arm(), GripperController.reset_right_arm(),
                            WheelController.move_wheels_backward_in_straight_line(float(240), Speed.Straight))
        else:
            await WheelController.move_wheels_backward_in_straight_line(float(240), Speed.Straight)

    return is_green_detected


async def water_the_green_plants_and_move_rotten_plants():
    count_tries_to_detect_green = 0
    await WheelController.wheel_left_turn_with_angle(float(20))
    await WheelController.move_wheels_forward_in_straight_line(float(210))
    await multitask(GripperController.grip_element_using_both_arms(),
                    WheelController.wheel_right_turn_with_angle(float(20)))
    is_green_found = False

    # go to 1st green square
    await WheelController.move_wheels_forward_in_straight_line(float(295))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(130))
    is_green = await water_if_green_plant(count_tries_to_detect_green, True)
    count_tries_to_detect_green = count_tries_to_detect_green + 1

    if is_green:
        is_green_found = True

    # go to 2nd green square
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(165), Speed.Straight)
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(130))
    is_green = await water_if_green_plant(count_tries_to_detect_green, not is_green_found)
    count_tries_to_detect_green = count_tries_to_detect_green + 1

    if is_green:
        is_green_found = True

    # go to 3rd green square
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(180), Speed.Straight)
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(130))
    is_green = await water_if_green_plant(count_tries_to_detect_green, not is_green_found)
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
    await wait(2000)
    
    await water_the_green_plants_and_move_rotten_plants()
    await get_the_vegetables()
    await get_the_vegetables_at_the_market()
    await get_elements_at_greenhouse()
    # await multitask(get_the_vegetables(), WheelController.debug())
    print("DONE!")

    # ignore below, tester only
    # print("Test simple run")


run_task(main())
