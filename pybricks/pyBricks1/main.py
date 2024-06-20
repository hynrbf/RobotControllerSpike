from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task, multitask


async def old_code():
    await GripperController.reset_left_arm()
    await GripperController.reset_right_arm()
    wheel_to_butt_distance = float(50)
    left_turn_variance_to_left_wheel = float(60)
    right_turn_variance_to_right_wheel = float(60)
    await WheelController.move_wheels_backward_in_straight_line(float(170) - wheel_to_butt_distance, Speed.Medium)

    # get red vegetable and yellow
    await WheelController.move_wheels_forward_in_straight_line(float(40))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(250) + left_turn_variance_to_left_wheel)
    await GripperController.grip_element_using_both_arms()

    # get another set of vegetable
    await WheelController.move_wheels_backward_in_straight_line(float(150))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(140))
    await WheelController.wheel_left_turn()
    await GripperController.release_element_using_both_arms()
    await WheelController.move_wheels_forward_in_straight_line(float(120))
    await GripperController.grip_element_using_both_arms()

    # going long straight
    await WheelController.move_wheels_backward_in_straight_line(float(160))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(1600))
    await WheelController.wheel_slight_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(210))
    await GripperController.reset_left_arm()
    await WheelController.move_wheels_backward_in_straight_line(float(210))
    await WheelController.wheel_slight_left_turn()
    await GripperController.grip_element_using_left_arm()

    # going to red market
    await WheelController.move_wheels_backward_in_straight_line(float(800))
    await WheelController.move_wheels_forward_in_straight_line(float(120))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_backward_in_straight_line(float(600))
    await GripperController.release_element_using_both_arms()

    # go back to starting point
    await WheelController.move_wheels_backward_in_straight_line(float(1600))
    await WheelController.move_wheels_forward_in_straight_line(float(200))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(800))
    await WheelController.wheel_right_turn()

    # reset all controllers
    await GripperController.reset_left_arm()
    await GripperController.reset_right_arm()
    await WheelController.reset_wheels()


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


async def water_the_green_plants():
    await WheelController.move_wheels_forward_in_straight_line(float(50))
    await GripperController.grip_element_using_left_arm()
    await WheelController.wheel_left_turn_with_angle(float(30))
    await WheelController.move_wheels_forward_in_straight_line(float(160))
    await WheelController.wheel_right_turn_with_angle(float(30))
    await WheelController.move_wheels_forward_in_straight_line(float(300))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(60))
    await WheelController.move_wheels_towards_element_then_stop_at_marker()
    await WheelController.move_wheels_backward_in_straight_line(float(30))
    await multitask(GripperController.reset_left_arm(),
                    WheelController.move_wheels_backward_in_straight_line(float(90)))
    await GripperController.grip_element_using_left_arm()
    await WheelController.move_wheels_forward_in_straight_line(float(60))
    await WheelController.move_wheels_towards_element_then_stop_at_marker()
    await WheelController.move_wheels_backward_in_straight_line(float(90))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(160))
    await WheelController.wheel_left_turn()
    await multitask(GripperController.grip_element_using_both_arms(),
                    WheelController.move_wheels_forward_in_straight_line(float(180)))


# 1) example of moving motors straight. e.g. float(1000) is 1 meter which is 1000mm
# 2) when getting vegetable, yung bigat could affect the gyro, so make sure to compute distance
#    via sensing the white color or ibangga sa edge

async def main():
    print("Start, pb version: ", version)
    await water_the_green_plants()
    print("DONE!")

    # ignore below, tester only
    # print("Test simple run")


run_task(main())
