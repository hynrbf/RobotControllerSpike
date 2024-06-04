from hub import light_matrix
import runloop
from app import display


class DisplayController:
    @staticmethod
    async def display_text():
        await light_matrix.write("Hi Grachi!")
        display.image(4)


async def main():
    await DisplayController.display_text()


runloop.run(main())
