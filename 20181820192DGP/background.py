from pico2d import *


class BackGround:
    def __init__(self, stage):
        self.stage1 = load_image('chip\\background\\realBackGround.png')
        self.stage2 = load_image('chip\\background\\backGround3.png')
        self.stage3 = load_image('chip\\background\\backGround4.png')
        self.cur_stage = stage



    def update(self):
        pass

    def late_update(self):
        pass

    def draw(self):
        if self.cur_stage is 1:
            self.stage1.draw(640, 320)
        elif self.cur_stage is 2:
            self.stage2.draw(640, 320)
        elif self.cur_stage is 3:
            self.stage3.draw(640, 320)
