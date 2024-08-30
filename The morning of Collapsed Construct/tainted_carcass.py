import pygame
from pygame.sprite import Sprite

class Tainted_carcass(Sprite):
    def __init__(self,screen,st_x,st_y,direction,now_tim=0):
        super().__init__()
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.image=[]
        self.image_rect=[]
        self.image_corruption = []
        self.image_corruption_rect = []
        for i in range(1,11):
            self.image.append(pygame.image.load("photo/tainted carcass"+str(i)+".png"))
            self.image_rect.append(self.image[i-1].get_rect())
        for i in range(1, 11):
            self.image_corruption.append(pygame.image.load("photo/tainted carcass_black" + str(i) + ".png"))
            self.image_corruption_rect.append(self.image[i - 1].get_rect())
        self.kind_gap=10
        self.rect=pygame.Rect(st_x,st_y,18,28)
        self.direction=direction
        self.kind=5
        self.la_change=0
        self.speed=5
    def update(self,now_tim,ai_settings,status):
        if self.la_change==self.kind_gap:
            self.kind=(self.kind+2)%10
            self.la_change=0
        else:
            self.la_change+=1
        if status.game_KEYDOWN==True:
            self.rect.centerx+=ai_settings.move_x[self.direction]*self.speed
            self.rect.centery+=ai_settings.move_y[self.direction]*self.speed
        else:
            self.rect.centerx+=ai_settings.move_x[self.direction]*(self.speed/ai_settings.time_speed_down)
            self.rect.centery+=ai_settings.move_y[self.direction]*(self.speed/ai_settings.time_speed_down)

    def blitme(self,now_tim,status):
        if status.image_corruption==False:
            self.image_rect[self.kind].center=self.rect.center
            self.image_rect[self.kind].centerx=self.rect.centerx+3
            self.screen.blit(self.image[self.kind],self.image_rect[self.kind])
        else:
            self.image_corruption_rect[self.kind].center = self.rect.center
            self.image_corruption_rect[self.kind].centerx = self.rect.centerx + 3
            self.screen.blit(self.image_corruption[self.kind], self.image_corruption_rect[self.kind])

    #  self.screen.fill((200,200,200),self.rect)