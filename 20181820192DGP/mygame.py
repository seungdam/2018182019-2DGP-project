import game_framework
import pico2d
import title_state
import stage1_state
import stage2_state
import stage3_state
import level_select_state

pico2d.open_canvas(960, 480)
game_framework.run(stage3_state)
pico2d.close_canvas()