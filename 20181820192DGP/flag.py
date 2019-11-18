from pico2d import*

image_sizeW = 64
image_sizeH = 64

def check_intersected_rect(left1, top1, right1, bottom1, left2, top2, right2, bottom2):  # 자기자신의 인자 (1)   플레이어 인자 (2)
    if left2 < right1 and right1 > left2 and bottom2 <= top1 and top2 >= bottom1:
        return True

class Flag:

    def __init__(self, pos):
        self.noFlagImage = load_image('chip\\object\\check_point_noflag.png')
        self.FlagImage = load_image('chip\\object\\check_point.png')
        self.x = pos[0]
        self.y = pos[1]
        self.frame = 0
        self.left = self.x - 10
        self.top = self.y + 32
        self.right = self.x + 10
        self.bottom = self.y - 32
        self.flagOn = False
        pass

    def update(self,player):
        if player.objectNum == 16:
            self.flagOn = True

        if self.flagOn:
            self.frame = (self.frame + 1) % 10
        else:
            pass
        pass

    def check_collision(self , player):
        if self.flagOn:
            if check_intersected_rect(self.left,self.top,self.right,self.bottom,player.left,player.top,player.right,player.bottom):
                # game_framework.quit()
                pass
        pass

    def draw(self):
        if self.flagOn:
            self.FlagImage.clip_draw(self.frame * image_sizeW, 0 , image_sizeW, image_sizeH, self.x, self.y)
        else:
            self.noFlagImage.draw(self.x, self.y)
        #   draw_rectangle(self.left, self.top, self.right, self.bottom)
        pass


