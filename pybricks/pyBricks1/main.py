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
    # await GripperController.grip_element_using_left_arm()
    # await GripperController.reset_left_arm()
   # await GripperController.grip_element_using_right_arm()
   # await GripperController.reset_right_arm()
    #await GripperController.grip_element_using_both_arms()
    # await GripperController.release_element_using_both_arms()
    # await WheelController.move_wheels_forward_in_straight_line(float(1000))
    wheel_to_butt_distance = float(50)
    await WheelController.move_wheels_backward_in_straight_line(float(180) - wheel_to_butt_distance)
    
    # get vegatables
    await WheelController.move_wheels_forward_in_straight_line(float(40))
    await WheelController.wheel_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(300))
    await GripperController.grip_element_using_both_arms()

    # get 2nd vegatables
    await WheelController.move_wheels_backward_in_straight_line(float(150))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(170))
    await WheelController.wheel_left_turn()
    await GripperController.release_element_using_both_arms()
    await WheelController.move_wheels_forward_in_straight_line(float(135))
    await GripperController.grip_element_using_both_arms()

    # going to compose area
    await WheelController.move_wheels_backward_in_straight_line(float(200))
    await WheelController.wheel_right_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(1670))
    await WheelController.wheel_slight_left_turn()
    await WheelController.move_wheels_forward_in_straight_line(float(150))
    await GripperController.reset_left_arm
   
    # ignore below, tester only
    # print("Test simple run")


run_task(main())
