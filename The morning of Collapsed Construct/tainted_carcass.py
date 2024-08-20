import pygame
from pygame.sprite import Sprite

class Tainted_carcass(Sprite):
    def __init__(self,screen,st_x,st_y,direction,now_tim):
        super().__init__()
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.image=[]
        self.image_rect=[]
        for i in range(1,11):
            self.image.append(pygame.image.load("photo/tainted carcass"+str(i)+".png"))
            self.image_rect.append(self.image[i-1].get_rect())
        self.kind_gap=5
        self.rect=pygame.Rect(st_x,st_y,18,28)
        self.direction=direction
        self.kind=5
        self.la_change=0
        self.speed=10
    def update(self,now_tim,ai_settings,status):
        if self.la_change==self.kind_gap:
            self.kind=(self.kind+1)%10
            self.la_change=0
        else:
            self.la_change+=1
        if status.game_KEYDOWN==True:
            self.rect.centerx+=ai_settings.move_x[self.direction]*self.speed
            self.rect.centery+=ai_settings.move_y[self.direction]*self.speed
        else:
            self.rect.centerx+=ai_settings.move_x[self.direction]*(self.speed/ai_settings.time_speed_down)
            self.rect.centery+=ai_settings.move_y[self.direction]*(self.speed/ai_settings.time_speed_down)

    def blitme(self,now_tim):
        self.image_rect[self.kind].center=self.rect.center
        self.image_rect[self.kind].centerx=self.rect.centerx+3
        self.screen.blit(self.image[self.kind],self.image_rect[self.kind])
        self.screen.fill((200,200,200),self.rect)