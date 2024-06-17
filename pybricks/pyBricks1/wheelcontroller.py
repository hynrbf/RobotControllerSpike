from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Icon, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from colorcontroller import ColorController
from shared import Shared, Speed


class WheelController:
    # I measured manually and the wheel diameter is 5.6cm and the axle distance is 11.7cm float(117)
    # when double wheels wheel diameter is 5.6cm and the axle distance is 17.5cm
    __wheel_diameter_in_mm = float(56)
    __axle_track_in_mm = float(175)

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
        wheel_controller.settings(straight_speed=speed, straight_acceleration=Speed.Fast)
        await wheel_controller.straight(distance_in_mm)

        travelled_distance = WheelController.__get_distance_in_mm()
        print("Travelled distance in mm: ", travelled_distance)

    @staticmethod
    async def move_wheels_backward_in_straight_line(distance_in_mm: float, speed: float = Speed.Fast):
        Shared.hub().display.icon(Icon.ARROW_DOWN)
        distance_in_mm = distance_in_mm * -1
        wheel_controller = WheelController.__object()
        wheel_controller.settings(straight_speed=speed, straight_acceleration=Speed.Fast)
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

    @staticmethod
    async def move_wheels_towards_element_then_stop_at_marker(speed: float = Speed.Slow):
        Shared.hub().display.icon(Icon.ARROW_UP)
        wheel_controller = WheelController.__object()
        wheel_controller.settings(straight_speed=speed, straight_acceleration=Speed.Slow)

        while True:
            if await ColorController.get_mat_color() == Color.RED:
                wheel_controller.drive(speed, 0)
            elif await ColorController.get_mat_color() == Color.BROWN:
                wheel_controller.drive(speed, 0)
            elif await ColorController.get_mat_color() == Color.GREEN:
                wheel_controller.drive(speed, 0)
            elif await ColorController.get_mat_color() == Color.YELLOW:
                wheel_controller.drive(speed, 0)
            elif await ColorController.get_mat_color() == Color.BLUE:
                wheel_controller.drive(speed, 0)
            elif await ColorController.get_mat_color() == Color.WHITE:
                await wheel_controller.straight(float(30))
                wheel_controller.stop()
                break
            elif await ColorController.get_mat_color() == Color.BLACK:
                wheel_controller.stop()
                break
            else:
                wheel_controller.stop()
                break

            await wait(100)

        wheel_controller.stop()

    @staticmethod
    async def move_wheels_towards_water_tower_stop_at_brown_marker(speed: float = Speed.Slow):
        Shared.hub().display.icon(Icon.ARROW_UP)
        wheel_controller = WheelController.__object()
        wheel_controller.settings(straight_speed=speed, straight_acceleration=Speed.Slow)

        while True:
            if await ColorController.get_mat_color() == Color.RED:
                wheel_controller.stop()
                break
            elif await ColorController.get_mat_color() == Color.BROWN:
                wheel_controller.stop()
                break
            elif await ColorController.get_mat_color() == Color.GREEN:
                wheel_controller.drive(speed, 0)
            elif await ColorController.get_mat_color() == Color.YELLOW:
                wheel_controller.drive(speed, 0)
            elif await ColorController.get_mat_color() == Color.BLUE:
                wheel_controller.drive(speed, 0)
            elif await ColorController.get_mat_color() == Color.WHITE:
                wheel_controller.drive(speed, 0)
            elif await ColorController.get_mat_color() == Color.BLACK:
                wheel_controller.drive(speed, 0)
            else:
                wheel_controller.drive(speed, 0)

            await wait(100)

        await wheel_controller.straight(float(20))
        wheel_controller.stop()

    @staticmethod
    async def move_wheels_forward_while_in_white_line(speed: float = Speed.Fast):
        Shared.hub().display.icon(Icon.ARROW_UP)
        wheel_controller = WheelController.__object()
        wheel_controller.settings(straight_speed=speed, straight_acceleration=Speed.Slow)

        while True:
            if await ColorController.get_mat_color() == Color.WHITE:
                wheel_controller.drive(speed, 0)
            else:
                wheel_controller.stop()
                break

            await wait(100)

        wheel_controller.stop()

    @staticmethod
    def __get_distance_in_mm() -> int:
        wheel_controller = WheelController.__object()
        return wheel_controller.distance()

    @staticmethod
    def __object() -> DriveBase:
        return Shared.wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                       WheelController.__wheel_diameter_in_mm,
                                       WheelController.__axle_track_in_mm)
