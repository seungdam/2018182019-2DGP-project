from pico2d import *
import new_stage1_state

image_sizeW = 64
image_sizeH = 64


# def check_intersected_rect(left1, top1, right1, bottom1, left2, top2, right2, bottom2):  # 자기자신의 인자 (1)   플레이어 인자 (2)
#     if left2 < right1 and right1 > left2 and bottom2 <= top1 and top2 >= bottom1:
#         return True
#
#     return False


class CrushBlock:
    def __init__(self, pos):
        self.image = load_image('chip\\tileset\\Terrain (16x16)_9.png')
        self.x = pos[0]
        self.y = pos[1]

        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32
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
        self.fill = True
        self.restore = 100
        pass

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

        if self.o_right <= self.left and self.o_left >= self.left - 64 and self.top <= self.o_y <= self.top + 32:
            if self.o_actionOn:
                self.fill = False
        if self.o_left >= self.right and self.o_right <= self.right + 64 and self.top <= self.o_y <= self.top + 32:
            if self.o_actionOn:
                self.fill = False

        if not self.fill:
            self.restore -= 1

        if self.restore is 0:
            self.fill = True
            self.restore = 100
        pass

    def get_bb(self):
        return self.x - 32, self.y + 32, self.x + 32, self.y - 32

    def late_update(self):
        self.o_falling = False
        if self.o_bottom <= self.top:
            self.o_y += self.top - self.o_bottom
        pass

    def draw(self):
        if self.fill:
            self.image.draw(self.x, self.y, image_sizeW, image_sizeH)

        pass
