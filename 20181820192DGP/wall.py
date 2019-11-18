from pico2d import *

image_sizeW = 64
image_sizeH = 64

def collide(a, b):
    left_a, top_a, right_a, bottom_a = a.get_bb()
    left_b, top_b, right_b, bottom_b = b.get_bb()

    if left_b < right_a and right_a > left_b and bottom_b <= top_a and top_b >= bottom_a:
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
        pass

    def get_bb(self):
        return self.x - 32, self.y + 32, self.x + 32, self.y - 32

    def update(self):
        pass

    def late_update(self, player):
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
