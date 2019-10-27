from pico2d import *
import game_framework
import pygame

game = True
claiming = False
state = 0

name = 'Stage1'

tile_type = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 2, 1, 1, 1, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0]
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
            elif event.key == SDLK_UP:
                player.state = 2
            elif event.key == SDLK_DOWN:
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
        self.idle = load_image('character_idle.png')
        self.run_right = load_image('character_run_right.png')
        self.run_left = load_image('character_run_left.png')
        self.up_down = load_image('character_updown2.png')
        self.action_right = load_image('character_action_right.png')
        self.action_left = load_image('character_action_left.png')
        self.falling = True
        self.top = 0
        self.left = 0
        self.bottom = 0
        self.right = 0
    pass

    def set_position(self,x,y):
        self.x = x
        self.y = y
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32

    def set_rect(self):
        self.left = self.x - 32
        self.top = self.y + 16
        self.right = self.x + 32
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
            self.y -= 4

        if self.state == 1 and not self.falling:
            self.x += 4
        if self.state == -1 and not self.falling:
            self.x -= 4
        if self.state == 2 and not self.falling:
            self.y += 4
        if self.state == -2 and not self.falling:
            self.y -= 4
        self.set_rect()

    pass

    def drawing(self):
        draw_rectangle(self.left, self.top, self.right, self.bottom)
        if self.state == 0:
            self.idle.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif self.state == 1:
            self.run_right.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif self.state == -1:
            self.run_left.clip_draw(self.frame * 64, 0, 64, 64, self.x , self.y)
        elif self.state == 2 or self.state == -2:
            self.up_down.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif self.state == 3:
            self.action_right.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif self.state == -3:
            self.action_left.clip_draw(self.frame * 64, 0, 64, 64, self.x , self.y)

    def collision(self):
        pass


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

        pass

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32

    def check_collision(self):
        if player.bottom <= self.top:
            player.falling = False
        else:
            player.falling = True
        pass

    def update(self):
        pass

    def draw(self):
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
        if player.bottom < self.top:
            player.falling = False
        else:
            player.falling = True

        pass
    def draw(self):

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
        if player.bottom <= self.top:
            player.falling = False
        else:
            player.falling = True

        pass

    def draw(self):
        self.image.draw(self.x, self.y, 64, 64)
        draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass


open_canvas(1280, 640)
player = Player()
player.set_position(500,500)

block = []
count = 0

def interact():
   for i in range(0, 40):
       block[i].check_collision()

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

while game:
    handle_event()
    player.update()
    interact()
    clear_canvas()
   # stage1.draw()
    for i in block:
        i.draw()
    player.drawing()
    update_canvas()
