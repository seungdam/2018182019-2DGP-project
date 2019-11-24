import game_framework
import pico2d

import title_state
import stage1_state
import stage2_state


pico2d.open_canvas(1280, 640)
game_framework.run(stage1_state)
pico2d.close_canvas()