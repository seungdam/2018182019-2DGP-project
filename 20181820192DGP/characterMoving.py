from pico2d import *

open_canvas(1000,1000)
character_idle = load_image('test1.png')
character_run_right = load_image('test2-r.png')
character_run_left = load_image('test2-l.png')
character_action_right = load_image('test4-r.png')
character_action_left = load_image('test4-l.png')
character_up_down = load_image('test3-2.png')

x = 200
y = 500
frame = 0
state = 0 # 0 stand /1 ,-1 run/ 2 -2 up down / 3, -3 action
claiming = False
game = True
# class Stage1:
#     def __init__(self):
#         self.tile_type = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                           [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#                           [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
#                           [0, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
#                           [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
#                           [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 1, 1, 1, 1, 1, 0, 0],
#                           [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
#                           [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
#                           [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
#                           [0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0]
#                           ]
#         self.normal_block = load_image('block4.png')
#         self.wall_block = load_image('block3.png')
#         self.background1 = load_image('trees.png')
#         self.background2 = load_image('sky.png')
#         self.background3 = load_image('clouds.png')
#         self.rectX = []
#         self.rectY = []
#         for i in range(0,10):
#             for j in range(0,19):
#                 if self.tile_type[i][j] == 1 or self.tile_type[i][j] == 2:
#                     self.rectX.append(32 + j * 64)
#                     self.rectY.append(608 - i * 64)
#         self.rect = [[x - 32 for x in self.rectX]]
#     def draw(self):
#
#         self.background2.draw(640, 320, 1280, 640)
#         self.background3.draw(320, 400, 640, 160)
#         self.background3.draw(640, 400, 640, 160)
#         self.background3.draw(960, 400, 640, 160)
#         self.background1.draw(640, 160, 640, 640)
#         self.background1.draw(320, 160, 640, 640)
#         self.background1.draw(960, 160, 640, 640)
#
#         for i in range(0, 10):
#             for k in range(0, 19):
#                 if self.tile_type[i][k] == 1:
#                     self.normal_block.draw(32 + 64 * k, 608 - i * 64, 64, 64)
#                 elif self.tile_type[i][k] == 2:
#                     self.wall_block.draw(32 + 64 * k, 608 - i * 64, 64, 64)

def move_event():
    global game
    global state
    global claiming
    global frame
    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                state = 1
            elif event.key == SDLK_LEFT:
                state = -1
            elif event.key == SDLK_UP:
                state = 2
            elif event.key == SDLK_DOWN:
                state = -2
            elif event.key == SDLK_x:
                state = 3
            elif event.key == SDLK_z:
                state = -3
            elif event.key == SDLK_ESCAPE:
                game = False
        elif event.type == SDL_KEYUP:
            frame = 0
            if event.key == SDLK_UP or event.key == SDLK_DOWN:
                if not claiming:
                    state = 0
            else:
                state = 0
        elif event.type == SDL_QUIT:
                game = False
    pass

while game:
    clear_canvas()

    if state == 0:
        character_idle.clip_draw(frame * 64, 0, 64, 64, x, y)
    elif state == 1:
        character_run_right.clip_draw(frame * 64, 0, 64, 64, x, y)
    elif state == -1:
        character_run_left.clip_draw(frame * 64, 0, 64, 64, x, y)
    elif state == 2 or state == -2:
        character_up_down.clip_draw(frame * 64, 0, 64, 64, x, y)
    elif state == 3:
        character_action_right.clip_draw(frame * 64, 0, 64, 64, x, y)
    elif state == -3:
        character_action_left.clip_draw(frame * 64, 0, 64, 64, x, y)
    update_canvas()
    move_event()

    if state == 0:
        frame = (frame + 1) % 11
        delay(0.04)
    elif state == 1:
        frame = (frame + 1) % 11
        delay(0.04)
    elif state == -1:
        frame = (frame - 1) % 11
        delay(0.04)
    elif state == 2 or state == -2:
        frame = (frame + 1) % 6
        delay(0.04)
    elif state == 3:
        frame = (frame + 1) % 9
        delay(0.04)
    elif state == -3:
        frame = (frame - 1) % 9
        delay(0.04)

    if state == 1:
        x += 4
    if state == -1:
        x -= 4
    if state == 2:
        y += 4
    if state == -2:
        y -= 4

close_canvas()
