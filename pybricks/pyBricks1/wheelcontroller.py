from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
from pybricks.pupdevices import ForceSensor

from shared import Shared


class WheelController:
    __left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
    __right_motor = Motor(Port.F)
    __button = ForceSensor(Port.A)

    @staticmethod
    def move_forward_left_motor():
        WheelController.__left_motor.run(500)
        wait(1500)

    @staticmethod
    def move_backward_left_motor():
        print("backward")

    @staticmethod
    def move_forward_right_motor():
        WheelController.__right_motor.run(500)
        wait(1500)

    @staticmethod
    def move_backward_right_motor():
        print("backward")

    @staticmethod
    def move_forward_both_motors():
        while True:
            if WheelController.__button.touched():
                WheelController.__left_motor.stop()
                WheelController.__right_motor.stop()
                print("Button is touched, motors stopped.")
                break
            else:
                WheelController.__left_motor.run(-500)
                WheelController.__right_motor.run(500)
                print("Motors running forward.")
            wait(100)

    @staticmethod
    def move_wheel_in_straight_line(distance_in_mm: int):
        # I measured manually and the wheel diameter is 5.6cm and the axle distance is 11.7cm
        wheel_diameter_in_mm = 56
        axle_track_in_mm = 56
        wheel_controller = Shared.get_wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                                       wheel_diameter_in_mm,
                                                       axle_track_in_mm)
        wheel_controller.straight(distance_in_mm)

        # # Turn around clockwise by 180 degrees.
        # WheelController.__drive_base.turn(90)
        #
        # # Drive forward again to get back to the start.
        # WheelController.__drive_base.straight(500)
        #
        # # Turn around counterclockwise.
        # WheelController.__drive_base.turn(-90)

    @staticmethod
    def check_when_button_pressed():
        while True:
            res = WheelController.__button.touched()
            print("is touched: ", res)
            wait(500)
