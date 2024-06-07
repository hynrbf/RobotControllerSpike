from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

from shared import Shared


class ColorController:
    __left_sensor = ColorSensor(Port.C)

    @staticmethod
    def get_mat_color():
        while True:
            if ColorController.__left_sensor.color() == Color.RED:
                print("Red")
                Shared.hub().display.char("R")
            elif ColorController.__left_sensor.color() == Color.WHITE:
                print("White")
                Shared.hub().display.char("W")
            elif ColorController.__left_sensor.color() == Color.BLACK:
                print("Black")
                Shared.hub().display.char("B")
            elif ColorController.__left_sensor.color() == Color.GREEN:
                print("Green")
                Shared.hub().display.char("G")
            elif ColorController.__left_sensor.color() == Color.YELLOW:
                print("Yellow")
                Shared.hub().display.char("Y")
            elif ColorController.__left_sensor.color() == Color.BLUE:
                print("Blue")
                Shared.hub().display.char("A")
            else:
                print("Black")
                Shared.hub().display.char("B")

            wait(100)

    @staticmethod
    def detect_yellow_vegetable() -> bool:
        is_detected = False

        while True:
            if ColorController.__left_sensor.color() == Color.YELLOW:
                wait(100)
                Shared.hub().display.char("Y")
                is_detected = True
                break

        return is_detected

    @staticmethod
    def detect_red_vegetable() -> bool:
        is_detected = False

        while True:
            if ColorController.__left_sensor.color() == Color.RED:
                wait(100)
                Shared.hub().display.char("R")
                is_detected = True
                break

        return is_detected
