from pico2d import *

game = True
action = 0


def handle_event():
    global game

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game = False
    pass


class Block:
    global action

    def __init__(self):
        self.x = 0
        self.y = 0
        self.frame = 0
        self.idle = load_image('block1.png')
        self.state = 0
        self.rectX1 = 0
        self.rectY1 = 0
        self.rectX2 = 0
        self.rectY2 = 0
        self.draw = True

    pass

    def update(self):
        if action == 1:
            self.draw == False

    pass

    def drawing(self, x, y):

        self.rectX1 = x + 32
        self.rectY1 = y + 32
        self.rectX2 = self.rectX1 + 32
        self.rectY2 = self.rectY1 + 32

        draw_rectangle(self.rectX1, self.rectY1, self.rectX2, self.rectY2)
        self.idle.draw(x + 32, y + 32, 64, 64)

    pass


open_canvas(1280, 640)

block = Block()

blocks = [Block() for i in range (0, 40)]

while game:
    handle_event()
    block.update()
    clear_canvas()
    block.drawing(0, 0)
    update_canvas()
