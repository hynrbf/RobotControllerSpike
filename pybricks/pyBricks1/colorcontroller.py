from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

from shared import Shared


class ColorController:
    __front_sensor = ColorSensor(Port.C)
    __mat_sensor = ColorSensor(Port.D)

    @staticmethod
    async def get_element_color() -> Color:
        color = await ColorController.__front_sensor.color()
        print("Color: ", color)
        return color

    @staticmethod
    async def get_mat_color() -> Color:
        color = await ColorController.__mat_sensor.color()
        print("Color: ", color)
        return color

    @staticmethod
    async def detect_yellow_vegetable() -> bool:
        is_detected = False

        while True:
            if await ColorController.__front_sensor.color() == Color.YELLOW:
                await wait(100)
                Shared.hub().display.char("Y")
                is_detected = True
                break

        return is_detected

    @staticmethod
    async def detect_red_vegetable() -> bool:
        is_detected = False

        while True:
            if await ColorController.__front_sensor.color() == Color.RED:
                await wait(100)
                Shared.hub().display.char("R")
                is_detected = True
                break

        return is_detected
