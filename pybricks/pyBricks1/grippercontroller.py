from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from shared import Shared, Speed


class HandPosition:
    Release = 0
    Grip = 1


class GripperController:
    __right_motor = Motor(Port.B)
    __left_motor = Motor(Port.A)
    __right_motor_position = HandPosition.Release
    __left_motor_position = HandPosition.Release
    __both_motors = DriveBase(__left_motor, __right_motor, 56, 60)
    __grip_turn_angle = 90

    @staticmethod
    async def reset_both_arms():
        await GripperController.reset_right_arm()
        await GripperController.reset_left_arm()

    @staticmethod
    async def reset_right_arm():
        Shared.hub().display.icon(Icon.EMPTY)
        GripperController.__get_right_arm_angle()
        await wait(100)

        await GripperController.__right_motor.run_target(500, 0)
        GripperController.__right_motor_position = HandPosition.Release
        await wait(100)

        print("Right hand pos: ", GripperController.__right_motor_position)
        GripperController.__get_right_arm_angle()

    @staticmethod
    async def reset_left_arm():
        Shared.hub().display.icon(Icon.EMPTY)
        GripperController.__get_left_arm_angle()
        await wait(100)

        await GripperController.__left_motor.run_target(500, 0)
        GripperController.__left_motor_position = HandPosition.Release
        await wait(100)

        print("Left hand pos: ", GripperController.__right_motor_position)
        GripperController.__get_left_arm_angle()

    @staticmethod
    async def grip_element_using_right_arm():
        if GripperController.__right_motor_position == HandPosition.Grip:
            return

        await GripperController.__right_motor.run_angle(500, -GripperController.__grip_turn_angle, wait=True)
        GripperController.__right_motor_position = HandPosition.Grip
        Shared.hub().display.icon(Icon.SAD)
        await wait(500)

        GripperController.__get_right_arm_angle()

    @staticmethod
    async def grip_element_using_left_arm():
        if GripperController.__left_motor_position == HandPosition.Grip:
            return

        await GripperController.__left_motor.run_angle(500, GripperController.__grip_turn_angle, wait=True)
        GripperController.__left_motor_position = HandPosition.Grip
        Shared.hub().display.icon(Icon.SAD)
        await wait(500)

        GripperController.__get_left_arm_angle()

    @staticmethod
    async def grip_element_using_both_arms():
        if GripperController.__right_motor_position == HandPosition.Grip and GripperController.__left_motor_position == HandPosition.Grip:
            return
        elif GripperController.__right_motor_position == HandPosition.Grip and GripperController.__left_motor_position == HandPosition.Release:
            await GripperController.grip_element_using_left_arm()
            return
        elif GripperController.__right_motor_position == HandPosition.Release and GripperController.__left_motor_position == HandPosition.Grip:
            await GripperController.grip_element_using_right_arm()
            return

        await GripperController.__both_motors.turn(GripperController.__grip_turn_angle)
        GripperController.__right_motor_position = HandPosition.Grip
        GripperController.__left_motor_position = HandPosition.Grip
        print("Right hand pos: ", GripperController.__right_motor_position)
        print("Left hand pos: ", GripperController.__left_motor_position)
        Shared.hub().display.icon(Icon.SAD)
        await wait(500)

    @staticmethod
    async def release_element_using_both_arms():
        if GripperController.__right_motor_position == HandPosition.Release and GripperController.__left_motor_position == HandPosition.Release:
            return
        elif GripperController.__right_motor_position == HandPosition.Release and GripperController.__left_motor_position == HandPosition.Grip:
            await GripperController.reset_left_arm()
            return
        elif GripperController.__right_motor_position == HandPosition.Grip and GripperController.__left_motor_position == HandPosition.Release:
            await GripperController.reset_right_arm()
            return

        await GripperController.__both_motors.turn(-GripperController.__grip_turn_angle)
        GripperController.__right_motor_position = HandPosition.Release
        GripperController.__left_motor_position = HandPosition.Release
        print("Right hand pos: ", GripperController.__right_motor_position)
        print("Left hand pos: ", GripperController.__left_motor_position)
        Shared.hub().display.icon(Icon.SAD)
        await wait(500)

    @staticmethod
    async def hook_element_downwards(speed: float = Speed.Fast, angle: int = 45):
        await GripperController.__left_motor.run_angle(speed, angle, wait=True)
        await wait(500)

        GripperController.__get_left_arm_angle()

    @staticmethod
    async def hook_element_upwards(speed: float = Speed.Fast, angle: int = 45):
        angle = angle * -1
        await GripperController.__left_motor.run_angle(speed, angle, wait=True)
        await wait(500)

        GripperController.__get_left_arm_angle()

    @staticmethod
    async def hook_element_using_left_arm():
        await GripperController.__left_motor.run_angle(500, 45, wait=True)
        await wait(500)

        GripperController.__get_left_arm_angle()

    @staticmethod
    def __get_right_arm_angle() -> int:
        current_angle = GripperController.__right_motor.angle()
        print("right arm current angle", current_angle)
        return current_angle

    @staticmethod
    def __get_left_arm_angle() -> int:
        current_angle = GripperController.__left_motor.angle()
        print("left arm current angle", current_angle)
        return current_angle
