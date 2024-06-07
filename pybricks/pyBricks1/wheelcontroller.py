from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait


class WheelController:
    __left_motor = Motor(Port.F)

    @staticmethod
    def move_forward_left_motor():
        WheelController.__left_motor.run(500)
        wait(1500)

    @staticmethod
    def move_backward():
        print("backward")
