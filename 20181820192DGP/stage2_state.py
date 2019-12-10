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
from enemy2 import Monster2
from apple import Apple

name = 'Stage2State'

mapTop = 608

mapFirst = 32

player = None
blockList = []
crushBlockList = []
lebberList = []
flourBlockList = []
objectList = []
enemy = None
enemyList = []
image_sizeW = 64
image_sizeH = 64
music = None
count = 0

backGround = None
flag = None

# 1 - 3 block wall crush block
# 4 - 6 lebber
# 7 player respone
# 8 enemy respone
# 9 flag
# object -1
# side lebber -2
tile_type = [
    # 32 96
    [0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0  608
    [0, 0, 1, 1, 1, 4, 0, 0, 0, 0, 4, 1, 1, 0, 4, 1, 4, 0, 0, 0],  # 1  544
    [0, 0, 0, 0, 0, 5, 0, 0, 1, 1, 5, 0, 0, 0, 5, 0, 5, 0, 0, 0],  # 2  480
    [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 1, 3, 0, 5, 0, 5, 0, 0, 0],  # 3  416
    [0, 0, 0, 1, 1, 5, 0, 0, 1, 1, 5, 0, 0, 0, 5, 1, 5, 0, 0, 0],  # 4  352
    [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 1, 1, 0, 5, 0, 6, 0, 9, 0],  # 5  288
    [0, 0, 0, 1, 1, 5, 0, 0, 0, 0, 5, 0, 0, 0, 5, 0, 1, 1, 1, 0],  # 6  224
    [0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 8, 0, 0],  # 7  160
    [0, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 1, 1, 3, 3, 1, 0],  # 8  96
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 9  32
]


def enter():
    global player
    global objectList
    global backGround
    global flag
    global enemyList
    backGround = BackGround(2)
    game_world.add_object(backGround, 0)

    global music
    music = load_music('sound\\stage.mp3')
    music.set_volume(60)
    music.repeat_play()

    for i in range(10):
        for k in range(20):
            if tile_type[i][k] is 3:
                crushBlockList.append(CrushBlock((mapFirst + image_sizeW * k, mapTop - i * image_sizeH)))
            elif tile_type[i][k] is 4:
                lebberList.append(Lebber((mapFirst + image_sizeW * k, mapTop - i * image_sizeH), tile_type[i][k]))
            elif tile_type[i][k] is 5:
                lebberList.append(Lebber((mapFirst + image_sizeW * k, mapTop - i * image_sizeH), tile_type[i][k]))
            elif tile_type[i][k] is 6:
                lebberList.append(Lebber((mapFirst + image_sizeW * k, mapTop - i * image_sizeH), tile_type[i][k]))
            elif tile_type[i][k] is 7:
                player = Ohdam((mapFirst + image_sizeW * k, mapTop - i * image_sizeH))
            elif tile_type[i][k] is 8:
                enemyList.append(Monster1((mapFirst + image_sizeW * k, mapTop - i * image_sizeH)))
            elif tile_type[i][k] is 9:
                flag = Flag((mapFirst + image_sizeW * k, mapTop - i * image_sizeH))
            elif tile_type[i][k] is 0:
                pass
            else:
                flourBlockList.append(
                    FlourBlock((mapFirst + image_sizeW * k, mapTop - i * image_sizeH), tile_type[i][k]))

    enemyList.append(Monster2((32 + 64 * 5, 480)))
    enemyList.append(Monster2((32 + 64 * 10, 480)))
    enemyList.append(Monster2((32 + 64 * 14, 480)))
    enemyList.append(Monster2((32 + 64 * 16, 480)))

    game_world.add_object(flag, 5)
    game_world.add_objects(lebberList, 1);
    game_world.add_objects(flourBlockList, 3);
    game_world.add_objects(crushBlockList, 4);
    game_world.add_objects(enemyList, 2);
    game_world.add_object(player, 6)

    for i in range(0, 6):
        objectList.append(Apple((32 + 64 * 5, 544 - i * 64)))
    for i in range(1, 6):
        objectList.append(Apple((32 + 64 * 10, 544 - i * 64)))
    for i in range(0, 6):
        objectList.append(Apple((32 + 64 * 14, 544 - i * 64)))
    for i in range(0, 5):
        objectList.append(Apple((32 + 64 * 16, 544 - i * 64)))
    for i in range(0, 2):
        objectList.append(Apple((32 + 64 * 10 + 64 * i, 608)))
    for i in range(0, 2):
        objectList.append(Apple((32 + 64 * 10 + 64 * i, 480)))
    for i in range(0, 2):
        objectList.append(Apple((32 + 64 * 10 + 64 * i, 352)))
    for i in range(0, 2):
        objectList.append(Apple((32 + 64 * 10 + 64 * i, 352)))

    for k in range(0, 2):
        objectList.append(Apple((32 + 64 * 8 + k * 64, 544)))
    for k in range(0, 2):
        objectList.append(Apple((32 + 64 * 8 + k * 64, 416)))
    for k in range(0, 2):
        objectList.append(Apple((32 + 64 * 3 + k * 64, 416)))
    for k in range(0, 2):
        objectList.append(Apple((32 + 64 * 3 + k * 64, 288)))

    game_world.add_objects(objectList, 7);
    pass


def exit():
    global music
    global objectList
    global blockList
    global flourBlockList
    global lebberList
    music.stop()
    lebberList.clear()
    crushBlockList.clear()
    flourBlockList.clear()
    objectList.clear()
    enemyList.clear()
    game_world.clear()
    pass


def resume():
    pass


def pause():
    pass


def handle_events():
    global player
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(level_select_state)
        else:
            player.handle_event(event)
    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def update():
    if flag.end:
        game_framework.change_state(level_select_state)

    for game_object in game_world.all_objects():
        game_object.update()

    player.falling = True
    for i in enemyList:
        i.falling = True

    for game_object in game_world.all_objects():
        game_object.late_update()

    pass
