from hub import light_matrix
import runloop
import time


class DisplayController:
    @staticmethod
    async def display_text(text: str, sleep_ms: int):
        while True:
            await light_matrix.write(text)
            time.sleep_ms(sleep_ms)


async def main():
    await DisplayController.display_text("lol", 5000)


runloop.run(main())
