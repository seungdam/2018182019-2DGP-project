from pico2d import *
import game_world
import game_framework

image_sizeW = 64
image_sizeH = 64

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Flag:

    def __init__(self, pos):
        self.noFlagImage = load_image('chip\\object\\check_point_noflag.png')
        self.FlagImage = load_image('chip\\object\\check_point.png')
        self.x = pos[0]
        self.y = pos[1]
        self.frame = 0
        self.left = self.x - 10
        self.top = self.y + 32
        self.right = self.x + 10
        self.bottom = self.y - 32
        self.flagOn = False

        pass

    def get_bb(self):
        return self.x - 10, self.y + 32, self.x + 10, self.y - 32

    def update(self):

        player = game_world.bring_object(1, 0)

        if player.objectNum == 10:
            self.flagOn = True

        if self.flagOn:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        else:
            pass
        pass

    def late_update(self):
        if self.flagOn:
            game_framework.quit()
            pass
        pass

    def draw(self):
        if self.flagOn:
            self.FlagImage.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)
        else:
            self.noFlagImage.draw(self.x, self.y)
        #   draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass
