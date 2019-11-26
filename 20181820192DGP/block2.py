from pico2d import *
import game_world

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


class FlourBlock:
    image = None

    def __init__(self, pos, type):
        if FlourBlock.image is None:
            self.image = load_image('chip\\tileset\\newTile(7X11)2.png')
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

        # --------- 플레이어 객체 정보 ---------

        # -----------------------------------------
        pass

    def update(self):
        player = game_world.bring_object(1, 0)

        if intersected_rectangle(self.collided_Rect, self.left, self.top, self.right, self.bottom,
                                 player.left, player.top, player.right, player.bottom):
            self.collided_Rect_Height = self.collided_Rect[1] - self.collided_Rect[3]
            self.collided_Rect_Width = self.collided_Rect[2] - self.collided_Rect[0]

            if self.collided_Rect_Width > self.collided_Rect_Height:

                if self.collided_Rect[1] == self.y + 32:
                    player.falling = False
                    player.y += self.collided_Rect_Height
                elif self.collided_Rect[3] == self.y - 32:
                    player.y -= self.collided_Rect_Height
                    player.y -= 1
            else:
                if self.collided_Rect[0] == self.x - 32:
                    player.x -= self.collided_Rect_Width
                elif self.collided_Rect[2] == self.x + 32:
                    player.x += self.collided_Rect_Width
        pass

    def late_update(self):
        pass

    def late_update2(self):
        enemy = game_world.bring_object(1, 1)

        if enemy.bottom < self.top:
            enemy.y += (self.top - enemy.bottom)

    def draw(self):
        if self.type is 1:
            self.image.clip_draw(positionX[0], positionY[10], 32, 32, self.x, self.y, 64, 64)
        elif self.type is 2:
            self.image.clip_draw(positionX[1], positionY[10], 32, 32, self.x, self.y, 64, 64)
        elif self.type is 3:
            self.image.clip_draw(positionX[2], positionY[10], 32, 32, self.x, self.y, 64, 64)
        elif self.type is 4:
            self.image.clip_draw(positionX[0], positionY[9], 32, 32, self.x, self.y, 64, 64)
        elif self.type is 5:
            self.image.clip_draw(positionX[1], positionY[9], 32, 32, self.x, self.y, 64, 64)
        elif self.type is 6:
            self.image.clip_draw(positionX[2], positionY[9], 32, 32, self.x, self.y, 64, 64)
        elif self.type is 7:
            self.image.clip_draw(positionX[0], positionY[8], 32, 32, self.x, self.y, 64, 64)
        elif self.type is 8:
            self.image.clip_draw(positionX[1], positionY[8], 32, 32, self.x, self.y, 64, 64)
        elif self.type is 9:
            self.image.clip_draw(positionX[2], positionY[8], 32, 32, self.x, self.y, 64, 64)
        elif self.type is 10:
            self.image.clip_draw(positionX[0], positionY[4], 32, 32, self.x, self.y, 64, 64)
        elif self.type is 11:
            self.image.clip_draw(positionX[1], positionY[4], 32, 32, self.x, self.y, 64, 64)
        elif self.type is 12:
            self.image.clip_draw(positionX[2], positionY[4], 32, 32, self.x, self.y, 64, 64)
        elif self.type is 13:
            self.image.clip_draw(positionX[6], positionY[10], 32, 32, self.x, self.y, 64, 64)
        elif self.type is 14:
            self.image.clip_draw(positionX[6], positionY[10], 32, 32, self.x, self.y, 64, 64)
        elif self.type is -1:
            self.image.clip_draw(positionX[3], positionY[3], 32, 32, self.x, self.y, 64, 64)
        elif self.type is -2:
            self.image.clip_draw(positionX[3], positionY[2], 32, 32, self.x, self.y, 64, 64)
        elif self.type is -3:
            self.image.clip_draw(positionX[3], positionY[1], 32, 32, self.x, self.y, 64, 64)
        elif self.type is -4:
            self.image.clip_draw(positionX[5], positionY[3], 32, 32, self.x, self.y, 64, 64)
        elif self.type is -5:
            self.image.clip_draw(positionX[5], positionY[2], 32, 32, self.x, self.y, 64, 64)
        elif self.type is -6:
            self.image.clip_draw(positionX[5], positionY[1], 32, 32, self.x, self.y, 64, 64)
        pass
