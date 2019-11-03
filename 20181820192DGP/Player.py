from pico2d import*

image_sizeW = 64
image_sizeH = 64

class Player:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.state = 0
        self.frame = 0
        self.speed = 4
        self.fallSpeed = 5
        self.idle = load_image('chip\\character_idle.png')
        self.run_right = load_image('chip\\character_run_right.png')
        self.run_left = load_image('chip\\character_run_left.png')
        self.up_down = load_image('chip\\character_updown2.png')
        self.action_right = load_image('chip\\character_action_right.png')
        self.action_left = load_image('chip\\character_action_left.png')
        self.falling = True
        self.left = self.x - 22
        self.top = self.y + 20
        self.right = self.x + 22
        self.bottom = self.y - 32
        self.objectNum = 0

    pass

    def update(self):
        if self.falling:
            self.y -= self.fallSpeed

        if self.state == 0:
            self.frame = (self.frame + 1) % 11
            delay(0.04)
        elif self.state == 1:
            self.frame = (self.frame + 1) % 11
            delay(0.04)
        elif self.state == -1:
            self.frame = (self.frame - 1) % 11
            delay(0.04)
        elif self.state == 2 or self.state == -2:
            self.frame = (self.frame + 1) % 6
            delay(0.04)
        elif self.state == 3:
            self.frame = 8
            delay(0.04)
        elif self.state == -3:
            self.frame = 1
            delay(0.04)

        if self.state == 1:
            self.speed = 4
            self.x += self.speed
        if self.state == -1:
            self.speed = -4
            self.x += self.speed
        if self.state == 2:
            self.speed = 4
            self.y += self.speed
        if self.state == -2:
            self.speed = -4
            self.y += self.speed

    pass

    def update_rect(self):
        self.left = self.x - 22
        self.top = self.y + 20
        self.right = self.x + 22
        self.bottom = self.y - 32

    def draw(self):

        if self.state == 0:
            self.idle.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)
        elif self.state == 1:
            self.run_right.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)
        elif self.state == -1:
            self.run_left.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)
        elif self.state == 2 or self.state == -2:
            self.up_down.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)
        elif self.state == 3:
            self.action_right.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)
        elif self.state == -3:
            self.action_left.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)
