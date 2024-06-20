from grippercontroller import GripperController
from shared import Speed
from wheelcontroller import WheelController
from pybricks import version
from pybricks.tools import run_task


# Notes:
# 1) example of moving motors straight. e.g. float(1000) is 1 meter which is 1000mm
# 2) when getting vegetable, yung bigat could affect the gyro, so make sure to compute distance
#    via sensing the white color or ibangga sa edge

async def main():
    print("Start, pb version: ", version)
    await GripperController.reset_left_arm()
    await GripperController.reset_right_arm()
    wheel_to_butt_distance = float(50)
    left_turn_variance_to_left_wheel = float(60)
    right_turn_variance_to_right_wheel = float(60)
    await WheelController.move_wheels_backward_in_straight_line(float(170) - wheel_to_butt_distance, Speed.Medium)

    # get red vegetable and yellow
    await WheelController.move_wheels_forward_in_straight_line(float(50))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_towards_element(float(250) + left_turn_variance_to_left_wheel)
    await GripperController.grip_element_using_both_arms()

    # get another set of vegetable
    await WheelController.move_wheels_backward_in_straight_line(float(150))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(180))
    await WheelController.wheel_left_turn()
    await GripperController.release_element_using_both_arms()
    await WheelController.move_wheels_towards_element(float(130))
    await GripperController.grip_element_using_both_arms()

    # going long straight
    await WheelController.move_wheels_backward_in_straight_line(float(175))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_backward_in_straight_line(float(600), Speed.Medium)
    await WheelController.move_wheels_backward_in_straight_line(float(600), Speed.Medium)
    await WheelController.move_wheels_backward_in_straight_line(float(470), Speed.Medium)
    await WheelController.wheel_u_turn_right()
    await WheelController.wheel_slight_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(240))
    await GripperController.reset_left_arm()
    await WheelController.move_wheels_backward_in_straight_line(float(430))
    await WheelController.wheel_slight_left_turn()
    await GripperController.grip_element_using_left_arm()

    # going to red market
    await WheelController.move_wheels_backward_in_straight_line(float(550))
    await WheelController.move_wheels_forward_in_straight_line(float(70))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_backward_in_straight_line(float(600))
    await GripperController.release_element_using_both_arms()
    await WheelController.move_wheels_backward_in_straight_line(float(200))
    await WheelController.wheel_left_turn()
    await WheelController.wheel_slight_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(310))
    await WheelController.wheel_slight_left_turn
    await WheelController.move_wheels_forward_in_straight_line(float(210))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(130))
    await GripperController.grip_element_using_both_arms()

    # # reset all controllers
    # await GripperController.reset_left_arm()
    # await GripperController.reset_right_arm()
    # await WheelController.reset_wheels()
    print("DONE!")

    # ignore below, tester only
    # print("Test simple run")


run_task(main())
