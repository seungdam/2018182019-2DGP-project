from pico2d import *
import game_framework
import game_world
import title_state
from player import Ohdam
from background import BackGround
from crush import CrushBlock
from flour import FlourBlock
from wall import WallBlock
name = 'Stage1State'

player = None
blockList = []
crushBlockList = []
objectList = []

image_sizeW = 64
image_sizeH = 64

count = 0

backGround = None
flag = None

tile_type = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 1
             [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],  # 2
             [0, 0, 0, 0, 2, 1, 1, 1, 3, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0],  # 3
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],  # 4
             [0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 4, 1, 1, 1, 1, 4, 0, 0],  # 5
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],  # 6
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],  # 7
             [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 6, 4, 0, 0],  # 8
             [0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0]  # 9
             ]





def enter():
    global player
    player = Ohdam((480, 500))
    game_world.add_object(player, 1)

    global backGround
    backGround = BackGround()
    game_world.add_object(backGround, 0)

    global blockList
    for i in range(10):
        for k in range(19):
            if tile_type[i][k] is 1:
                blockList.append(FlourBlock((32 + 64 * k, 608 - i * 64)))
            elif tile_type[i][k] is 2:
                blockList.append(WallBlock((32 + 64 * k, 608 - i * 64)))
            elif tile_type[i][k] is 3:
                blockList.append(CrushBlock((32 + 64 * k, 608 - i * 64)))
    for i in range(39):
        game_world.add_object(blockList[i], 1)
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
    for game_object in game_world.all_objects():
        game_object.update()
    for game_object in game_world.all_objects():
        if collide(game_object,player):
            game_object.late_update()

    pass
