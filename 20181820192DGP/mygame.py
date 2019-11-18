import game_framework
import pico2d

import title_state
import new_stage1_state


pico2d.open_canvas(1280, 640)
game_framework.run(new_stage1_state)
pico2d.close_canvas()