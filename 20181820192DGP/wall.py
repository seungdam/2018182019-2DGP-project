from pico2d import *
import new_stage1_state
import game_framework
image_sizeW = 64
image_sizeH = 64

PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

def check_intersected_rect(left1, top1, right1, bottom1, left2, top2, right2, bottom2):  # 자기자신의 인자가 먼저 그이후에 플레이어 인자
    if left2 < right1 and right1 > left2 and bottom2 <= top1 and top2 >= bottom1:
        return True
    return False


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

        # --------- 플레이어 객체 정보 ---------
        self.o_falling = False
        self.o_x = 0
        self.o_y = 0
        self.o_left = 0
        self.o_top = 0
        self.o_right = 0
        self.o_bottom = 0
        self.o_actionOn = False
        # -----------------------------------------

        pass

    def get_bb(self):
        return self.x - 32, self.y + 32, self.x + 32, self.y - 32

    def get_player_info(self):
        self.o_falling = new_stage1_state.player.falling
        self.o_x = new_stage1_state.player.x
        self.o_y = new_stage1_state.player.y
        self.o_left = new_stage1_state.player.left
        self.o_top = new_stage1_state.player.top
        self.o_right = new_stage1_state.player.right
        self.o_bottom = new_stage1_state.player.bottom
        self.o_actionOn = new_stage1_state.player.actionOn

    def update(self):

        pass

    def late_update(self):
        if self.o_left < self.right and self.o_right > self.left and self.o_bottom <= self.top and self.o_top >= self.bottom:
            print("l")
            if self.o_left <= self.right:
                new_stage1_state.player.x += (self.right - self.o_left)
            if self.o_right >= self.left:
                new_stage1_state.player.x -= (self.o_right - self.left)
        pass

    def draw(self):
        if self.drawing:
            self.image.draw(self.x, self.y, image_sizeW, image_sizeH)
        draw_rectangle(self.o_left, self.o_top, self.o_right, self.o_bottom)

        pass
