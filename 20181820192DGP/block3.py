from pico2d import *
import game_world
import random

IMAGE_WIDTH, IMAGE_HEIGHT = 32, 32

positionX = [0]
positionY = [0, 48, 96]


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
        self.restore = 2000

        self.left = self.x - colW
        self.top = self.y + colH
        self.right = self.x + colW
        self.bottom = self.y - colH

        self.check2_left = self.left + 16
        self.check2_top = self.top + colH + 16
        self.check2_right = self.check2_left + 32
        self.check2_bottom = self.top + 16

        self.check1_left = self.check2_left - colW - colW
        self.check1_top = self.check2_top
        self.check1_right = self.check2_left - colW
        self.check1_bottom = self.check2_bottom

        self.check3_left = self.check2_right + colW
        self.check3_top = self.check2_top
        self.check3_right = self.check3_left + colW
        self.check3_bottom = self.check2_bottom

        self.collided_Rect_Height = 0
        self.collided_Rect_Width = 0
        self.collided_Rect = [0, 0, 0, 0]
        self.collided_Rect2 = [0, 0, 0, 0]
        self.collided_Rect3 = [0, 0, 0, 0]
        self.collided_Rect4 = [0, 0, 0, 0]
        self.fill = True
        self.canCrush = True
        pass

    def get_bb(self):
        return self.left, self.top, self.right, self.bottom

    def get_bb2(self):
        return self.check1_left, self.check1_top, self.check1_right, self.check1_bottom

    def get_bb3(self):
        return self.check2_left, self.check2_top, self.check2_right, self.check2_bottom

    def get_bb4(self):
        return self.check3_left, self.check3_top, self.check3_right, self.check3_bottom

    def update(self):

        player = game_world.bring_object(6, 0)
        crush = game_world.bring_objects(4)
        enemy = game_world.bring_objects(2)

        self.canCrush = True
        for i in crush:
            if i.fill:
                if intersected_rectangle(self.collided_Rect3, self.check2_left, self.check2_top, self.check2_right,
                                         self.check2_bottom,
                                         i.left, i.top, i.right, i.bottom):
                    self.canCrush = False

        for i in enemy:
            if i.state is 2:
                if intersected_rectangle(self.collided_Rect3, self.check2_left, self.check2_top, self.check2_right,
                                         self.check2_bottom,
                                         i.left, i.top, i.right, i.bottom):
                    self.canCrush = False

        if intersected_rectangle(self.collided_Rect2, self.left, self.top, self.right,
                                 self.bottom, player.left, player.top, player.right,
                                 player.bottom) and self.fill:
            if self.left <= player.x <= self.right and self.bottom <= player.y <= self.top and player.state is not 3:
                player.state = 3
                player.frame = 0

        if intersected_rectangle(self.collided_Rect2, self.check1_left, self.check1_top, self.check1_right,
                                 self.check1_bottom, player.left, player.top, player.right,
                                 player.bottom) and player.do_right_action and self.canCrush:
            self.fill = False
        elif intersected_rectangle(self.collided_Rect3, self.check3_left, self.check3_top, self.check3_right,
                                   self.check3_bottom, player.left, player.top, player.right,
                                   player.bottom) and player.do_left_action and self.canCrush:
            self.fill = False

        if not self.fill:
            self.restore -= 1
            if self.restore == 0:
                self.fill = True
                self.restore = 1000
        pass

    def late_update(self):
        player = game_world.bring_object(6, 0)
        enemy = game_world.bring_objects(2)
        if self.fill:
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

            for i in enemy:
                if intersected_rectangle(self.collided_Rect, self.left, self.top, self.right, self.bottom,
                                         i.left2, i.top2, i.right2, i.bottom2):
                    self.collided_Rect_Height = self.collided_Rect[1] - self.collided_Rect[3]
                    self.collided_Rect_Width = self.collided_Rect[2] - self.collided_Rect[0]
                    if i.state is 2:
                        i.falling = False

                    if self.collided_Rect_Width > self.collided_Rect_Height:
                        if self.collided_Rect[1] == self.y + colH:
                            i.falling = False
                            if i.state is not 2:
                                i.y += self.collided_Rect_Height
                        elif self.collided_Rect[3] == self.y - colH:
                            if i.state is not 2:
                                i.y -= self.collided_Rect_Height
                                i.y -= 1
                    else:
                        if self.collided_Rect[0] == self.x - colW:
                            if i.state is not 2:
                                i.x -= self.collided_Rect_Width
                        elif self.collided_Rect[2] == self.x + colW:
                            if i.state is not 2:
                                i.x += self.collided_Rect_Width
        else:
            for i in enemy:
                if intersected_rectangle(self.collided_Rect, self.left, self.top, self.right, self.bottom,
                                         i.left2, i.top2, i.right2, i.bottom2):
                    if i.y < self.y:
                        i.x = self.x
                        i.falling = False
                        i.state = 2

    def draw(self):
        if self.fill:
            self.image.clip_draw(positionX[0], positionY[0], image_sizeW, image_sizeH, self.x, self.y, object_sizeW,
                                 object_sizeH)
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_bb2())
        draw_rectangle(*self.get_bb3())
        draw_rectangle(*self.get_bb4())
