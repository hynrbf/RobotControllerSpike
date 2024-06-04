from hub import light_matrix
import runloop
import time


class DisplayController:
    @staticmethod
    def display_text(text: str, sleep_ms: int):
        light_matrix.write(text)
        time.sleep_ms(sleep_ms)
        light_matrix.clear()


async def main():
    DisplayController.display_text("A", 5000)


runloop.run(main())
