0. ToDo coach tito
calibrate the getting the 2 sets of veg in Karen mat
calibrate the getting the 2 veg in red market as well if is_red_got_first

1. source https://spike.legoeducation.com/essential/help/lls-help-python

2. https://www.youtube.com/watch?v=C05-aLtvSLI&list=PLj_k_RHuTqaUlBoR-8AemA2PeXgZLVBZG

3. sensors spike
https://education.lego.com/en-us/product-resources/spike-prime/downloads/technical-specifications/

4. version of pybricks we use
https://beta.pybricks.com/

5. removed code
# moving wheels while tracing the white and black line
@staticmethod
async def move_wheels_forward_while_in_white_line(speed: float = Speed.Fast):
    Shared.hub().display.icon(Icon.ARROW_UP)
    wheel_controller = WheelController.__object()
    # reset to None when moving straight, otherwise the yaw angle becomes not good
    wheel_controller.settings(straight_speed=None, straight_acceleration=None, turn_rate=None,
                              turn_acceleration=None)

    while True:
        if await ColorController.get_mat_color() == Color.RED:
            wheel_controller.stop()
            break
        elif await ColorController.get_mat_color() == Color.BROWN:
            wheel_controller.stop()
            break
        elif await ColorController.get_mat_color() == Color.GREEN:
            wheel_controller.stop()
            break
        elif await ColorController.get_mat_color() == Color.YELLOW:
            wheel_controller.stop()
            break
        elif await ColorController.get_mat_color() == Color.BLUE:
            wheel_controller.stop()
            break
        elif await ColorController.get_mat_color() == Color.WHITE:
            wheel_controller.drive(speed, 0)
        elif await ColorController.get_mat_color() == Color.BLACK:
            wheel_controller.drive(speed, 0)
        else:
            wheel_controller.drive(speed, 0)

        await wait(100)

    wheel_controller.stop()

@staticmethod
async def move_wheels_backward_while_in_white_line(speed: float = Speed.Fast):
    Shared.hub().display.icon(Icon.ARROW_UP)
    wheel_controller = WheelController.__object()
    # reset to None when moving straight, otherwise the yaw angle becomes not good
    wheel_controller.settings(straight_speed=None, straight_acceleration=None, turn_rate=None,
                              turn_acceleration=None)

    while True:
        if await ColorController.get_mat_color() == Color.RED:
            wheel_controller.stop()
            break
        elif await ColorController.get_mat_color() == Color.BROWN:
            wheel_controller.stop()
            break
        elif await ColorController.get_mat_color() == Color.GREEN:
            wheel_controller.stop()
            break
        elif await ColorController.get_mat_color() == Color.YELLOW:
            wheel_controller.stop()
            break
        elif await ColorController.get_mat_color() == Color.BLUE:
            wheel_controller.stop()
            break
        elif await ColorController.get_mat_color() == Color.WHITE:
            wheel_controller.drive(speed * -1, 0)
        elif await ColorController.get_mat_color() == Color.BLACK:
            wheel_controller.drive(speed * -1, 0)
        else:
            wheel_controller.drive(speed * -1, 0)

        await wait(100)

    wheel_controller.stop()
