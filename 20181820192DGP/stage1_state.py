from pico2d import *
import game_framework
import game_world
import title_state
from ohdam import Ohdam
from background import BackGround
from crush import CrushBlock
from flour import FlourBlock
from flag import Flag
from wall import WallBlock
from enemy import Monster1

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
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 1
             [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],  # 2
             [0, 0, 0, 0, 2, 1, 1, 1, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0],  # 3
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],  # 4
             [0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 2, 1, 1, 1, 1, 2, 0, 0],  # 5
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],  # 6
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],  # 7
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 6, 2, 0, 0],  # 8
             [0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 3, 3, 3, 3, 2, 0, 0]  # 9
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
    player = Ohdam((480, 500))
    game_world.add_object(player, 1)

    global enemy
    enemy = Monster1((600, 96))
    game_world.add_object(enemy, 1);

    global backGround
    backGround = BackGround()
    game_world.add_object(backGround, 0)

    global flag

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

    game_world.add_object(flag, 2)
    game_world.add_objects(flourBlockList, 2);
    game_world.add_objects(crushBlockList, 2);
    game_world.add_objects(wallBlockList, 2);

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
    update_canvas()


def update():

    player.update()
    enemy.update()
    flag.update()

    for i in wallBlockList:
        i.update()
    for i in flourBlockList:
        i.update()
    for i in crushBlockList:
        i.update()

    player.falling = True
    for i in wallBlockList:
        if collide(i, player):
            i.late_update()
        if collide(i, enemy):
            i.late_update2()
    for i in flourBlockList:
        if collide(i, player):
            i.late_update()
        if collide(i, enemy):
            i.late_update2()
    for i in crushBlockList:
        if collide(i, player):
            i.late_update()
        if collide(i, enemy):
            if i.fill:
                i.late_update2()
            elif not i.fill:
                enemy.become_block(i)

    if collide(enemy, player):
        enemy.late_update()
    if collide(flag, player):
        flag.late_update()

    pass
