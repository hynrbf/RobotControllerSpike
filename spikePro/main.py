from hub import light_matrix
import runloop
from app import display, sound
import time


class DisplayController:
    @staticmethod
    async def display_text():
        while True:
            # await light_matrix.write("Hi Grachi!")
            sound.play('Bus Door')
            time.sleep_ms(1000)
            # display.image(4)


async def main():
    await DisplayController.display_text()


runloop.run(main())
