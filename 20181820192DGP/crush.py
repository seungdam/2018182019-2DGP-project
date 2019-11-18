from pico2d import *

image_sizeW = 64
image_sizeH = 64


def check_intersected_rect(left1, top1, right1, bottom1, left2, top2, right2, bottom2):  # 자기자신의 인자 (1)   플레이어 인자 (2)
    if left2 < right1 and right1 > left2 and bottom2 <= top1 and top2 >= bottom1:
        return True

    return False


def collide(a, b):
    left_a, top_a, right_a, bottom_a = a.get_bb()
    left_b, top_b, right_b, bottom_b = b.get_bb()

    if left_b < right_a and right_a > left_b and bottom_b <= top_a and top_b >= bottom_a:
        return True

    return False


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
        self.restore = 100
        pass

    def update(self):
        if not self.fill:
            self.restore -= 1

        if self.restore is 0:
            self.fill = True
            self.restore = 100
        pass

    def get_bb(self):
        return self.x - 32, self.y + 32, self.x + 32, self.y - 32

    def late_update(self, player):
        player.falling = False

        if player.bottom <= self.top:
            player.y += self.top - player.bottom

        pass

    def crush(self, player):
        if player.right <= self.left and player.left >= self.left - 64 and self.top <= player.y <= self.top + 32:
            if player.actionOn:
                self.fill = False
        if player.left >= self.right and player.right <= self.right + 64 and self.top <= player.y <= self.top + 32:
            if player.actionOn:
                self.fill = False

    def draw(self):
        if self.fill:
            self.image.draw(self.x, self.y, image_sizeW, image_sizeH)

        pass
