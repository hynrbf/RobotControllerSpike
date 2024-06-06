import runloop


class GrabberController:
    @staticmethod
    def spin_clockwise():
        print('clockwise')

    @staticmethod
    def spin_counter_clockwise():
        print('counter clockwise')


async def main():
    GrabberController.spin_clockwise()
    GrabberController.spin_counter_clockwise()

    # ignore below
    await runloop.sleep_ms(1000)


runloop.run(main())
