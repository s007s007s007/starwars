import arcade
import random

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 900
SCREEN_TITLE = "kNIGGA"


class OKKOiliOKNO(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("background.jpg")

    def spawn(self):
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)

    def update(self, delta_time: float):
        pass


window = OKKOiliOKNO(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
arcade.run()
