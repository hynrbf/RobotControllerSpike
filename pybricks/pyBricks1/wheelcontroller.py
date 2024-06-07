from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.pupdevices import ForceSensor


class WheelController:
    __left_motor = Motor(Port.E)
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
    def check_when_button_pressed():
        while True:
            res = WheelController.__button.touched()
            print("is touched: ", res)
            wait(500)
