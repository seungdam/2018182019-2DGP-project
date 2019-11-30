from pico2d import *
import game_world
import game_framework


image_sizeW = 64
image_sizeH = 64

object_sizeW = 32
object_sizeH = 32

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

def intersected_rectangle(collided_Rect, rect1_left, rect1_top, rect1_right, rect1_bottom,
                          rect2_left, rect2_top, rect2_right, rect2_bottom):
    vertical = False
    horizontal = False

    if rect1_left <= rect2_right and rect1_right >= rect2_left:
        horizontal = True
        collided_Rect[0] = max(rect1_left, rect2_left)
        collided_Rect[2] = min(rect1_right, rect2_right)

    if rect1_top >= rect2_bottom and rect1_bottom <= rect2_top:
        vertical = True
        collided_Rect[1] = min(rect1_top, rect2_top)
        collided_Rect[3] = max(rect1_bottom, rect2_bottom)

    if vertical and horizontal:
        return True
    else:
        return False


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
        self.collided_Rect_Height = 0
        self.collided_Rect_Width = 0
        self.collided_Rect = [0, 0, 0, 0]
        self.flagOn = False
        self.end = False
        pass

    def get_bb(self):
        return self.x - 10, self.y + 32, self.x + 10, self.y - 32

    def update(self):
        objects = game_world.bring_objects(5)
        count = 0
        player = game_world.bring_object(1, 0)
        for i in objects:
            count += 1
        if player.objectNum is count:
            self.flagOn = True
        if intersected_rectangle(self.collided_Rect, self.left, self.top, self.right, self.bottom,
                                 player.left, player.top, player.right, player.bottom):
            if self.flagOn:
                self.end = True

        if self.flagOn:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        else:
            pass
        pass

    def late_update(self):

        pass

    def draw(self):
        if self.flagOn:
            self.FlagImage.clip_draw(int(self.frame) * image_sizeW, 0, object_sizeW, object_sizeH, self.x, self.y)
        else:
            self.noFlagImage.draw(self.x, self.y)
        #   draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass
