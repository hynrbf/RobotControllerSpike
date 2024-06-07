import runloop
import motor
import time
import color_sensor
import color
from hub import port
from hub import light_matrix


class GrabberController:
    @staticmethod
    async def reset():
        current_position = motor.absolute_position(port.A)
        print("His current position is: ", current_position)
        await motor.run_to_absolute_position(port.A, 0, 100, direction=motor.SHORTEST_PATH)
        time.sleep_ms(500)

        current_position = motor.absolute_position(port.A)
        print("His current position now: ", current_position)
        time.sleep_ms(500)

    @staticmethod
    async def spin_clockwise():
        await motor.run_to_absolute_position(port.A, 0, 600, direction=motor.CLOCKWISE)
        time.sleep_ms(500)

    @staticmethod
    async def spin_counter_clockwise():
        # the values of position is 0=base, 90, 180, 270, 360 in clockwise fashion
        await motor.run_to_absolute_position(port.A, 180, 600, direction=motor.COUNTERCLOCKWISE)
        time.sleep_ms(500)


class ColorController:
    @staticmethod
    async def get_mat_color(port_to_use: int = port.A):
        while True:
            retrieved_color = color_sensor.color(port_to_use)

            if retrieved_color == color.RED:
                await light_matrix.write('R')
            elif retrieved_color == color.GREEN:
                await light_matrix.write('G')
            elif retrieved_color == color.YELLOW:
                await light_matrix.write('Y')
            elif retrieved_color == color.BLUE:
                await light_matrix.write('A')
            elif retrieved_color == color.BLACK:
                await light_matrix.write('B')
            elif retrieved_color == color.WHITE:
                await light_matrix.write('W')
            else:
                await light_matrix.write('0')

            time.sleep_ms(500)

    @staticmethod
    async def get_element_color():
        print('')


async def main():
    # await GrabberController.reset()
    # await GrabberController.spin_counter_clockwise()
    # await GrabberController.spin_clockwise()
    await ColorController.get_mat_color(port.B)

    # ignore below
    await runloop.sleep_ms(1000)


runloop.run(main())
