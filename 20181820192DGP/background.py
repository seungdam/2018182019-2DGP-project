from pico2d import *


class BackGround:
    def __init__(self):
        self.image = load_image('chip\\background\\realBackGround.png')

    def get_bb(self):
        return 0, 0, 1600 - 1, 50

    def update(self):
        pass

    def late_update(self):
        pass

    def draw(self):
        self.image.draw(640, 320)


