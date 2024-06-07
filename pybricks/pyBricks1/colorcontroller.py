from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

from shared import Shared


class ColorController:
    __left_sensor = ColorSensor(Port.C)

    @staticmethod
    def get_mat_color():
        hub = Shared.hub()

        while True:
            if ColorController.__left_sensor.color() == Color.RED:
                print("Red")
                hub.display.char("R")
            elif ColorController.__left_sensor.color() == Color.WHITE:
                print("White")
                hub.display.char("W")
            elif ColorController.__left_sensor.color() == Color.BLACK:
                print("Black")
                hub.display.char("B")
            elif ColorController.__left_sensor.color() == Color.GREEN:
                print("Green")
                hub.display.char("G")
            elif ColorController.__left_sensor.color() == Color.YELLOW:
                print("Yellow")
                hub.display.char("Y")
            elif ColorController.__left_sensor.color() == Color.BLUE:
                print("Blue")
                hub.display.char("A")
            else:
                print("Black")
                hub.display.char("B")

            wait(100)

    @staticmethod
    def detect_yellow_vegetable() -> bool:
        print("yellow detected")
        return True

    @staticmethod
    def detect_red_vegetable() -> bool:
        print("red detected")
        return True
