import pygame
import time
import math
from pygame.sprite import Sprite
class Collapse_paradigm_list():
    def __init__(self):
        self.active=[False,False,False]
        self.num = 1
class Collapse_paradigm(Sprite):
    def __init__(self,screen,now_tim,during=5):
        super().__init__()
        self.begin=now_tim
        self.during=during
        self.screen=screen

class Collapse_paradigm_nonlinear_motion(Collapse_paradigm):
    def __init__(self,screen,now_tim,during=5):
        super().__init__(screen,now_tim,during)
        self.msg="Nonlinear_motion"
        self.image=pygame.image.load("photo/unliner_motion.png")
        self.rect=self.image.get_rect()
        self.id=0
    def act(self,Player):
        Player.unliner_motion=True
    def self_kill(self,Player):
        Player.unliner_motion=False
        self.kill()
    def blitme(self):
        self.screen.blit(self.image,self.rect)
class Collapse_paradigm_image_corruption(Collapse_paradigm):
    def __init__(self,screen,now_tim,during=5):
        super().__init__(screen,now_tim,during)
        self.msg="Image corruption"
        self.image=pygame.image.load("photo/image corruption.png")
        self.rect=self.image.get_rect()
        self.id=1
    def act(self,status):
        status.image_corruption=True
    def self_kill(self,status):
        status.image_corruption=False
        self.kill()
    def blitme(self):
        self.screen.blit(self.image,self.rect)