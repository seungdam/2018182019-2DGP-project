from collections import namedtuple
from pico2d import *

open_canvas(1200, 800)

block = load_image('Terrain (16X16)_9.png')
wallPos = namedtuple('wallPos', 'x y')

blockPos_x = []
blockPos_y = []

for i in range(1,15):
    blockPos_x += [100 + (64*i)]
    blockPos_y += [100]


while(True):
    for i in range(0,14):
        block.draw_now(blockPos_x[i],blockPos_y[i],64,64)

