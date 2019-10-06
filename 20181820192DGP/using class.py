from pico2d import *

game = True
claiming = False
state = 0


def handle_event():
    global game
    global state
    global claiming

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
            if event.key == SDLK_UP or event.key == SDLK_DOWN:
                if not claiming:
                    state = 0
            else:
                state = 0
        elif event.type == SDL_QUIT:
            game = False
    pass


class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.frame = 0
        self.idle = load_image('test1.png')
        self.run_right = load_image('test2-r.png')
        self.run_left = load_image('test2-l.png')
        self.up_down = load_image('test3-2.png')
        self.action_right = load_image('test4-r.png')
        self.action_left = load_image('test4-l.png')
        self.state = 0

    pass

    def update(self):
        if state == 0:
            self.frame = (self.frame + 1) % 11
            delay(0.04)
        elif state == 1:
            self.frame = (self.frame + 1) % 11
            delay(0.04)
        elif state == -1:
            self.frame = (self.frame - 1) % 11
            delay(0.04)
        elif state == 2 or state == -2:
            self.frame = (self.frame + 1) % 6
            delay(0.04)
        elif state == 3:
            self.frame = (self.frame + 1) % 9
            delay(0.04)
        elif state == -3:
            self.frame = (self.frame - 1) % 9
            delay(0.04)

        if state == 1:
            self.x += 4
        if state == -1:
            self.x -= 4
        if state == 2:
            self.y += 4
        if state == -2:
            self.y -= 4

    pass

    def drawing(self):
        if state == 0:
            self.idle.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif state == 1:
            self.run_right.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif state == -1:
            self.run_left.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif state == 2 or state == -2:
            self.up_down.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif state == 3:
            self.action_right.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif state == -3:
            self.action_left.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)

    pass

open_canvas()
player = Player()

while(game):
    handle_event()
    player.update()

    clear_canvas()
    player.drawing()
    update_canvas()