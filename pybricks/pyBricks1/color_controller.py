from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait


class ColorController:
    @staticmethod
    def get_mat_color():
        sensor = ColorSensor(Port.A)

        while True:
            if sensor.color() == Color.RED:
                print("Red")
            elif sensor.color() == Color.WHITE:
                print("White")
            elif sensor.color() == Color.BLACK:
                print("Black")
            else:
                print("NA")

            wait(100)
