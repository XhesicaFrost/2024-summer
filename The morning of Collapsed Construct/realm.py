import pygame
import time
import math
from pygame.sprite import Sprite

class Realm(Sprite):
    def __init__(self,screen,st_x=None,st_y=None,color="BLACK",now_tim=0):
        super().__init__()
        self.screen=screen
        self.screen_rect=screen.get_rect()
        if color=="BLACK":
            self.image1=pygame.image.load("photo/fire-black1.png")
            self.image1_rect=self.image1.get_rect()
            self.image2=pygame.image.load("photo/fire-black2.png")
            self.image2_rect = self.image2.get_rect()
            self.image3=pygame.image.load("photo/fire-black3.png")
            self.image3_rect = self.image3.get_rect()
        else :
            self.image1=pygame.image.load("photo/fire-purple1.png")
            self.image1_rect = self.image1.get_rect()
            self.image2=pygame.image.load("photo/fire-purple2.png")
            self.image2_rect = self.image2.get_rect()
            self.image3=pygame.image.load("photo/fire-purple3.png")
            self.image3_rect = self.image3.get_rect()
        self.rect=pygame.Rect((st_x,st_y,25,35))
        self.kind_gap=0.3
        self.begin=now_tim
        self.la_change=now_tim
        self.kind=1
    def update(self,now_tim):
        if self.kind_gap+self.la_change<now_tim:
            self.kind=(self.kind+1)%3+1
            self.la_change=now_tim
    def blitme(self):
        if self.kind==1:
            self.image1_rect.center=self.rect.center
            self.image1_rect.centery-=15
            self.screen.blit(self.image1,self.image1_rect)
        if self.kind==2:
            self.image2_rect.center=self.rect.center
            self.image2_rect.centery -= 15
            self.screen.blit(self.image2,self.image2_rect)
        if self.kind==3:
            self.image3_rect.center=self.rect.center
            self.image3_rect.centery -= 15
            self.screen.blit(self.image3,self.image3_rect)
        #self.screen.fill((200, 200, 200), self.rect)