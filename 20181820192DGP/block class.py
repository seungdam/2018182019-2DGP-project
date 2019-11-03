from pico2d import *


image_sizeW = 64
image_sizeH = 64


class FlourBlock:
    image = None

    def __init__(self, pos):
        if FlourBlock.image is None:
            self.image = load_image('chip\\block4.png')
        self.x = pos[0]
        self.y = pos[1]
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32

        self.drawing = True
        pass

    def check_collision(self,player):
        if player.left < self.right and player.right > self.left and player.bottom <= self.top and player.top >= self.bottom and player.falling:
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


# -------------------------------------------------------------

class LeftBlock:

    def __init__(self, pos):
        self.image = load_image('chip\\block3.png')
        self.x = pos[0]
        self.y = pos[1]
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32
        self.drawing = True

        pass

    def update(self):
        pass

    def check_collision(self):
        if player.left < self.right and player.right > self.left and player.bottom <= self.top and player.top >= self.bottom:
            if player.left <= self.right:
                player.x += self.right - player.left
        pass

    def draw(self):
        if self.drawing:
            self.image.draw(self.x, self.y, image_sizeW, image_sizeH)
        # draw_rectangle(self.left, self.top, self.right, self.bottom)

        pass


class RightBlock:
    image = None

    def __init__(self, pos):
        if RightBlock.image is None:
            self.image = load_image('chip\\block3.png')
        self.x = pos[0]
        self.y = pos[1]
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32
        self.drawing = True

        pass

    def update(self):
        pass

    def check_collision(self):
        if player.left < self.right and player.right > self.left and player.bottom <= self.top and player.top >= self.bottom:
            if player.right >= self.left:
                player.x -= player.right - self.left
        pass

    def draw(self):
        if self.drawing:
            self.image.draw(self.x, self.y, image_sizeW, image_sizeH)
        # draw_rectangle(self.left, self.top, self.right, self.bottom)

        pass

#---------------------- 위 코드의 경우 충돌체크 부분을 합칠 예정 -----------

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

    def check_collision(self):
        if player.left < self.right and player.right > self.left and player.bottom <= self.top and player.top >= self.bottom and player.falling and self.fill:
            player.falling = False
            if player.bottom <= self.top:
                player.y += self.top - player.bottom
        pass

    def crush(self):
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


class Flag:
    global player, stageClear

    def __init__(self, pos):
        self.noFlagImage = load_image('chip\\check_point_noflag.png')
        self.FlagImage = load_image('chip\\check_point.png')
        self.x = pos[0]
        self.y = pos[1]
        self.frame = 0
        self.left = self.x - 10
        self.top = self.y + 32
        self.right = self.x + 10
        self.bottom = self.y - 32
        self.flagOn = False
        pass

    def update(self):
        if player.objectNum == 16:
            self.flagOn = True

        if self.flagOn:
            self.frame = (self.frame + 1) % 10
        else:
            pass
        pass

    def check_collision(self):
        if self.flagOn:
            if (player.left <= self.right and player.right >= self.left) and (
                    player.bottom <= self.top and player.top >= self.bottom):
                # game_framework.quit()

        pass

    def draw(self):
        if self.flagOn:
            self.FlagImage.clip_draw(self.frame * image_sizeW, 0 , image_sizeW, image_sizeH, self.x, self.y)
        else:
            self.noFlagImage.draw(self.x, self.y)
        #   draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass

