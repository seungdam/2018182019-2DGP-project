from pico2d import *
import game_framework
import game_world
import level_select_state
from ohdam2 import Ohdam
from background import BackGround
from block3 import CrushBlock
from block2 import FlourBlock
from flag import Flag
from lebber2 import Lebber
from enemy import Monster1
from apple import Apple

name = 'Stage1State'

mapTop = 448

mapFirst = 16

player = None
blockList = []
crushBlockList = []
lebberList = []
flourBlockList = []
objectList = []
enemy = None
enemyList = []
image_sizeW = 32
image_sizeH = 32

count = 0

backGround = None
flag = None

tile_type = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1           448
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2           416
    [0, 0, 21, 0, 0, 22, 10, 10, 20, 20, 20, 10, 10, 0, 0, 0, 0, 0, 0],  # 3  400
    [0, 1, 2, 2, 3, 22, 0, 11, 0, 0, 0, 0, 11, 22, 1, 2, 3, 0, 0],  # 4       368
    [0, 7, 8, 8, 9, 23, 0, 11, 0, 0, 12, 12, 11, 23, 7, 8, 9, 0, 0],  # 5     336
    [0, 0, 0, 0, 0, 23, 0, 11, 0, 0, 0, 0, 11, 23, 0, 0, 0, 0, 0],  # 6       304
    [0, 0, 0, 0, 0, 23, 0, 11, 12, 12, 0, 0, 11, 23, 13, 13, 0, 0, 0],  # 7   272
    [0, 1, 2, 2, 3, 23, 0, 0, 0, 0, 0, 0, 11, 23, 0, 0, 0, 13, 0],  # 8       240
    [0, 7, 8, 8, 9, 23, 0, 0, 0, 0, 0, 0, 11, 23, 0, 0, 0, 0, 0],  # 9        208
    [0, 0, 0, 0, 0, 23, 0, 12, 12, 12, 12, 12, 23, 0, 0, 25, 0, 0, 0],  # 10  176
    [0, 0, 0, 0, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 24, 0, 0, 0, 0],  # 11        144
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],  # 12          112
    [4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6],  # 13           80
    [4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6],  # 14           48
    [4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6],  # 15           16
]


def enter():
    global player
    global objectList
    global enemy
    global backGround
    global flag
    global enemyList
    backGround = BackGround()
    game_world.add_object(backGround, 0)

    enemy = Monster1((600, 96))
    game_world.add_object(enemy, 2);

    for i in range(15):
        for k in range(19):
            if tile_type[i][k] is 20:
                crushBlockList.append(CrushBlock((mapFirst + 32 * k, mapTop - i * 32)))
            elif tile_type[i][k] is 21:
                flag = Flag((mapFirst + 32 * k, mapTop - i * 32))
            elif tile_type[i][k] is 22:
                lebberList.append(Lebber((mapFirst + 32 * k, mapTop - i * 32), tile_type[i][k]))
            elif tile_type[i][k] is 23:
                lebberList.append(Lebber((mapFirst + 32 * k, mapTop - i * 32), tile_type[i][k]))
            elif tile_type[i][k] is 24:
                lebberList.append(Lebber((mapFirst + 32 * k, mapTop - i * 32), tile_type[i][k]))
            elif tile_type[i][k] is 25:
                player = Ohdam((mapFirst + 32 * k, mapTop - i * 32))
            elif tile_type[i][k] is 26:
                enemyList.append(Monster1((mapFirst + 32 * k, mapTop - i * 32)))
            elif tile_type[i][k] is 0:
                pass
            else:
                flourBlockList.append(FlourBlock((16 + 32 * k, mapTop - i * 32), tile_type[i][k]))

    game_world.add_object(flag, 3)
    game_world.add_objects(lebberList, 6);
    game_world.add_objects(flourBlockList, 3);
    game_world.add_objects(crushBlockList, 4);
    game_world.add_objects(enemyList, 2);
    game_world.add_object(player, 1)

    for i in range(0, 6):
        objectList.append(Apple((520 + i * 30, 470)))
    for k in range(0, 3):
        objectList.append(Apple((540 + k * 50, 340)))
    for j in range(0, 7):
        objectList.append(Apple((540 + j * 50, 80)))

    game_world.add_objects(objectList, 5);
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
    for i in flourBlockList:
        i.draw()
    for i in crushBlockList:
        i.draw()
    for i in objectList:
        i.draw()
    update_canvas()


def update():
    player.update()
    flag.update()
    if flag.end:
        game_framework.change_state(level_select_state)
    player.falling = True

    for i in flourBlockList:
        i.update()
    for i in crushBlockList:
        i.update()
    for i in objectList:
        i.update()
    pass
