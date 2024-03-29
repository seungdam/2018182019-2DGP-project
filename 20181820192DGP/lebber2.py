from pico2d import *
import game_world

image_sizeW = 32
image_sizeH = 32

object_sizeW = 64
object_sizeH = 64

positionX = [0, 32, 64, 96, 128, 160, 192]
positionY = [0, 32, 64, 96, 128, 160, 192, 224, 256, 288, 320]


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


class Lebber:
    def __init__(self, pos, type):
        self.image = load_image('chip\\tileset\\newTile(7X11).png')
        self.x = pos[0]
        self.y = pos[1]
        self.type = type
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32

        self.collided_Rect_Height = 0
        self.collided_Rect_Width = 0
        self.collided_Rect = [0, 0, 0, 0]

        pass

    def update(self):

        pass

    def get_bb(self):
        return self.x - 32, self.y + 32, self.x + 32, self.y - 32

    def update(self):
        pass

    def late_update(self):
        player = game_world.bring_object(6, 0)
        if intersected_rectangle(self.collided_Rect, self.left, self.top, self.right, self.bottom,
                                 player.left, player.top, player.right, player.bottom):
            player.can_up = True
            if player.falling:
                player.falling = False
        pass

    def draw(self):
        if self.type is 4:
            self.image.clip_draw(positionX[1], positionY[7], 32, 32, self.x, self.y, object_sizeW, object_sizeH)
        elif self.type is 5:
            self.image.clip_draw(positionX[1], positionY[6], 32, 32, self.x, self.y, object_sizeW, object_sizeH)
        elif self.type is 6:
            self.image.clip_draw(positionX[1], positionY[5], 32, 32, self.x, self.y, object_sizeW, object_sizeH)

        pass
