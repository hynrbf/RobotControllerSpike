import motor
import runloop


class MotorController:
    @staticmethod
    async def move_forward():
        motor.run(1, 1000)


async def main():
    await MotorController.move_forward()


runloop.run(main())
