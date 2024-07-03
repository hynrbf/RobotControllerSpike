from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Icon, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from colorcontroller import ColorController
from shared import Shared, Speed


class WheelController:
    # I measured manually and the wheel diameter is 5.6cm and the axle distance is 11.7cm float(117)
    # when double wheels wheel diameter is 5.6cm and the axle distance is 17.4cm
    __wheel_diameter_in_mm = float(55)
    __axle_track_in_mm = float(185)

    __left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
    __right_motor = Motor(Port.F)

    @staticmethod
    async def reset_wheels():
        await WheelController.__left_motor.run_target(Speed.Fast, 0)
        await WheelController.__right_motor.run_target(Speed.Fast, 0)
        await wait(100)

        state = WheelController.__object().state()
        print("State of robot is: ", state)

    @staticmethod
    async def move_wheels_forward_in_straight_line(distance_in_mm: float, speed: float = Speed.Fast):
        Shared.hub().display.icon(Icon.ARROW_UP)
        wheel_controller = WheelController.__object()
        # reset to None when moving straight, otherwise the yaw angle becomes not good
        wheel_controller.settings(straight_speed=None, straight_acceleration=None, turn_rate=None,
                                  turn_acceleration=None)
        await wheel_controller.straight(distance_in_mm)

        travelled_distance = WheelController.__get_distance_in_mm()
        print("Travelled distance in mm: ", travelled_distance)

    @staticmethod
    async def move_wheels_backward_in_straight_line(distance_in_mm: float, speed: float = Speed.Fast):
        Shared.hub().display.icon(Icon.ARROW_DOWN)
        distance_in_mm = distance_in_mm * -1
        wheel_controller = WheelController.__object()
        # reset to None when moving straight, otherwise the yaw angle becomes not good
        wheel_controller.settings(straight_speed=None, straight_acceleration=None, turn_rate=None,
                                  turn_acceleration=None)
        await wheel_controller.straight(distance_in_mm)

        travelled_distance = WheelController.__get_distance_in_mm()
        print("Travelled distance in mm: ", travelled_distance)

    @staticmethod
    async def wheel_right_turn():
        Shared.hub().display.icon(Icon.ARROW_RIGHT)
        wheel_controller = WheelController.__object()
        await wheel_controller.turn(90)

    @staticmethod
    async def wheel_right_turn_slowly():
        Shared.hub().display.icon(Icon.ARROW_RIGHT)
        wheel_controller = WheelController.__object()
        wheel_controller.settings(turn_rate=180)
        await wheel_controller.turn(90)

    @staticmethod
    async def wheel_slight_right_turn():
        Shared.hub().display.icon(Icon.ARROW_LEFT)
        wheel_controller = WheelController.__object()
        await wheel_controller.turn(45)

    @staticmethod
    async def wheel_u_turn_right():
        Shared.hub().display.icon(Icon.ARROW_RIGHT)
        wheel_controller = WheelController.__object()
        await wheel_controller.turn(180)

    @staticmethod
    async def wheel_right_turn_with_angle(angle: float = 90):
        if angle < 0:
            angle = angle * -1

        Shared.hub().display.icon(Icon.ARROW_RIGHT)
        wheel_controller = WheelController.__object()
        await wheel_controller.turn(angle)

    @staticmethod
    async def wheel_left_turn():
        Shared.hub().display.icon(Icon.ARROW_LEFT)
        wheel_controller = WheelController.__object()
        await wheel_controller.turn(-90)

    @staticmethod
    async def wheel_left_turn_slowly():
        Shared.hub().display.icon(Icon.ARROW_LEFT)
        wheel_controller = WheelController.__object()
        wheel_controller.settings(turn_rate=180)
        await wheel_controller.turn(-90)

    @staticmethod
    async def wheel_slight_left_turn():
        Shared.hub().display.icon(Icon.ARROW_LEFT)
        wheel_controller = WheelController.__object()
        await wheel_controller.turn(-45)

    @staticmethod
    async def wheel_left_turn_with_angle(angle: float = -90):
        if angle > 0:
            angle = angle * -1

        Shared.hub().display.icon(Icon.ARROW_RIGHT)
        wheel_controller = WheelController.__object()
        await wheel_controller.turn(angle)

    @staticmethod
    async def wheel_u_turn_left():
        Shared.hub().display.icon(Icon.ARROW_RIGHT)
        wheel_controller = WheelController.__object()
        await wheel_controller.turn(-180)

    # when going towards element make sure to slow down when approaching otherwise matumba yung element sa
    # lakas ng impact
    @staticmethod
    async def move_wheels_towards_element(distance_in_mm: float, speed: float = Speed.Fast):
        Shared.hub().display.icon(Icon.ARROW_UP)
        wheel_controller = WheelController.__object()
        wheel_controller.settings(straight_speed=speed, straight_acceleration=Speed.Slow)
        await wheel_controller.straight(distance_in_mm)

        travelled_distance = WheelController.__get_distance_in_mm()
        print("Travelled distance in mm: ", travelled_distance)

    # moving towards element
    @staticmethod
    async def move_wheels_towards_element_then_stop_at_marker():
        Shared.hub().display.icon(Icon.ARROW_UP)
        wheel_controller = WheelController.__object()
        await wheel_controller.straight(float(70))

        while True:
            if await ColorController.detect_white_or_black_mat_color():
                wheel_controller.stop()
                break
            else:
                # you can be fast here otherwise bump the element
                wheel_controller.drive(Speed.Slow, 0)

            await wait(100)

        wheel_controller.stop()

    @staticmethod
    async def move_wheels_towards_water_tower_stop_at_brown_marker():
        Shared.hub().display.icon(Icon.ARROW_UP)
        wheel_controller = WheelController.__object()

        while True:
            if await ColorController.detect_brown_mat_color():
                wheel_controller.stop()
                break
            else:
                # you can be fast here otherwise bump the element
                wheel_controller.drive(Speed.Slow, 0)

            await wait(100)

        await wheel_controller.straight(float(20))
        wheel_controller.stop()

    # debugging while wheels moving
    @staticmethod
    async def debug():
        hub = Shared.hub()

        while True:
            if hub.imu.stationary():
                hub.light.on(Color.BLUE)
            else:
                hub.light.on(Color.GREEN)

            yaw_angle = hub.imu.heading()
            heading_angle = WheelController.__get_heading_angle(yaw_angle)
            hub.display.number(round(yaw_angle))
            print('yaw_angle= ', "{:.1f}".format(yaw_angle), 'heading_angle= ', "{:.1f}".format(heading_angle))
            await wait(25)

            # # You can easily reset the heading to arbitrary values.
            # # No special wait operations are required here. Just reset and go.
            # if hub.buttons.pressed():
            #     hub.imu.reset_heading(0)

    @staticmethod
    def __get_heading_angle(yaw_angle):
        if yaw_angle <= 0:
            heading_angle = (-yaw_angle % 360)
        else:
            heading_angle = 360 - (yaw_angle % 360)

        return heading_angle

    @staticmethod
    def __get_distance_in_mm() -> int:
        wheel_controller = WheelController.__object()
        return wheel_controller.distance()

    @staticmethod
    def __object() -> DriveBase:
        return Shared.wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                       WheelController.__wheel_diameter_in_mm,
                                       WheelController.__axle_track_in_mm)
