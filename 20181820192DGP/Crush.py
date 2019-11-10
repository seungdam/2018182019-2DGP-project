from pico2d import *

image_sizeW = 64
image_sizeH = 64


def check_intersected_rect(left1, top1, right1, bottom1, left2, top2, right2, bottom2):  # 자기자신의 인자 (1)   플레이어 인자 (2)
    if left2 < right1 and right1 > left2 and bottom2 <= top1 and top2 >= bottom1:
        return True


class CrushBlock:
    def __init__(self, pos):
        self.image = load_image('chip\\Terrain (16x16)_9.png')
        self.x = pos[0]
        self.y = pos[1]
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32
        self.fill = True
        pass

    def update(self):
        pass

    def check_collision(self, player):
        if check_intersected_rect(self.left, self.top, self.right, self.bottom, player.left, player.top, player.right,
                                  player.bottom) and self.fill:
            player.falling = False
            if player.bottom <= self.top:
                player.y += self.top - player.bottom
        pass

    def crush(self, player):
        if player.right <= self.left and player.left >= self.left - 64 and self.top <= player.y <= self.top + 32:
            if player.state == 3:
                self.fill = False
        if player.left >= self.right and player.right <= self.right + 64 and self.top <= player.y <= self.top + 32:
            if player.state == -3:
                self.fill = False

    def draw(self):
        if self.fill:
            self.image.draw(self.x, self.y, image_sizeW, image_sizeH)
            # draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass
