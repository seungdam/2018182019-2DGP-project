from pico2d import *

import game_world
import game_framework
import random

image_sizeW = 32
image_sizeH = 32

object_sizeW = 32
object_sizeH = 32

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

RUN, IDLE, STUN = range(3)
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
        self.x = pos[0]
        self.y = pos[1]
        self.state = RUN  # 0 일때 정지 상태 1일때 움직이는 상태
        self.frame = 0
        self.dir = 1
        self.change_state_time = 700
        self.velocity = RUN_SPEED_PPS
        self.left = self.x - 16
        self.top = self.y + 16
        self.right = self.x + 16
        self.bottom = self.y - 16

        self.camera_left = 0
        self.camera_top = 0
        self.camera_right = 0
        self.camera_bottom = 0

        self.collided_Rect_Height = 0
        self.collided_Rect_Width = 0
        self.collided_Rect = [0, 0, 0, 0]
        self.collided_Rect2 = [0, 0, 0, 0]

        self.sleep = False  # 플레이어가 오브젝트를 먹는 순간 해제
        self.rezen_time = 2000
        self.rezen_postion =[pos[0], pos[1]]
        pass

    def get_bb(self):
        return self.x - 8, self.y + 16, self.x + 8, self.y - 16
    def update(self):

        player = game_world.bring_object(1, 0)

        wall = game_world.bring_objects(3)
        crush = game_world.bring_objects(4)

        if self.state is RUN:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

            if self.dir is RIGHT:
                self.x += self.velocity * game_framework.frame_time
                self.camera_left = self.left + 8
                self.camera_top =  self.bottom - 8
                self.camera_right = self.camera_left + 16
                self.camera_bottom = self.camera_top - 16
            elif self.dir is LEFT:
                self.x -= self.velocity * game_framework.frame_time
                self.camera_left = self.camera_right - 16
                self.camera_top = self.bottom -8
                self.camera_right = self.left - 8
                self.camera_bottom = self.camera_top - 16

            self.change_state_time -= 1

            for i in crush:
                if not intersected_rectangle(self.collided_Rect2, self.camera_left, self.camera_top, self.camera_right, self.camera_bottom,
                                     crush[i].left,  crush[i].top,  crush[i].right, crush[i].bottom):
                    self.change_state_time = 0


            if self.change_state_time < 0:
                self.change_state_time = 500
                self.state = IDLE
        elif self.state is IDLE:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
            self.change_state_time -= 1
            if self.change_state_time is 0:
                self.change_state_time = 1000
                self.state = RUN
                if self.dir is RIGHT:
                    self.dir = LEFT
                else:
                    self.dir = RIGHT
        elif self.state is STUN:

            if self.state is STUN:
                if player.falling:
                    player.falling = False
                    if player.bottom < self.top:
                        player.y += (self.top - player.bottom)

            self.rezen_time -= 1
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11

            if self.rezen_time < 0:
                self.rezen_time = 1000
                self.rezen((self.rezen_postion[0], self.rezen_postion[1]))

        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32
        pass


    def rezen(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.state = IDLE
        self.dir = random.randint(0,1)

    def draw(self):
        if self.state is RUN:
            if self.dir is RIGHT:
                self.run.clip_draw(int(self.frame) * image_sizeW, 0, object_sizeW, object_sizeH, self.x, self.y)
            elif self.dir is LEFT:
                self.run.clip_composite_draw(int(self.frame) * image_sizeW, 0, image_sizeW, image_sizeH, 0.0, 'h',
                                             self.x, self.y, object_sizeW, object_sizeH)
        elif self.state is STUN or self.state is IDLE:
            self.idle.clip_draw(int(self.frame) * image_sizeW, 0, object_sizeW, object_sizeH, self.x, self.y)

        draw_rectangle(*self.get_bb())
        pass
