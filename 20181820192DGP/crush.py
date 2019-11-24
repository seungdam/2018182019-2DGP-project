from pico2d import *
import stage1_state

image_sizeW = 64
image_sizeH = 64





class CrushBlock:
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
        if self.left - 42 <= player.x <= self.left and self.top <= player.y <= self.top + 32 and player.do_right_action:  #플레이어 -> 블록
                self.fill = False
        if self.right + 42 >= player.x >= self.right and self.top <= player.y <= self.top + 32 and player.do_left_action: # 블록 <- 플레이어
                self.fill = False

        if not self.fill:
            self.restore -= 1
            if self.restore is 0:
                self.fill = True
                self.restore = 1000
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
        if self.fill:
            self.image.draw(self.x, self.y, image_sizeW, image_sizeH)

        draw_rectangle(*self.get_bb())

        pass
