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
        count = 1
        is_detected = False

        while True:
            if count > 3:
                is_detected = False
                break

            color = await ColorController.__front_sensor.hsv()
            color_int = color.h
            print("Color detected: ", color_int)

            if 40 <= color_int <= 65:
                Shared.hub().display.char("R")
                is_detected = True
                break

            count = count + 1
            await wait(100)

        return is_detected

    @staticmethod
    async def detect_red_vegetable() -> bool:
        count = 1
        is_detected = False

        while True:
            if count > 3:
                is_detected = False
                break

            color = await ColorController.__front_sensor.hsv()
            color_int = color.h
            print("Color detected: ", color_int)

            if 340 <= color_int <= 360:
                Shared.hub().display.char("R")
                is_detected = True
                break

            count = count + 1
            await wait(100)

        return is_detected

    @staticmethod
    async def detect_green_vegetable() -> bool:
        count = 1
        is_detected = False

        while True:
            if count > 3:
                is_detected = False
                break

            color = await ColorController.__front_sensor.hsv()
            color_int = color.h
            print("Color detected: ", color_int)

            # tested and found out green always at Color(h=156, s=78, v=64), so we be safe at 100 - 165
            if 110 <= color_int <= 165:
                Shared.hub().display.char("G")
                is_detected = True
                break

            count = count + 1
            await wait(100)

        return is_detected
