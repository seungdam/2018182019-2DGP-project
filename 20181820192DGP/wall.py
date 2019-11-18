from pico2d import *

image_sizeW = 64
image_sizeH = 64


def check_intersected_rect(left1, top1, right1, bottom1, left2, top2, right2, bottom2):  # 자기자신의 인자가 먼저 그이후에 플레이어 인자
    if left2 < right1 and right1 > left2 and bottom2 <= top1 and top2 >= bottom1:
        return True


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

    def check_collision(self, player):
        if check_intersected_rect(self.left, self.top, self.right, self.bottom, player.left, player.top, player.right,
                                  player.bottom) and player.falling:
            if player.left <= self.right:
                player.x += self.right - player.left
            if player.right >= self.left:
                player.x -= player.right - self.left
        pass

    def draw(self):
        if self.drawing:
            self.image.draw(self.x, self.y, image_sizeW, image_sizeH)
        # draw_rectangle(self.left, self.top, self.right, self.bottom)

        pass
