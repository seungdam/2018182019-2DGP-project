from pico2d import *
import game_framework
import game_world
import level_select_state
from ohdam import Ohdam
from background import BackGround
from block3 import CrushBlock
from block2 import FlourBlock
from flag import Flag
from wall import WallBlock
from enemy import Monster1
from apple import Apple

name = 'Stage1State'

player = None
blockList = []
crushBlockList = []
flourBlockList = []
wallBlockList = []
objectList = []
enemy = None
image_sizeW = 64
image_sizeH = 64

count = 0

backGround = None
flag = None

tile_type = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
             [0, 0, 0, 0, 13, 22, 0, 0, 0, 0, 0,   13, 0, 0, 0, 0, 0, 0, 0],  # 1
             [0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0,  14, 0, 0, 0, 0, 0, 0, 0],  # 2
             [0, 0, 0, 0, 1, 2, 2, 3, 20, 20, 20, 3, 0, 0, 0, 0, 0, 0, 0],  # 3
             [0, 0, 0, 0, 4, 5, 5, 6, 0, 0, 0,    13, 0, 0, 0, 0, 1, 2, 3],  # 4
             [0, 0, 0, 0, 4, 5, 5, 6, 20, 20, 20, 14, 0, 0, 0, 0, 4, 5, 6],  # 5
             [0, 0, 0, 0, 4, 5, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 6],  # 6
             [0, 0, 0, 0, 4, 5, 5, 6, 0, 0, 0, 0, 0, 0, 0, 21, 4, 5, 6],  # 7
             [0, 0, 0, 0, 4, 5, 5, -4, 2, 2, 2, 2, 2, 2, 2, 2, -1, 5, 6],  # 8
             [0, 0, 0, 0, 4, 5, 5, -5, 5, 5, 5, 5, 5, 5, 5, 5, -2, 5, 6]  # 9
             ]


def collide(a, b):
    left_a, top_a, right_a, bottom_a = a.get_bb()
    left_b, top_b, right_b, bottom_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global player
    global objectList
    global enemy
    global backGround
    global flag


    backGround = BackGround()
    game_world.add_object(backGround, 0)



    for i in range(10):
        for k in range(19):
            if tile_type[i][k] is 20:
                crushBlockList.append(CrushBlock((32 + 64 * k, 608 - i * 64)))
            elif tile_type[i][k] is 21:
                flag = Flag((32 + 64 * k, 608 - i * 64))
            elif tile_type[i][k] is 22:
                player = Ohdam((32 + 64 * k, 608 - i * 64))
            elif tile_type[i][k] is 0:
                pass
            else:
                flourBlockList.append(FlourBlock((32 + 64 * k, 608 - i * 64), tile_type[i][k]))

    game_world.add_object(flag, 2)
    game_world.add_objects(flourBlockList, 2);
    game_world.add_objects(crushBlockList, 2);
    game_world.add_objects(wallBlockList, 2);
    game_world.add_object(player, 1)
    enemy = Monster1((600, 96))
    game_world.add_object(enemy, 1);

    for i in range(0, 6):
        objectList.append(Apple((520 + i * 30, 470)))
    for k in range(0, 3):
        objectList.append(Apple((540 + k * 50, 340)))
    for j in range(0, 7):
        objectList.append(Apple((540 + j * 50, 80)))
    game_world.add_objects(objectList, 2);
    pass


def exit():
    game_world.clear()
    pass


def resume():
    pass


def pause():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            player.handle_event(event)
    pass


def draw():
    clear_canvas()
    backGround.draw()
    player.draw()
    flag.draw()
    player.draw()
    enemy.draw()
    for i in wallBlockList:
        i.draw()
    for i in flourBlockList:
        i.draw()
    for i in crushBlockList:
        i.draw()
    for i in objectList:
        i.draw()
    update_canvas()


def update():
    player.update()
    enemy.update()
    flag.update()

    player.falling = True
    for i in wallBlockList:
        i.update()
    for i in flourBlockList:
        i.update()
    for i in crushBlockList:
        i.update()
    for i in objectList:
        i.update()

    for i in wallBlockList:
        if collide(i, player):
            i.late_update()
        if collide(i, enemy):
            i.late_update2()
    for i in objectList:
        if collide(i, player):
            i.late_update()

    if collide(enemy, player):
        enemy.late_update()

    if collide(flag, player):
        if flag.flagOn:
            game_framework.change_state(level_select_state)

    pass
