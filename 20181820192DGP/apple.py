from pico2d import*
import game_framework
import new_stage1_state

image_sizeW = 32
image_sizeH = 32

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Apple:
    global player
    image = None

    def __init__(self, pos):
        if Apple.image is None:
            self.image = load_image('chip\\object\\Apple.png')
        self.x = pos[0]
        self.y = pos[1]
        self.frame = 0

        pass
    def get_bb(self):
        return self.x - 10, self.y + 10, self.x + 10, self.y -10


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 17
        pass

    def late_update(self):
        player = new_stage1_state.get_player_info()
        player.objectNum += 1

    def draw(self):
        self.image.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)

        pass

