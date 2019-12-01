from pico2d import *
import game_world

positionX = [0]
positionY = [0, 48, 96]

image_sizeW = 48
image_sizeH = 48

object_sizeW = 64
object_sizeH = 64

colW = 32
colH = 32


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


class FlourBlock:
    image = None

    def __init__(self, pos, type):
        if FlourBlock.image is None:
            self.image = load_image('chip\\tileset\\newTile5.png')
        self.x = pos[0]
        self.y = pos[1]
        self.type = type
        self.left = self.x - colW
        self.top = self.y + colH
        self.right = self.x + colW
        self.bottom = self.y - colH

        self.collided_Rect_Height = 0
        self.collided_Rect_Width = 0
        self.collided_Rect = [0, 0, 0, 0]

        # --------- 플레이어 객체 정보 ---------

        # -----------------------------------------
        pass

    def get_bb(self):
        return self.x - colW, self.y + colH, self.x + colW, self.y - colH
    def update(self):
        pass
    def late_update(self):
        player = game_world.bring_object(1, 0)

        if intersected_rectangle(self.collided_Rect, self.left, self.top, self.right, self.bottom,
                                 player.left, player.top, player.right, player.bottom):
            self.collided_Rect_Height = self.collided_Rect[1] - self.collided_Rect[3]
            self.collided_Rect_Width = self.collided_Rect[2] - self.collided_Rect[0]

            if self.collided_Rect_Width > self.collided_Rect_Height:

                if self.collided_Rect[1] == self.y + colH:
                    player.falling = False
                    player.y += self.collided_Rect_Height
                elif self.collided_Rect[3] == self.y - colH:
                    player.y -= self.collided_Rect_Height
                    player.y -= 1
            else:
                if self.collided_Rect[0] == self.x - colW:
                    player.x -= self.collided_Rect_Width
                elif self.collided_Rect[2] == self.x + colW:
                    player.x += self.collided_Rect_Width
        pass

    def draw(self):
        # if self.type is 1:
        #     self.image.clip_draw(positionX[0], positionY[8], 32, 32, self.x, self.y, object_sizeW, object_sizeH)
        # elif self.type is 2:
        #     self.image.clip_draw(positionX[1], positionY[8], 32, 32, self.x, self.y, object_sizeW, object_sizeH)
        # elif self.type is 3:
        #     self.image.clip_draw(positionX[2], positionY[8], 32, 32, self.x, self.y, object_sizeW, object_sizeH)
        # elif self.type is 4:
        #     self.image.clip_draw(positionX[0], positionY[7], 32, 32, self.x, self.y, object_sizeW, object_sizeH)
        # elif self.type is 5:
        #     self.image.clip_draw(positionX[1], positionY[7], 32, 32, self.x, self.y, object_sizeW, object_sizeH)
        # elif self.type is 6:
        #     self.image.clip_draw(positionX[2], positionY[7], 32, 32, self.x, self.y, object_sizeW, object_sizeH)
        # elif self.type is 7:
        #     self.image.clip_draw(positionX[0], positionY[6], 32, 32, self.x, self.y, object_sizeW, object_sizeH)
        # elif self.type is 8:
        #     self.image.clip_draw(positionX[1], positionY[6], 32, 32, self.x, self.y, object_sizeW, object_sizeH)
        # elif self.type is 9:
        #     self.image.clip_draw(positionX[2], positionY[6], 32, 32, self.x, self.y, object_sizeW, object_sizeH)
        # elif self.type is -1:
        #     self.image.clip_draw(positionX[0], positionY[5], 32, 32, self.x, self.y, object_sizeW, object_sizeH)
        # elif self.type is -2:
        #     self.image.clip_draw(positionX[1], positionY[5], 32, 32, self.x, self.y,  object_sizeW, object_sizeH)
        # elif self.type is -3:
        #     self.image.clip_draw(positionX[2], positionY[5], 32, 32, self.x, self.y,  object_sizeW, object_sizeH)
        # elif self.type is -4:
        #     self.image.clip_draw(positionX[0], positionY[4], 32, 32, self.x, self.y,  object_sizeW, object_sizeH)
        # elif self.type is -5:
        #     self.image.clip_draw(positionX[1], positionY[4], 32, 32, self.x, self.y,  object_sizeW, object_sizeH)
        # elif self.type is -6:
        #     self.image.clip_draw(positionX[2], positionY[4], 32, 32, self.x, self.y,  object_sizeW, object_sizeH)
        # elif self.type is -7:
        #     self.image.clip_draw(positionX[0], positionY[3], 32, 32, self.x, self.y,  object_sizeW, object_sizeH)
        # elif self.type is -8:
        #     self.image.clip_draw(positionX[1], positionY[3], 32, 32, self.x, self.y,  object_sizeW, object_sizeH)
        # elif self.type is -9:
        #     self.image.clip_draw(positionX[2], positionY[3], 32, 32, self.x, self.y,  object_sizeW, object_sizeH)
        # elif self.type is 10:
        #     self.image.clip_draw(positionX[3], positionY[2], 32, 32, self.x, self.y,  object_sizeW, object_sizeH)
        # elif self.type is 11:
        #     self.image.clip_draw(positionX[3], positionY[1], 32, 32, self.x, self.y,  object_sizeW, object_sizeH)
        # elif self.type is 12:
        #     self.image.clip_draw(positionX[3], positionY[0], 32, 32, self.x, self.y,  object_sizeW, object_sizeH)
        #
        # elif self.type is 13:
        #     self.image.clip_draw(positionX[3], positionY[7], 32, 32, self.x, self.y,  object_sizeW, object_sizeH)

        if self.type is 1:
            self.image.clip_draw(positionX[0], positionY[2], image_sizeW, image_sizeH, self.x, self.y, object_sizeW,
                                 object_sizeH)
        elif self.type is 2:
            self.image.clip_draw(positionX[0], positionY[1], image_sizeW, image_sizeH, self.x, self.y, object_sizeW,
                                 object_sizeH)

        draw_rectangle(*self.get_bb())
        pass
