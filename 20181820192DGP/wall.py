from pico2d import *
import game_world

import game_framework

image_sizeW = 64
image_sizeH = 64

PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class WallBlock:

    def __init__(self, pos):
        self.image = load_image('chip\\tileset\\block3.png')
        self.x = pos[0]
        self.y = pos[1]
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32
        self.drawing = True

        pass

    def get_bb(self):
        return self.x - 32, self.y + 32, self.x + 32, self.y - 32

    def update(self):

        pass

    def late_update(self):

        player = game_world.bring_object(1, 0)

        if player.x <= self.x:  # 플레이어 -> ㅁ
            player.x -= (player.right - self.left)
        elif player.x >= self.x:  # ㅁ <- 플레이어
            player.x += (self.right - player.left)

        pass

    def late_update2(self):
        enemy = game_world.bring_object(1, 1)

        if enemy.x <= self.x:  # 플레이어 -> ㅁ
            enemy.x -= (enemy.right - self.left - 10)
        elif enemy.x >= self.x:  # ㅁ <- 플레이어
            enemy.x += (self.right - enemy.left + 10)

    def draw(self):
        if self.drawing:
            self.image.draw(self.x, self.y, image_sizeW, image_sizeH)
        draw_rectangle(*self.get_bb())
        pass
