from pico2d import *
import game_framework
import stage1_state

name = 'TitleState'

title_image1 = None
title_image2 = None
character_image = None

timer = 0
change = True


def enter():
    global character_image, title_image1, title_image2
    title_image1 = load_image('title\\title1.png')
    title_image2 = load_image('title\\title2.png')

    pass


def exit():
    global character_image, title_image1, title_image2

    del title_image2
    del title_image1

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
        else:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    game_framework.quit()
                else:
                    game_framework.change_state(stage1_state)

    pass


def update():
    global timer

    timer += 1
    delay(0.3)


def draw():
    clear_canvas()
    if timer % 2 == 0:
        title_image1.draw(640, 320)
    else:
        title_image2.draw(640, 320)
    update_canvas()
