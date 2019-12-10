from pico2d import *

import pygame


game = True
player = None
block = []
crushBlockList = []
objectList = []
count = 0
backGround = None

open_canvas(1280,640)
tile_type = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 1
             [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],  # 2
             [0, 0, 0, 0, 2, 1, 1, 1, 3, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0],  # 3
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],  # 4
             [0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 4, 1, 1, 1, 1, 4, 0, 0],  # 5
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],  # 6
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],  # 7
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],  # 8
             [0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0]  # 9
             ]
class Player:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.state = 0
        self.frame = 0
        self.speed = 4
        self.fallSpeed = 5

        self.idle = load_image('character_idle.png')
        self.run_right = load_image('character_run_right.png')
        self.run_left = load_image('character_run_left.png')
        self.up_down = load_image('character_updown2.png')
        self.action_right = load_image('character_action_right.png')
        self.action_left = load_image('character_action_left.png')

        self.falling = True
        self.left = self.x - 22
        self.top = self.y + 20
        self.right = self.x + 22
        self.bottom = self.y - 32

    pass

    def update(self):

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

        if self.falling:
            self.y -= self.fallSpeed

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
        draw_rectangle(self.left, self.top, self.right, self.bottom)
        if self.state == 0:
            self.idle.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif self.state == 1:
            self.run_right.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif self.state == -1:
            self.run_left.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif self.state == 2 or self.state == -2:
            self.up_down.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif self.state == 3:
            self.action_right.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif self.state == -3:
            self.action_left.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)

# -------------------------------------------------------------------------------

class DownBlock:
    global player
    image = None

    def __init__(self, pos):
        if DownBlock.image is None:
            self.image = load_image('block4.png')
        self.x = pos[0]
        self.y = pos[1]
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32

        self.drawing = True
        pass



    def check_collision(self):
        if player.left < self.right and player.right > self.left and player.bottom <= self.top and player.top >= self.bottom and player.falling:
            player.falling = False
            if player.bottom <= self.top:
                player.y += self.top - player.bottom

        pass

    def update(self):
        pass

    def draw(self):
        if self.drawing:
            self.image.draw(self.x, self.y, 64, 64)
        draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass


# -------------------------------------------------------------


class LeftBlock:
    global player

    def __init__(self,pos):
        self.image = load_image('block3.png')
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
            self.image.draw(self.x, self.y, 64, 64)
        draw_rectangle(self.left, self.top, self.right, self.bottom)

        pass


class RightBlock:
    global player
    image = None

    def __init__(self,pos):
        if RightBlock.image is None:
            self.image = load_image('block3.png')
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
            self.image.draw(self.x, self.y, 64, 64)
        draw_rectangle(self.left, self.top, self.right, self.bottom)

        pass


class CrushBlock:
    global player

    def __init__(self,pos):
        self.image = load_image('block3.png')
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
        pass

    def draw(self):
        if self.fill:
            self.image.draw(self.x, self.y, 64, 64)
            self.image.draw(self.left, self.top, 10, 10)
            draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass


# --------------------------------------------------------------

class Object:
    global player
    image = None

    def __init__(self, pos):

        if Object.image is None:
            self.image = load_image('Apple.png')
        self.x = pos[0]
        self.y = pos[1]
        self.frame = 0
        self.left = self.x - 16
        self.top = self.y + 16
        self.right = self.x + 16
        self.bottom = self.y - 16
        self.drawing = True

        pass

    def update(self):
        self.frame = (self.frame + 1) % 17
        pass

    def check_collision(self):
        if (player.left <= self.right and player.right >= self.left) and (
                player.bottom <= self.top and player.top >= self.bottom):
            self.drawing = False
        else:
            self.drawing = True
        pass

    def draw(self):
        if self.drawing:
            self.image.clip_draw(self.frame * 32, 0, 32, 32, self.x, self.y)
        draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass


def interact():
    global player, backGround, count
    player.falling = True
    for i in range(0, 33):
        block[i].check_collision()
    for i in crushBlockList:
        i.check_collision()
        i.crush()
    for i in objectList:
        i.check_collision()


player = Player((500, 500))
backGround = load_image('realBackGround.png')

for i in range(6):
    objectList.append(Object((520 + (i * 20),470)))


for i in range(0, 10):
    for k in range(0, 19):
        if tile_type[i][k] == 1:
            block.append(DownBlock((32 + 64 * k, 608 - i * 64)))
            count += 1
        elif tile_type[i][k] == 2:
            block.append(LeftBlock((32 + 64 * k, 608 - i * 64)))
            count += 1
        elif tile_type[i][k] == 3:
            crushBlockList.append(CrushBlock((32 + 64 * k, 608 - i * 64)))
        elif tile_type[i][k] == 4:
            block.append(RightBlock((32 + 64 * k, 608 - i * 64)))
            count += 1


def handle_events():
    global player, game
    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN and not player.falling:
            if event.key == SDLK_RIGHT:
                player.state = 1
            elif event.key == SDLK_LEFT:
                player.state = -1
            elif event.key == SDLK_UP :
                player.state = 2
            elif event.key == SDLK_DOWN :
                player.state = -2
            elif event.key == SDLK_x:
                player.state = 3
            elif event.key == SDLK_z:
                player.state = -3
            elif event.key == SDLK_ESCAPE:
                game = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP or event.key == SDLK_DOWN:
                player.state = 0
                pass
            else:
                player.state = 0
        elif event.type == SDL_QUIT:
            game = False
    pass






# --------------- initiate map -----------

# --------------------------------------------
# stage1 = Stage1()










while game:
    handle_events()
    player.update()
    player.update_rect()
    for i in objectList:
        i.update()
    interact()

    clear_canvas()
    backGround.draw(640, 320)
    for i in block:
        i.draw()
    for i in crushBlockList:
        i.draw()
    for i in objectList:
        i.draw()
    player.draw()
    update_canvas()