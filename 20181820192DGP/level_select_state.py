from pico2d import *
import game_framework
import stage1_state
import stage2_state
name = 'TitleState'

level1_button = None
level2_button = None
level1_minimap = None
level2_minimap = None

backGround = None

mouseX = 0
mouseY = 0

change_button1 = False
change_button2 = False


def enter():
    global level1_button, level1_minimap, level2_button, level2_minimap, backGround
    if level1_button is None:
        level1_button = load_image('level_select\\level1_button.png')
    if level2_button is None:
        level2_button = load_image('level_select\\level2_button.png')
    if level1_minimap is None:
        level1_minimap = load_image('level_select\\level1.png')
    if level2_minimap is None:
        level2_minimap = load_image('level_select\\level2.png')
    if backGround is None:
        backGround = load_image('chip\\backGround\\realBackGround.png')
    pass


def exit():
    global level1_button, level1_minimap, level2_button, level2_minimap, backGround

    pass


def resume():
    pass


def pause():
    pass


def handle_events():

    global mouseX, mouseY, change_button2,change_button1
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mouseX, mouseY = event.x, 640 - 1 - event.y

            if 170 <= mouseX <= 470 and 170 <= mouseY <= 470:
                change_button1 = True
            else:
                change_button1 = False
            if 810 <= mouseX <= 1110 and 170 <= mouseY <= 470:
                change_button2 = True
            else:
                change_button2 = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if 170 <= mouseX <= 470 and 170 <= mouseY <= 470:
                game_framework.change_state(stage1_state)
            elif 810 <= mouseX <= 1110 and 170 <= mouseY <= 470:
                game_framework.change_state(stage2_state)

        else:
            if event.type == SDL_KEYDOWN:
                if event.key is SDLK_ESCAPE:
                    game_framework.quit()

                elif event.key is SDLK_s:
                    game_framework.change_state(stage1_state)

    pass


def update():

    pass


def draw():
    clear_canvas()
    print(mouseX)
    print(mouseY)
    backGround.draw(640, 320)
    if not change_button1:
        level1_button.draw(320, 320)
    else:
        level1_minimap.draw(320, 320)

    if not change_button2:
        level2_button.draw(960, 320)
    else:
        level2_minimap.draw(960, 320)

    update_canvas()
