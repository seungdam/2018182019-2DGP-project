from pico2d import *
import game_world
import random

IMAGE_WIDTH, IMAGE_HEIGHT = 32, 32

positionX = [0]
positionY = [0, 48, 96]

image_sizeW = 48
image_sizeH = 48

object_sizeW = 64
object_sizeH = 64

object_sizeW2 = 32
object_sizeH2 = 32

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


image_sizeW = 48
image_sizeH = 48

object_sizeW = 64
object_sizeH = 64

colW = 32
colH = 32
RUN, IDLE, STUN = range(3)


class CrushBlock:
    def __init__(self, pos):
        self.image = load_image('chip\\tileset\\newTile5.png')
        self.x = pos[0]
        self.y = pos[1]
        self.restore = 1000

        self.left = self.x - object_sizeW
        self.top = self.y + object_sizeW
        self.right = self.x + object_sizeW
        self.bottom = self.y - object_sizeW

        self.camera1_left = self.x - object_sizeW
        self.camera1_top = self.y + object_sizeW
        self.camera1_right = self.x + object_sizeW
        self.camera1_bottom = self.y - object_sizeW

        self.camera2_left = self.x - object_sizeW
        self.camera2_top = self.y + object_sizeW
        self.camera2_right = self.x + object_sizeW
        self.camera2_bottom = self.y - object_sizeW

        self.camera3_left = self.x - object_sizeW
        self.camera3_top = self.y + object_sizeW
        self.camera3_right = self.x + object_sizeW
        self.camera3_bottom = self.y - object_sizeW


        self.collided_Rect_Height = 0
        self.collided_Rect_Width = 0
        self.collided_Rect = [0, 0, 0, 0]

        self.fill = True

        pass

    def update(self):

        player = game_world.bring_object(1, 0)

        if self.left - 42 <= player.x <= self.left and self.top <= player.y <= self.top + 32 and player.do_right_action:  # 플레이어 -> 블록
            self.fill = False
        if self.right + 42 >= player.x >= self.right and self.top <= player.y <= self.top + 32 and player.do_left_action:  # 블록 <- 플레이어
            self.fill = False

        if not self.fill:
            self.restore -= 1
            if self.restore == 0:
                self.fill = True
                self.restore = 1000
        pass
    def late_update(self):
        player = game_world.bring_object(1, 0)

        if self.fill:
            if intersected_rectangle(self.collided_Rect, self.left, self.top, self.right, self.bottom,
                                     player.left, player.top, player.right, player.bottom):
                self.collided_Rect_Height = self.collided_Rect[1] - self.collided_Rect[3]
                self.collided_Rect_Width = self.collided_Rect[2] - self.collided_Rect[0]

                if self.collided_Rect_Width > self.collided_Rect_Height:
                    if self.collided_Rect[1] == self.y + colW:
                        player.falling = False
                        player.y += self.collided_Rect_Height
                    elif self.collided_Rect[3] == self.y - colW:
                        player.y -= self.collided_Rect_Height
                        player.y -= 1
                else:
                    if self.collided_Rect[0] == self.x - 16:
                        player.x -= self.collided_Rect_Width
                    elif self.collided_Rect[2] == self.x + 16:
                        player.x += self.collided_Rect_Width



    def draw(self):
        if self.fill:
            self.image.clip_draw(positionX[0], positionY[0], image_sizeW, image_sizeH, self.x, self.y, object_sizeW, object_sizeH)
