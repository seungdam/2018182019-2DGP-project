from pico2d import *
import game_framework

image_sizeW = 64
image_sizeH = 64

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

RIGHT_KEY_DOWN, LEFT_KEY_DOWN, UP_KEY_DOWN, DOWN_KEY_DOWN, Z_KEY_DOWN, X_KEY_DOWN, RIGHT_KEY_UP, LEFT_KEY_UP, UP_KEY_UP, DOWN_KEY_UP, Z_KEY_UP, X_KEY_UP = range(
    12)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_KEY_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_KEY_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_KEY_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_KEY_UP,

    (SDL_KEYDOWN, SDLK_x): X_KEY_DOWN,
    (SDL_KEYDOWN, SDLK_z): Z_KEY_DOWN,
    (SDL_KEYUP, SDLK_x): X_KEY_UP,
    (SDL_KEYUP, SDLK_z): Z_KEY_UP,

    (SDL_KEYDOWN, SDLK_DOWN): DOWN_KEY_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_KEY_DOWN,
    (SDL_KEYUP, SDLK_DOWN): DOWN_KEY_UP,
    (SDL_KEYUP, SDLK_UP): UP_KEY_UP,
}


class IdleState:
    @staticmethod
    def enter(ohdam, event):
        if event == RIGHT_KEY_DOWN:
            ohdam.velocity += RUN_SPEED_PPS
        elif event == LEFT_KEY_DOWN:
            ohdam.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_KEY_UP:
            ohdam.velocity -= RUN_SPEED_PPS
        elif event == LEFT_KEY_UP:
            ohdam.velocity += RUN_SPEED_PPS

        ohdam.dir = clamp(-1, ohdam.velocity, 1)

    @staticmethod
    def exit(ohdam, event):
        pass

    @staticmethod
    def do(ohdam):
        ohdam.frame = (ohdam.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11

    @staticmethod
    def draw(ohdam):
         ohdam.idle.clip_draw(int(ohdam.frame) * image_sizeW, 0, image_sizeW, image_sizeH, ohdam.x, ohdam.y)


class RunState:
    @staticmethod
    def enter(ohdam, event):
        if event == RIGHT_KEY_DOWN:
            ohdam.velocity += RUN_SPEED_PPS
        elif event == LEFT_KEY_DOWN:
            ohdam.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_KEY_UP:
            ohdam.velocity -= RUN_SPEED_PPS
        elif event == LEFT_KEY_UP:
            ohdam.velocity += RUN_SPEED_PPS
        ohdam.dir = clamp(-1, ohdam.velocity, 1)

    @staticmethod
    def exit(ohdam, event):

        pass

    @staticmethod
    def do(ohdam):
        ohdam.frame = (ohdam.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12
        if not ohdam.falling:
            ohdam.x += ohdam.velocity * game_framework.frame_time

    @staticmethod
    def draw(ohdam):
        if ohdam.dir is 1:
            ohdam.run_right.clip_draw(int(ohdam.frame) * image_sizeW, 0, image_sizeW, image_sizeH, ohdam.x,
                                      ohdam.y)
        else:
            ohdam.run_left.clip_draw(int(ohdam.frame) * image_sizeW, 0, image_sizeW, image_sizeH, ohdam.x, ohdam.y)

    pass


class LeftActionState:
    @staticmethod
    def enter(ohdam, event):
        ohdam.do_left_action = True
        pass

    @staticmethod
    def exit(ohdam, event):
        ohdam.do_left_action = False
        pass

    @staticmethod
    def do(ohdam):
        ohdam.frame = (ohdam.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

    @staticmethod
    def draw(ohdam):
        ohdam.action_left.clip_draw(int(ohdam.frame) * 64, 0, 64, 64, ohdam.x, ohdam.y)


class RightActionState:
    @staticmethod
    def enter(ohdam, event):
        ohdam.do_right_action = True
        pass

    @staticmethod
    def exit(ohdam, event):
        ohdam.do_right_action = False
        pass

    @staticmethod
    def do(ohdam):
        ohdam.frame = (ohdam.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

    @staticmethod
    def draw(ohdam):
        ohdam.action_right.clip_draw(int(ohdam.frame) * 64, 0, 64, 64, ohdam.x, ohdam.y)


class ClimbingState:
    @staticmethod
    def enter(ohdam, event):
        if event == UP_KEY_DOWN:
            ohdam.velocity += RUN_SPEED_PPS
        elif event == DOWN_KEY_DOWN:
            ohdam.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_KEY_UP:
            ohdam.velocity -= RUN_SPEED_PPS
        elif event == LEFT_KEY_UP:
            ohdam.velocity += RUN_SPEED_PPS

    @staticmethod
    def exit(ohdam, event):
        pass

    @staticmethod
    def do(ohdam):
        ohdam.frame = (ohdam.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        ohdam.y += ohdam.velocity * game_framework.frame_time

    @staticmethod
    def draw(ohdam):
        ohdam.up_down.clip_draw(int(ohdam.frame) * image_sizeW, image_sizeH, image_sizeW, image_sizeH, ohdam.x, ohdam.y)


next_state_table = {
    IdleState: {RIGHT_KEY_UP: IdleState, LEFT_KEY_UP: IdleState, RIGHT_KEY_DOWN: RunState, LEFT_KEY_DOWN: RunState,
                Z_KEY_UP: IdleState, X_KEY_UP: IdleState, Z_KEY_DOWN: LeftActionState, X_KEY_DOWN: RightActionState,
                UP_KEY_UP: IdleState, DOWN_KEY_UP: IdleState, UP_KEY_DOWN: IdleState, DOWN_KEY_DOWN: IdleState,
                },
    RunState: {RIGHT_KEY_UP: IdleState, LEFT_KEY_UP: IdleState, LEFT_KEY_DOWN: RunState, RIGHT_KEY_DOWN: RunState,
               Z_KEY_UP: RunState, X_KEY_UP: RunState, Z_KEY_DOWN: LeftActionState, X_KEY_DOWN: RightActionState,
               UP_KEY_UP: RunState, DOWN_KEY_UP: RunState, UP_KEY_DOWN: RunState, DOWN_KEY_DOWN: RunState,
               },
    LeftActionState: {RIGHT_KEY_UP: IdleState, LEFT_KEY_UP: IdleState, LEFT_KEY_DOWN: RunState,
                      RIGHT_KEY_DOWN: RunState,
                      Z_KEY_UP: IdleState, X_KEY_UP: IdleState, Z_KEY_DOWN: LeftActionState,
                      X_KEY_DOWN: RightActionState,
                      UP_KEY_UP: IdleState, DOWN_KEY_UP: IdleState, UP_KEY_DOWN: IdleState, DOWN_KEY_DOWN: IdleState,
                      },
    RightActionState: {RIGHT_KEY_UP: IdleState, LEFT_KEY_UP: IdleState, LEFT_KEY_DOWN: RunState,
                       RIGHT_KEY_DOWN: RunState,
                       Z_KEY_UP: IdleState, X_KEY_UP: IdleState, Z_KEY_DOWN: LeftActionState,
                       X_KEY_DOWN: RightActionState,
                       UP_KEY_UP: IdleState, DOWN_KEY_UP: IdleState, UP_KEY_DOWN: IdleState, DOWN_KEY_DOWN: IdleState,
                       },
}


class Ohdam:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.dir = 1
        self.frame = 0
        self.velocity = 0
        self.idle = load_image('chip\\character\\character_idle.png')
        self.run_right = load_image('chip\\character\\character_run_right.png')
        self.run_left = load_image('chip\\character\\character_run_left.png')
        self.up_down = load_image('chip\\character\\character_updown2.png')
        self.action_right = load_image('chip\\character\\character_action_right.png')
        self.action_left = load_image('chip\\character\\character_action_left.png')
        self.falling = True
        self.do_left_action = False
        self.do_right_action = False
        self.objectNum = 0

        self.font = load_font('chip\\font\\ENCR10B.TTF', 16)

        self.left = self.x - 22
        self.top = self.y + 20
        self.right = self.x + 22
        self.bottom = self.y - 32

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    pass

    def ohdam_dead(self):
        game_framework.quit()

    def get_bb(self):
        return self.x - 22, self.y + 20, self.x + 22, self.y - 32

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        if self.falling:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        self.left = self.x - 22
        self.top = self.y + 20
        self.right = self.x + 22
        self.bottom = self.y - 32

    def late_update(self):

        pass

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 20, self.y + 20, '(x: %3.2f y: %3.2f)' % (self.x, self.y), (255, 255, 0))
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

