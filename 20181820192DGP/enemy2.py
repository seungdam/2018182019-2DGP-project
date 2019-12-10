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

RUN, IDLE, APPEARING = range(3)
UP, DOWN = range(2)


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


class Monster2:
    def __init__(self, pos):
        self.run = load_image('chip\\enemy\\Frog.png')
        self.idle = load_image('chip\\enemy\\Frog_idle.png')
        self.appear = load_image('chip\\character\\Appearing.png')
        self.x = pos[0]
        self.y = pos[1]
        self.state = RUN  # 0 일때 정지 상태 1일때 움직이는 상태
        self.frame = 0
        self.dir = random.randint(0, 1)
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

        self.sleep = False  # 플레이어가 오브젝트를 먹는 순간해제
        pass

    def get_bb(self):
        return self.left2, self.top2, self.right2, self.bottom2

    def get_bb2(self):
        return self.camera_left, self.camera_top, self.camera_right, self.camera_bottom

    def update(self):
        lebbers = game_world.bring_objects(1)
        player = game_world.bring_object(6, 0)

        if self.state is RUN:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

            if intersected_rectangle(self.collided_Rect2, self.left, self.top, self.right,
                                     self.bottom, player.left, player.top, player.right, player.bottom):
                player.state = 3

            if self.dir is UP:
                self.y += self.velocity * game_framework.frame_time
            elif self.dir is DOWN:
                self.y -= self.velocity * game_framework.frame_time

            self.left = self.x - 32
            self.top = self.y + 32
            self.right = self.x + 32
            self.bottom = self.y - 32

            self.left2 = self.x - colW + 10
            self.top2 = self.y + colH - 10
            self.right2 = self.x + colW - 10
            self.bottom2 = self.y - colH

            if self.dir is UP:
                self.camera_top = self.top + 48
                self.camera_bottom = self.top + 16
                self.camera_left = self.left + 16
                self.camera_right = self.right - 16
            elif self.dir is DOWN:
                self.camera_top = self.bottom - 16
                self.camera_bottom = self.camera_top - 32
                self.camera_left = self.left + 16
                self.camera_right = self.right - 16

            self.change_state_time -= 1

            for i in lebbers:
                if intersected_rectangle(self.collided_Rect, self.camera_left, self.camera_top, self.camera_right,
                                         self.camera_bottom, i.left, i.top, i.right, i.bottom):
                    self.change_state_time = 0

            if self.change_state_time < 0:
                self.state = IDLE
                self.change_state_time = 700

        elif self.state is IDLE:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
            if intersected_rectangle(self.collided_Rect2, self.left, self.top, self.right,
                                     self.bottom, player.left, player.top, player.right, player.bottom):
                player.state = 3

            self.change_state_time -= 1

            if self.change_state_time is 0:
                self.change_state_time = 1000
                self.state = RUN
                if self.dir is UP:
                    self.dir = DOWN
                else:
                    self.dir = UP
        pass

    def late_update(self):

        pass

    def rezen(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.state = APPEARING
        self.dir = random.randint(0, 1)

    def draw(self):
        if self.state is RUN:
            if self.dir is UP:
                self.run.clip_draw(int(self.frame) * image_sizeW, 0, object_sizeW, object_sizeH, self.x, self.y)
            elif self.dir is DOWN:
                self.run.clip_composite_draw(int(self.frame) * image_sizeW, 0, image_sizeW, image_sizeH, 0.0, 'h',
                                             self.x, self.y, object_sizeW, object_sizeH)
        elif self.state is IDLE:
            self.idle.clip_draw(int(self.frame) * image_sizeW, 0, object_sizeW, object_sizeH, self.x, self.y)
        elif self.state is APPEARING:
            self.appear.clip_draw(int(self.frame) * 96, 0, 96, 96, self.x, self.y)
        print(self.state)
        pass
