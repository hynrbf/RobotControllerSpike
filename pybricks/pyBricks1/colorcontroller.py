from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

from shared import Shared


class ColorController:
    @staticmethod
    def get_mat_color(port_to_use: Port = Port.A):
        sensor = ColorSensor(port_to_use)
        hub = Shared.hub()

        while True:
            if sensor.color() == Color.RED:
                print("Red")
                hub.display.char("R")
            elif sensor.color() == Color.WHITE:
                print("White")
                hub.display.char("W")
            elif sensor.color() == Color.BLACK:
                print("Black")
                hub.display.char("B")
            elif sensor.color() == Color.GREEN:
                print("Green")
                hub.display.char("G")
            elif sensor.color() == Color.YELLOW:
                print("Yellow")
                hub.display.char("Y")
            elif sensor.color() == Color.BLUE:
                print("Blue")
                hub.display.char("A")
            else:
                print("Black")
                hub.display.char("B")

            wait(100)
