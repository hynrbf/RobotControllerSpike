import runloop
import motor
import time
from hub import port


class GrabberController:
    @staticmethod
    def reset():
        current_position = motor.absolute_position(port.A)
        print("His current position is: ", current_position)
        motor.run_to_absolute_position(port.A, 0, 100, direction=motor.SHORTEST_PATH)

        time.sleep_ms(500)

        current_position = motor.absolute_position(port.A)
        print("His current position now: ", current_position)

    @staticmethod
    def spin_clockwise():
        print('clockwise')
        current_position = motor.absolute_position(port.A)
        print(current_position)

    @staticmethod
    def spin_counter_clockwise():
        print('counter clockwise')


async def main():
    GrabberController.reset()
    # GrabberController.spin_clockwise()
    # GrabberController.spin_counter_clockwise()

    # ignore below
    await runloop.sleep_ms(1000)


runloop.run(main())
