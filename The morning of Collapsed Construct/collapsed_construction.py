import pygame
from pygame.sprite import Sprite
import random
import math

class collapsed_construction(Sprite):
    def __init__(self, ai_settings, screen):
        super(collapsed_construction, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load("photo/坍缩体.png")
        self.rect = self.image.get_rect()
        self.rect_draw=self.rect.copy()
       # print(self.rect.center,self.rect_draw.center)
        self.rect.width=30
        self.rect.height=30
        #print(self.rect.center, self.rect_draw.center)
        self.rect.center=self.rect_draw.center
        self.screen_rect = screen.get_rect()
        self.direction_x = random.randint(-10, 10)
        self.direction_y = random.randint(-10, 10)
        while (self.direction_x == 0 and self.direction_y == 0):
            self.direction_x = random.randint(-10, 10)
            self.direction_y = random.randint(-10, 10)
        self.speed=20
    def blitme(self):
        self.rect_draw.center=self.rect.center
        self.screen.blit(self.image, self.rect_draw)
       # self.screen.fill((100,200,200),self.rect) 这里是碰撞箱
    def update_direction(self, Player):
        if Player.hide == True :
            self.direction_x = -self.direction_x+random.randint(-500,500)
            self.direction_y = -self.direction_y+random.randint(-500,500)
        else :
            self.direction_x = Player.rect.centerx - self.rect.centerx
            self.direction_y = Player.rect.centery - self.rect.centery
        while(self.direction_x == 0 and self.direction_y ==0):
            self.direction_x = random.randint(-10, 10)
            self.direction_y = random.randint(-10, 10)
    def update(self, Player,status,ai_settings):
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom or \
                self.rect.left <= self.screen_rect.left or self.rect.right >= self.screen_rect.right:
            self.update_direction(Player)
        if status.game_KEYDOWN ==True :
            k=self.speed/math.sqrt(self.direction_x*self.direction_x+self.direction_y*self.direction_y)
        else:
            k = self.speed /math.sqrt(self.direction_x * self.direction_x + self.direction_y * self.direction_y)/(ai_settings.time_speed_down+2)
        change_x=self.direction_x*k
        change_y=self.direction_y*k
        self.rect.centerx+=change_x
        self.rect.centery+=change_y