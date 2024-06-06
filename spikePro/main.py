import runloop
import motor
import time
from hub import port


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
        await motor.run_to_absolute_position(port.A, 60, 600, direction=motor.COUNTERCLOCKWISE)
        time.sleep_ms(500)


async def main():
    await GrabberController.reset()
    await GrabberController.spin_counter_clockwise()
    await GrabberController.spin_clockwise()

    # ignore below
    await runloop.sleep_ms(1000)


runloop.run(main())
