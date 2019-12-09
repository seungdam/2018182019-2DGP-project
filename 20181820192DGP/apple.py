from pico2d import *
import game_framework
import game_world

image_sizeW = 32
image_sizeH = 32

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


class Apple:
    global player
    image = None

    def __init__(self, pos):
        if Apple.image is None:
            self.image = load_image('chip\\object\\Apple.png')
        self.x = pos[0]
        self.y = pos[1]
        self.frame = 0
        self.exist = True

        self.left = self.x - 10
        self.top = self.y + 10
        self.right = self.x + 10
        self.bottom = self.y - 10

        self.collided_Rect_Height = 0
        self.collided_Rect_Width = 0
        self.collided_Rect = [0, 0, 0, 0]
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 17
        pass

    def late_update(self):
        player = game_world.bring_object(6, 0)
        if intersected_rectangle(self.collided_Rect, self.left, self.top, self.right,
                                 self.bottom, player.left, player.top, player.right, player.bottom):
            if self.exist:
                player.objectNum += 1
                self.exist = False

    def draw(self):
        if self.exist:
            self.image.clip_draw(int(self.frame) * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)

        pass
