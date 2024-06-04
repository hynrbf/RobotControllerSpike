from hub import light_matrix
import runloop
from app import display, sound
import time


class DisplayController:
    @staticmethod
    async def display_text(text: str, sleep_ms: int):
        while True:
            await light_matrix.write(text)
            sound.play('Bus Door')
            time.sleep_ms(sleep_ms)


async def main():
    await DisplayController.display_text("R", 5000)


runloop.run(main())
