from pico2d import *
import game_framework
import stage1_state
import stage2_state
import stage3_state
name = 'LevelSelectState'

level1 = None
level2 = None
level3 = None
wav = None
backGround = None

mouseX = 0
mouseY = 0


def enter():
    global level3, level1, level2, backGround, wav
    if level1 is None:
        level1 = load_image('level_select\\01.png')
    if level2 is None:
        level2 = load_image('level_select\\02.png')
    if level3 is None:
        level3 = load_image('level_select\\03.png')
    if backGround is None:
        backGround = load_image('chip\\backGround\\BackGround2.png')
    if wav is None:
        wav = load_wav('sound\\button_sound.wav')
        wav.set_volume(50)
    pass


def exit():
    pass


def resume():
    pass


def pause():
    pass


def handle_events():
    global mouseX, mouseY, change_button2, change_button1,wav
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mouseX = event.x
            mouseY = 640 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if 320 - 64 <= mouseX <= 320 + 64 and 320 - 64 <= mouseY <= 320 + 64:
                wav.play()
                game_framework.change_state(stage1_state)
            elif 640 - 64 <= mouseX <= 640 + 64 and 320 - 64 <= mouseY <= 320 + 64:
                wav.play()
                game_framework.change_state(stage2_state)
            elif 960 - 64 <= mouseX <= 960 + 64 and 320 - 64 <= mouseY <= 320 + 64:
                wav.play()
                game_framework.change_state(stage3_state)

        else:
            if event.type == SDL_KEYDOWN:
                if event.key is SDLK_ESCAPE:
                    game_framework.quit()

    pass


def update():
    pass


def draw():
    clear_canvas()
    print(mouseX)
    print(mouseY)
    backGround.draw(640, 320)
    level1.draw(320, 320, 128, 128)
    level2.draw(640, 320, 128, 128)
    level3.draw(960, 320, 128, 128)

    update_canvas()
