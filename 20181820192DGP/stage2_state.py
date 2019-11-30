from pico2d import *
import game_framework
import game_world
import level_select_state
from ohdam import Ohdam
from background import BackGround
from crush import CrushBlock
from flour import FlourBlock
from wall import WallBlock
from lebber import LebberTop
from lebber import LebberMid
from lebber import LebberBottom
from flag import Flag
from apple import Apple
from enemy import Monster1

name = 'Stage2State'

player = None
flourBlockList = []
wallBlockList = []
lebberList = []
crushBlockList = []
objectList = []
enemy = None

image_sizeW = 64
image_sizeH = 64

count = 0

backGround = None
flag = None

tile_type = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5      464
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6      432
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7      400
             [0, 0, 1, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8      368
             [0, 0, 7, 8, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9      336
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10     304
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11     272
             [0, 0, 1, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12     240
             [0, 0, 7, 8, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13     208
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 14     176
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 15     144
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16     112
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 17      80
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 18      48
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 19      16
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
    player = Ohdam((96, 610))
    game_world.add_object(player, 1)

    global backGround
    backGround = BackGround()
    game_world.add_object(backGround, 0)
    global flag
    global blockList
    for i in range(10):
        for k in range(19):
            if tile_type[i][k] is 1:
                flourBlockList.append(FlourBlock((32 + 64 * k, 608 - i * 64)))
            elif tile_type[i][k] is 2:
                wallBlockList.append(WallBlock((32 + 64 * k, 608 - i * 64)))
            elif tile_type[i][k] is 3:
                crushBlockList.append(CrushBlock((32 + 64 * k, 608 - i * 64)))
            elif tile_type[i][k] is 6:
                flag = Flag((32 + 64 * k, 608 - i * 64))
            elif tile_type[i][k] is 7:
                lebberList.append(LebberTop((32 + 64 * k, 608 - i * 64)))
            elif tile_type[i][k] is 8:
                lebberList.append(LebberMid((32 + 64 * k, 608 - i * 64)))
            elif tile_type[i][k] is 9:
                lebberList.append(LebberBottom((32 + 64 * k, 608 - i * 64)))
    game_world.add_objects(flourBlockList, 2);
    game_world.add_objects(crushBlockList, 2);
    game_world.add_objects(wallBlockList, 2);
    game_world.add_objects(lebberList, 0);
    game_world.add_object(flag, 2)
    for i in range(0, 6):
        objectList.append(Apple((400 + i * 60, 470)))
    for k in range(0, 3):
        objectList.append(Apple((600 + k * 40, 340)))
    for j in range(0, 3):
        objectList.append(Apple((920 + j * 40, 280)))
    for i in range(0, 4):
        objectList.append(Apple((600 + i * 60, 140)))

    game_world.add_objects(objectList, 2);
    global enemy
    enemy = Monster1((700, 480))
    game_world.add_object(enemy, 1);
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
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def update():
    player.update()
    enemy.update()
    for i in wallBlockList:
        i.update()
    for i in flourBlockList:
        i.update()
    for i in crushBlockList:
        i.update()
    for i in objectList:
        i.update()
    flag.update()
    player.falling = True
    player.can_up = False

    for i in wallBlockList:
        if collide(i, player):
            i.late_update()
        if collide(i, enemy):
            i.late_update2()
    for i in flourBlockList:
        if collide(i, player):
            i.late_update()
    for i in crushBlockList:
        if collide(i, player):
            i.late_update()
        if collide(i, enemy):
            if i.fill is False:
                enemy.become_block(i)
    for i in lebberList:
        if collide(i, player):
            player.can_up = True
            i.late_update()
    for i in objectList:
        if collide(player, i):
            i.late_update()
    if collide(flag, player):
        if flag.flagOn:
            game_framework.change_state(level_select_state)
    if collide(enemy, player):
        enemy.late_update()

    pass
