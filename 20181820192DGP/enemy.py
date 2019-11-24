from pico2d import *
import stage1_state
import game_framework

image_sizeW = 64
image_sizeH = 64

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

RUN, IDLE = range(2)
LEFT, RIGHT = range(2)


class Monster1:
    def __init__(self, pos):
        self.run = load_image('chip\\enemy\\run.png')
        self.idle = load_image('chip\\enemy\\idle.png')
        self.x = pos[0]
        self.y = pos[1]
        self.state = RUN  # 0 일때 정지 상태 1일때 움직이는 상태
        self.frame = 0
        self.dir = 1
        self.change_dir_time = 700

        self.velocity = RUN_SPEED_PPS
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32
        self.sleep = False  # 플레이어가 오브젝트를 먹는 순간 해제
        self.intersect_wall = False
        self.restore = 1000
        pass

    def get_bb(self):
        return self.x - 32, self.y + 32, self.x + 32, self.y - 32

    def sleep_off(self):
        player = new_stage1_state.get_ohdam_info()
        if player.objectNum > 0:
            self.sleep = False

    def become_block(self,crushBlock):
        self.x = crushBlock.x
        self.y = crushBlock.y
        self.state = IDLE
        pass

    def update(self):
        player = new_stage1_state.get_ohdam_info()
        if not self.sleep:
            if self.state is RUN:
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12
                if self.dir is RIGHT:
                    self.x += self.velocity * game_framework.frame_time
                elif self.dir is LEFT:
                    self.x -= self.velocity * game_framework.frame_time
                self.change_dir_time -= 1
                if self.change_dir_time < 0 or self.intersect_wall:
                    self.change_dir_time = 1000
                    if self.dir is RIGHT:
                        self.dir = LEFT
                    else:
                        self.dir = RIGHT

            elif self.state is IDLE:
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        pass

    def get_bb(self):
        return self.x - 32, self.y + 32, self.x + 32, self.y - 32

    def late_update(self):
        player = new_stage1_state.get_ohdam_info()
        if self.state is IDLE:
            if player.falling:
                player.falling = False
                if player.bottom < self.top:
                    player.y += (self.top - player.bottom)
        else:
            pass
        pass

    def draw(self):
        if self.state is RUN:
            if self.dir is RIGHT:
                self.run.clip_draw(int(self.frame) * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)
            elif self.dir is LEFT:
                self.run.clip_composite_draw(int(self.frame) * image_sizeW, 0, image_sizeW, image_sizeH, 0.0, 'h',
                                             self.x, self.y ,image_sizeW,image_sizeH)
        elif self.state is IDLE:
            self.idle.clip_draw(int(self.frame) * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)

        draw_rectangle(*self.get_bb())
        pass
