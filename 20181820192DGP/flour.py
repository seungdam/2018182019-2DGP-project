from pico2d import *

image_sizeW = 64
image_sizeH = 64


def check_intersected_rect(left1, top1, right1, bottom1, left2, top2, right2, bottom2):  # 자기자신의 인자가 먼저 그이후에 플레이어 인자
    if left2 < right1 and right1 > left2 and bottom2 <= top1 and top2 >= bottom1:
        return True
    return False


# --------------------- 바닥 --------------------

class FlourBlock:
    image = None

    def __init__(self, pos):
        if FlourBlock.image is None:
            self.image = load_image('chip\\tileset\\block4.png')
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

    def check_collision(self, player):
        if check_intersected_rect(self.left, self.top, self.right, self.bottom, player.left, player.top, player.right,
                                  player.bottom) and player.falling:
            player.falling = False

            if player.bottom <= self.top:
                player.y += self.top - player.bottom

        pass

    def update(self):
        pass

    def draw(self):
        if self.drawing:
            self.image.draw(self.x, self.y, image_sizeW, image_sizeH)
        # draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass

# ---------------------------좌우 충돌체크 벽------------------------------


# class RightBlock:
#     image = None
#
#     def __init__(self, pos):
#         if RightBlock.image is None:
#             self.image = load_image('chip\\block3.png')
#         self.x = pos[0]
#         self.y = pos[1]
#         self.left = self.x - 32
#         self.top = self.y + 32
#         self.right = self.x + 32
#         self.bottom = self.y - 32
#         self.drawing = True
#
#         pass
#
#     def update(self):
#         pass
#
#     def check_collision(self):
#         if player.left < self.right and player.right > self.left and player.bottom <= self.top and player.top >= self.bottom:
#             if player.right >= self.left:
#                 player.x -= player.right - self.left
#         pass
#
#     def draw(self):
#         if self.drawing:
#             self.image.draw(self.x, self.y, image_sizeW, image_sizeH)
#         # draw_rectangle(self.left, self.top, self.right, self.bottom)
#
#         pass

# ---------------------- 위 코드의 경우 충돌체크 부분을 합칠 예정 -----------
