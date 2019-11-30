from pico2d import*
import game_world
import game_framework

image_sizeW = 64
image_sizeH = 64


class LebberTop:
    def __init__(self, pos):
        self.image = load_image('chip\\object\\lebber_top2.png')
        self.x = pos[0]
        self.y = pos[1]

        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32
        pass

    def update(self):

        pass

    def get_bb(self):
        return self.x - 32, self.y + 32, self.x + 32, self.y - 32

    def late_update(self):
        player = game_world.bring_object(1, 0)

        if player.falling and player.can_up:
            player.falling = False

        pass

    def draw(self):
        self.image.draw(self.x, self.y, image_sizeW, image_sizeH)
        pass


class LebberMid:

    def __init__(self, pos):
        self.image = load_image('chip\\object\\lebber_mid2.png')
        self.x = pos[0]
        self.y = pos[1]

        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32
        pass

    def update(self):
        pass

    def get_bb(self):
        return self.x - 32, self.y + 32, self.x + 32, self.y - 32

    def late_update(self):
        player = game_world.bring_object(1,0)
        if player.falling and player.can_up:
            player.falling = False
        pass

    def draw(self):
        self.image.draw(self.x, self.y, image_sizeW, image_sizeH)
        pass

class LebberBottom:

    def __init__(self, pos):
        self.image = load_image('chip\\object\\lebber_bottom2.png')
        self.x = pos[0]
        self.y = pos[1]

        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32
        pass

    def update(self):
        pass

    def get_bb(self):
        return self.x - 32, self.y + 32, self.x + 32, self.y - 32

    def late_update(self):
        player = game_world.bring_object(1,0)
        if player.falling and player.can_up:
            player.falling = False
        pass

    def late_update2(self):
        pass

    def draw(self):

        pass
