from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

from shared import Shared


class ColorController:
    __front_sensor = ColorSensor(Port.C)
    __mat_sensor = ColorSensor(Port.D)

    @staticmethod
    def get_element_color():
        while True:
            if ColorController.__front_sensor.color() == Color.RED:
                print("Red")
            elif ColorController.__front_sensor.color() == Color.WHITE:
                print("White")
            elif ColorController.__front_sensor.color() == Color.GREEN:
                print("Green")
            elif ColorController.__front_sensor.color() == Color.YELLOW:
                print("Yellow")
            elif ColorController.__front_sensor.color() == Color.BLUE:
                print("Blue")
            elif ColorController.__front_sensor.color() == Color.BLACK:
                print("Black")
            else:
                print("Black")

            wait(100)

    @staticmethod
    def get_mat_color():
        while True:
            if ColorController.__mat_sensor.color() == Color.RED:
                print("Red")
            elif ColorController.__mat_sensor.color() == Color.WHITE:
                print("White")
            elif ColorController.__mat_sensor.color() == Color.GREEN:
                print("Green")
            elif ColorController.__mat_sensor.color() == Color.YELLOW:
                print("Yellow")
            elif ColorController.__mat_sensor.color() == Color.BLUE:
                print("Blue")
            elif ColorController.__mat_sensor.color() == Color.BLACK:
                print("Black")
            else:
                print("Black")

            wait(100)

    @staticmethod
    def detect_yellow_vegetable() -> bool:
        is_detected = False

        while True:
            if ColorController.__front_sensor.color() == Color.YELLOW:
                wait(100)
                Shared.hub().display.char("Y")
                is_detected = True
                break

        return is_detected

    @staticmethod
    def detect_red_vegetable() -> bool:
        is_detected = False

        while True:
            if ColorController.__front_sensor.color() == Color.RED:
                wait(100)
                Shared.hub().display.char("R")
                is_detected = True
                break

        return is_detected
