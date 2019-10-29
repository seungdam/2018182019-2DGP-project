from pico2d import *
import game_framework
import title_state

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


# ---------------------------- 주인공 객체 ---------------------------------------
# -------------------------------------------------------------------------------

class Player:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.state = 0
        self.frame = 0
        self.speed = 4
        self.fallSpeed = 5
        self.idle = load_image('chip\\character_idle.png')
        self.run_right = load_image('chip\\character_run_right.png')
        self.run_left = load_image('chip\\character_run_left.png')
        self.up_down = load_image('chip\\character_updown2.png')
        self.action_right = load_image('chip\\character_action_right.png')
        self.action_left = load_image('chip\\character_action_left.png')
        self.falling = True
        self.left = self.x - 22
        self.top = self.y + 20
        self.right = self.x + 22
        self.bottom = self.y - 32
        self.objectNum = 0

    pass

    def update(self):
        if self.falling:
            self.y -= self.fallSpeed

        if self.state == 0:
            self.frame = (self.frame + 1) % 11
            delay(0.04)
        elif self.state == 1:
            self.frame = (self.frame + 1) % 11
            delay(0.04)
        elif self.state == -1:
            self.frame = (self.frame - 1) % 11
            delay(0.04)
        elif self.state == 2 or self.state == -2:
            self.frame = (self.frame + 1) % 6
            delay(0.04)
        elif self.state == 3:
            self.frame = 8
            delay(0.04)
        elif self.state == -3:
            self.frame = 1
            delay(0.04)



        if self.state == 1:
            self.speed = 4
            self.x += self.speed
        if self.state == -1:
            self.speed = -4
            self.x += self.speed
        if self.state == 2:
            self.speed = 4
            self.y += self.speed
        if self.state == -2:
            self.speed = -4
            self.y += self.speed

    pass

    def update_rect(self):
        self.left = self.x - 22
        self.top = self.y + 20
        self.right = self.x + 22
        self.bottom = self.y - 32

    def draw(self):
        draw_rectangle(self.left, self.top, self.right, self.bottom)
        if self.state == 0:
            self.idle.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)
        elif self.state == 1:
            self.run_right.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)
        elif self.state == -1:
            self.run_left.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)
        elif self.state == 2 or self.state == -2:
            self.up_down.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)
        elif self.state == 3:
            self.action_right.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)
        elif self.state == -3:
            self.action_left.clip_draw(self.frame * image_sizeW, 0, image_sizeW, image_sizeH, self.x, self.y)

    def collision(self):
        pass


# ---------------------------- 적 객체 ---------------------------------------
# ---------------------------------------------------------------------------

class Enemy:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.state = 0
        self.frame = 0
        self.speed = 4
        self.fallSpeed = 5
        # self.idle = load_image('chip\\character_idle.png')
        # self.run_right = load_image('chip\\character_run_right.png')
        # self.run_left = load_image('chip\\character_run_left.png')
        # self.up_down = load_image('chip\\character_updown2.png')
        # self.action_right = load_image('chip\\character_action_right.png')
        # self.action_left = load_image('chip\\character_action_left.png')
        self.falling = True
        self.left = self.x - 22
        self.top = self.y + 20
        self.right = self.x + 22
        self.bottom = self.y - 32
        self.objectNum = 0

    pass

    def update(self):
        pass

    def update_rect(self):
        self.left = self.x - 22
        self.top = self.y + 20
        self.right = self.x + 22
        self.bottom = self.y - 32

    def draw(self):
        pass


# ------------------------------맵 오브젝트---------------------------------------
# -------------------------------------------------------------------------------


class DownBlock:
    global player
    image = None

    def __init__(self, pos):
        if DownBlock.image is None:
            self.image = load_image('chip\\block4.png')
        self.x = pos[0]
        self.y = pos[1]
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32

        self.drawing = True
        pass

    def check_collision(self):
        if player.left < self.right and player.right > self.left and player.bottom <= self.top and player.top >= self.bottom and player.falling:
            player.falling = False
            if player.bottom <= self.top:
                player.y += self.top - player.bottom

        pass

    def update(self):
        pass

    def draw(self):
        if self.drawing:
            self.image.draw(self.x, self.y, image_sizeW, image_sizeH)
        # draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass


# -------------------------------------------------------------

class LeftBlock:
    global player

    def __init__(self, pos):
        self.image = load_image('chip\\block3.png')
        self.x = pos[0]
        self.y = pos[1]
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32
        self.drawing = True

        pass

    def update(self):
        pass

    def check_collision(self):
        if player.left < self.right and player.right > self.left and player.bottom <= self.top and player.top >= self.bottom:
            if player.left <= self.right:
                player.x += self.right - player.left
        pass

    def draw(self):
        if self.drawing:
            self.image.draw(self.x, self.y, image_sizeW, image_sizeH)
        # draw_rectangle(self.left, self.top, self.right, self.bottom)

        pass


class RightBlock:
    global player
    image = None

    def __init__(self, pos):
        if RightBlock.image is None:
            self.image = load_image('chip\\block3.png')
        self.x = pos[0]
        self.y = pos[1]
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32
        self.drawing = True

        pass

    def update(self):
        pass

    def check_collision(self):
        if player.left < self.right and player.right > self.left and player.bottom <= self.top and player.top >= self.bottom:
            if player.right >= self.left:
                player.x -= player.right - self.left
        pass

    def draw(self):
        if self.drawing:
            self.image.draw(self.x, self.y, image_sizeW, image_sizeH)
        # draw_rectangle(self.left, self.top, self.right, self.bottom)

        pass

#---------------------- 위 코드의 경우 충돌체크 부분을 합칠 예정 -----------

class CrushBlock:
    global player

    def __init__(self, pos):
        self.image = load_image('chip\\Terrain (16x16)_9.png')
        self.x = pos[0]
        self.y = pos[1]
        self.left = self.x - 32
        self.top = self.y + 32
        self.right = self.x + 32
        self.bottom = self.y - 32
        self.fill = True
        pass

    def update(self):
        pass

    def check_collision(self):
        if player.left < self.right and player.right > self.left and player.bottom <= self.top and player.top >= self.bottom and player.falling and self.fill:
            player.falling = False
            if player.bottom <= self.top:
                player.y += self.top - player.bottom
        pass

    def crush(self):
        if player.right <= self.left and player.left >= self.left - 64 and self.top <= player.y <= self.top + 32:
            if player.state == 3:
                self.fill = False
        if player.left >= self.right and player.right <= self.right + 64 and self.top <= player.y <= self.top + 32:
            if player.state == -3:
                self.fill = False

    def draw(self):
        if self.fill:
            self.image.draw(self.x, self.y, image_sizeW, image_sizeH)
            # draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass


class Flag:
    global player, stageClear

    def __init__(self, pos):
        self.noFlagImage = load_image('chip\\check_point_noflag.png')
        self.FlagImage = load_image('chip\\check_point.png')
        self.x = pos[0]
        self.y = pos[1]
        self.frame = 0
        self.left = self.x - 10
        self.top = self.y + 32
        self.right = self.x + 10
        self.bottom = self.y - 32
        self.flagOn = False
        pass

    def update(self):
        if player.objectNum == 16:
            self.flagOn = True

        if self.flagOn:
            self.frame = (self.frame + 1) % 10
        else:
            pass
        pass

    def check_collision(self):
        if self.flagOn:
            if (player.left <= self.right and player.right >= self.left) and (
                    player.bottom <= self.top and player.top >= self.bottom):
                game_framework.quit()

        pass

    def draw(self):
        if self.flagOn:
            self.FlagImage.clip_draw(self.frame * image_sizeW, 0 , image_sizeW, image_sizeH, self.x, self.y)
        else:
            self.noFlagImage.draw(self.x, self.y)
        #   draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass


# ------------------------아이템 오브젝트-----------------------
# --------------------------------------------------------------
class Object:
    global player
    image = None

    def __init__(self, pos):
        if Object.image is None:
            self.image = load_image('chip\\Apple.png')
        self.x = pos[0]
        self.y = pos[1]
        self.frame = 0
        self.left = self.x - 10
        self.top = self.y + 10
        self.right = self.x + 10
        self.bottom = self.y - 10
        self.exist = True

        pass

    def update(self):
        self.frame = (self.frame + 1) % 17
        pass

    def check_collision(self):
        if (player.left <= self.right and player.right >= self.left) and (
                player.bottom <= self.top and player.top >= self.bottom) and self.exist:
            self.exist = False
            player.objectNum += 1

        pass

    def draw(self):
        if self.exist:
            self.image.clip_draw(self.frame * 32, 0, 32, 32, self.x, self.y)
        # draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass


# ---------------------물리적용 처리 함수-------------------------
# ---------------------------------------------------------------

def interact():
    player.falling = True
    for i in range(0, 33):
        blockList[i].check_collision()
    for i in crushBlockList:
        i.check_collision()
        i.crush()
    for i in objectList:
        i.check_collision()
    flag.check_collision()


# --------------- 스테이지 1 State 처리 함수 -----------
# ----------------------------------------------------

def enter():
    global player, count, backGround, flag, blockList, crushBlockList, objectList
    player = Player((480, 500))
    backGround = load_image('chip\\realBackGround.png')

    for i in range(0, 10):
        for k in range(0, 19):
            if tile_type[i][k] == 1:
                blockList.append(DownBlock((32 + 64 * k, 608 - i * 64)))
                count += 1
            elif tile_type[i][k] == 2:
                blockList.append(LeftBlock((32 + 64 * k, 608 - i * 64)))
                count += 1
            elif tile_type[i][k] == 3:
                crushBlockList.append(CrushBlock((32 + 64 * k, 608 - i * 64)))
            elif tile_type[i][k] == 4:
                blockList.append(RightBlock((32 + 64 * k, 608 - i * 64)))
                count += 1
            elif tile_type[i][k] == 6:
                flag = Flag((32 + 64 * k, 608 - i * 64))

    for i in range(0, 6):
        objectList.append(Object((520 + i * 30, 470)))
    for k in range(0, 3):
        objectList.append(Object((540 + k * 50, 340)))
    for j in range(0, 7):
        objectList.append(Object((540 + j * 50, 80)))

    pass


def exit():
    global player, blockList, objectList, crushBlockList
    del player
    del blockList
    del objectList
    del crushBlockList
    pass


def resume():
    pass


def pause():
    pass


def handle_events():
    global player
    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT and not player.falling:
                player.state = 1
            elif event.key == SDLK_LEFT and not player.falling:
                player.state = -1
            elif event.key == SDLK_UP and not player.falling:
                player.state = 2
            elif event.key == SDLK_DOWN and not player.falling:
                player.state = -2
            elif event.key == SDLK_x and not player.falling:
                player.state = 3
            elif event.key == SDLK_z and not player.falling:
                player.state = -3
            elif event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_p:
                game_framework.change_state(tile_state)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP or event.key == SDLK_DOWN:
                player.state = 0
                pass
            else:
                player.state = 0
        elif event.type == SDL_QUIT:
            game_framework.quit
    pass


def draw():
    clear_canvas()
    backGround.draw(640, 320)
    for i in blockList:
        i.draw()
    for i in crushBlockList:
        i.draw()
    player.draw()
    for i in objectList:
        i.draw()
    flag.draw()
    update_canvas()


def update():
    player.update()
    player.update_rect()
    for i in objectList:
        i.update()
    flag.update()
    interact()
