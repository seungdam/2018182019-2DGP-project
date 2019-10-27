from pico2d import *
import game_framework
import pygame

game = True
claiming = False
state = 0

name = 'Stage1'

tile_type = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 1
             [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],  # 2
             [0, 0, 0, 0, 2, 1, 1, 1, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0],  # 3
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],  # 4
             [0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1, 0, 0],  # 5
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],  # 6
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],  # 7
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],  # 8
             [0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0]  # 9
             ]


def enter():
    pass


def exit():
    pass


def resume():
    pass


def pause():
    pass


def world_update():
    player.update()


def handle_event():
    global game
    global claiming
    global player
    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                player.state = 1
            elif event.key == SDLK_LEFT:
                player.state = -1
            elif event.key == SDLK_UP and claiming:
                player.state = 2
            elif event.key == SDLK_DOWN and claiming:
                player.state = -2
            elif event.key == SDLK_x:
                player.state = 3
            elif event.key == SDLK_z:
                player.state = -3
            elif event.key == SDLK_ESCAPE:
                game = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP or event.key == SDLK_DOWN:
                if not claiming:
                    player.state = 0
            else:
                player.state = 0
        elif event.type == SDL_QUIT:
            game = False
    pass


class Player:
    def __init__(self):
        self.x = 500
        self.y = 500
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
        self.moveRX = True
        self.moveLX = True
        self.top = 0
        self.left = 0
        self.bottom = 0
        self.right = 0

    pass

    def set_position(self, x, y):
        self.x = x
        self.y = y


    def set_rect(self):
        self.left = self.x - 22
        self.top = self.y + 20
        self.right = self.x + 22
        self.bottom = self.y - 32

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
            self.y -= 5

        if self.state == 1 and not self.falling and self.moveRX:
            self.speed = 4
            self.x += self.speed
        if self.state == -1 and not self.falling and self.moveLX:
            self.speed = -4
            self.x += self.speed
        if self.state == 2 and not self.falling:
            self.y += self.speed
        if self.state == -2 and not self.falling:
            self.y += self.speed
        self.set_rect()

    pass

    def drawing(self):
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

    def collision(self):
        pass

open_canvas(1280, 640)
player = Player()
player.set_position(500, 500)

class NormalBlock:
    global player

    def __init__(self):
        self.image = load_image('block4.png')
        self.x = 0
        self.y = 0
        self.top = 0
        self.left = 0
        self.bottom = 0
        self.right = 0
        self.drawing = True
        pass

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32

    def check_collision(self):
        if player.left < self.right and player.right > self.left and player.bottom <= self.top and player.top >= self.bottom \
                and player.falling:
           player.falling = False

        if self.top - player.bottom > self.right - player.left:
            player.moveLX = False;
        pass

    def update(self):
        pass

    def draw(self):
        if self.drawing:
            self.image.draw(self.x, self.y, 64, 64)
        draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass


class WallBlock:
    global player

    def __init__(self):
        self.image = load_image('block3.png')
        self.x = 0
        self.y = 0
        self.top = 0
        self.left = 0
        self.bottom = 0
        self.right = 0
        self.drawing = True
        pass

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32

    def update(self):
        pass

    def check_collision(self):
        if player.left <= self.right and player.right >= self.left and player.bottom <= self.top and player.top >= self.bottom\
                and player.falling:
            player.falling = False

        pass

    def draw(self):
        if self.drawing:
            self.image.draw(self.x, self.y, 64, 64)
        draw_rectangle(self.left, self.top, self.right, self.bottom)

        pass


class CrushBlock:
    global player

    def __init__(self):
        self.image = load_image('block3.png')
        self.x = 0
        self.y = 0
        self.top = 0
        self.left = 0
        self.bottom = 0
        self.right = 0
        self.drawing = True
        pass

    def set_position(self, x, y):
        self.x = x
        self.y = y

        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32

    def update(self):
        pass

    def check_collision(self):
        pass

    def draw(self):
        if self.drawing:
            self.image.draw(self.x, self.y, 64, 64)
        draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass


class Object:
    global player
    def __init__(self, pos):
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
        if (player.left <= self.right and player.right >= self.left) and (player.bottom <= self.top and player.top >= self.bottom):
           self.drawing = False
        else:
            self.drawing = True
        pass

    def draw(self):
        if self.drawing:
            self.image.clip_draw(self.frame * 32, 0, 32, 32, self.x, self.y)
        draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass



object = Object((500,100))
block = []
count = 0


def interact():
    player.falling = True
    player.moveRX = True
    player.moveLX = True
    for i in range(0, 39):
        block[i].check_collision()
    object.check_collision()


# --------------- initiate map -----------
for i in range(0, 10):
    for k in range(0, 19):
        if tile_type[i][k] == 1:
            block.append(NormalBlock())
            block[count].set_position(32 + 64 * k, 608 - i * 64)
            count += 1
        elif tile_type[i][k] == 2:
            block.append(WallBlock())
            block[count].set_position(32 + 64 * k, 608 - i * 64)
            count += 1
        elif tile_type[i][k] == 3:
            block.append(CrushBlock())
            block[count].set_position(32 + 64 * k, 608 - i * 64)
            count += 1
# --------------------------------------------
# stage1 = Stage1()
a = 100
while game:
    handle_event()
    player.update()
    object.update()
    interact()
    clear_canvas()
    # stage1.draw()
    for i in block:
        i.draw()
    object.draw()
    player.drawing()
    update_canvas()
