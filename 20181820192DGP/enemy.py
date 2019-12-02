from pico2d import *

import game_world
import game_framework
import random

image_sizeW = 64
image_sizeH = 64

object_sizeW = 64
object_sizeH = 64

colH = 32
colW = 32

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

RUN, IDLE, STUN, APPEARING = range(4)
LEFT, RIGHT = range(2)


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


class Monster1:
    def __init__(self, pos):
        self.run = load_image('chip\\enemy\\run.png')
        self.idle = load_image('chip\\enemy\\idle.png')
        self.appear = load_image('chip\\character\\Appearing.png')
        self.x = pos[0]
        self.y = pos[1]
        self.state = RUN  # 0 일때 정지 상태 1일때 움직이는 상태
        self.frame = 0
        self.dir = 1
        self.change_state_time = 700
        self.velocity = RUN_SPEED_PPS
        self.falling = True

        self.left = self.x - colW
        self.top = self.y + colH
        self.right = self.x + colW
        self.bottom = self.y - colH

        self.left2 = self.x - colW + 10
        self.top2 = self.y + colH
        self.right2 = self.x + colW - 10
        self.bottom2 = self.y - colH

        self.camera_left = 0
        self.camera_top = 0
        self.camera_right = 0
        self.camera_bottom = 0

        self.font = load_font('chip\\font\\ENCR10B.TTF', 16)

        self.collided_Rect_Height = 0
        self.collided_Rect_Width = 0
        self.collided_Rect = [0, 0, 0, 0]
        self.collided_Rect2 = [0, 0, 0, 0]

        self.sleep = False  # 플레이어가 오브젝트를 먹는 순간 해제
        self.rezen_time = 2000
        self.rezen_position = [pos[0], pos[1]]
        pass

    def get_bb(self):
        return self.left2, self.top2, self.right2, self.bottom2

    def get_bb2(self):
        return self.camera_left, self.camera_top, self.camera_right, self.camera_bottom

    def update(self):

        if self.falling:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time

        wall = game_world.bring_objects(3)
        crush = game_world.bring_objects(4)
        player = game_world.bring_object(6, 0)
        if self.state is RUN and self.falling is False:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12
            if intersected_rectangle(self.collided_Rect2, self.left, self.top, self.right,
                                     self.bottom, player.left, player.top, player.right, player.bottom) and player.state is not 3:
                player.state = 3
                player.frame = 0
            if self.dir is RIGHT:
                self.x += self.velocity * game_framework.frame_time
            elif self.dir is LEFT:
                self.x -= self.velocity * game_framework.frame_time

            self.change_state_time -= 1

            for i in crush:
                if self.bottom - 40 <= i.y <= self.bottom:
                    if intersected_rectangle(self.collided_Rect2, self.camera_left, self.camera_top, self.camera_right,
                                             self.camera_bottom, i.left, i.top, i.right, i.bottom):
                        self.change_state_time = 0

            for i in wall:
                if self.bottom - 40 <= i.y <= self.bottom:
                    if intersected_rectangle(self.collided_Rect2, self.camera_left, self.camera_top, self.camera_right,
                                             self.camera_bottom, i.left, i.top, i.right, i.bottom):
                        self.change_state_time = 0

            if self.change_state_time < 0:
                self.change_state_time = 500
                self.state = IDLE

        elif self.state is IDLE:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11

            if intersected_rectangle(self.collided_Rect2, self.left, self.top, self.right,
                                     self.bottom, player.left, player.top, player.right, player.bottom):
                player.state = 3

            self.change_state_time -= 1

            if self.change_state_time is 0:
                self.change_state_time = 1000
                self.state = RUN
                if self.dir is RIGHT:
                    self.dir = LEFT
                else:
                    self.dir = RIGHT

        elif self.state is STUN:
            self.rezen_time -= 1
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11

            if self.rezen_time < 0:
                self.rezen_time = 1000
                self.rezen((self.rezen_position[0], self.rezen_position[1]))
        elif self.state is APPEARING:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
            if self.frame >= 7:
                self.state = RUN
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32

        self.left2 = self.x - colW + 10
        self.top2 = self.y + colH - 10
        self.right2 = self.x + colW - 10
        self.bottom2 = self.y - colH

        if self.dir is RIGHT:
            self.camera_left = self.right + 16
            self.camera_top = self.bottom - 16
            self.camera_right = self.camera_left + colW
            self.camera_bottom = self.camera_top - colW
        elif self.dir is LEFT:
            self.camera_left = self.left - 16 - colW
            self.camera_top = self.bottom - 16
            self.camera_right = self.left - 16
            self.camera_bottom = self.camera_top - colH

        pass

    def late_update(self):

        player = game_world.bring_object(6, 0)
        if self.state is STUN:
            if intersected_rectangle(self.collided_Rect, self.left, self.top, self.right,
                                     self.bottom, player.left, player.top, player.right, player.bottom):
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

    def rezen(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.state = APPEARING
        self.dir = random.randint(0, 1)

    def draw(self):
        if self.state is RUN:
            if self.dir is RIGHT:
                self.run.clip_draw(int(self.frame) * image_sizeW, 0, object_sizeW, object_sizeH, self.x, self.y)
            elif self.dir is LEFT:
                self.run.clip_composite_draw(int(self.frame) * image_sizeW, 0, image_sizeW, image_sizeH, 0.0, 'h',
                                             self.x, self.y, object_sizeW, object_sizeH)
        elif self.state is STUN or self.state is IDLE:
            self.idle.clip_draw(int(self.frame) * image_sizeW, 0, object_sizeW, object_sizeH, self.x, self.y)
        elif self.state is APPEARING:
            self.appear.clip_draw(int(self.frame) * 96, 0, 96, 96, self.x, self.y)
        draw_rectangle(*self.get_bb())
        # draw_rectangle(*self.get_bb2())
        print(self.state)
        pass
