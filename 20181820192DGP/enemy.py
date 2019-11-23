from pico2d import *
import new_stage1_state

image_sizeW = 64
image_sizeH = 64


# def check_intersected_rect(left1, top1, right1, bottom1, left2, top2, right2, bottom2):  # 자기자신의 인자 (1)   플레이어 인자 (2)
#     if left2 < right1 and right1 > left2 and bottom2 <= top1 and top2 >= bottom1:
#         return True
#
#     return False


class Monster1:
    def __init__(self, pos):
        self.image = load_image('chip\\tileset\\Terrain (16x16)_9.png')
        self.x = pos[0]
        self.y = pos[1]

        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32
        self.fill = True
        self.restore = 1000
        pass

    def update(self):
        player = new_stage1_state.get_ohdam_info()

        pass

    def get_bb(self):
        return self.x - 32, self.y + 32, self.x + 32, self.y - 32

    def late_update(self):
        player = new_stage1_state.get_ohdam_info()
        if self.fill and player.falling:
            player.falling = False
            if player.bottom <= self.top:
                player.y += self.top - player.bottom
                pass
        pass

    def draw(self):

        self.image.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)
        draw_rectangle(*self.get_bb())

        pass
