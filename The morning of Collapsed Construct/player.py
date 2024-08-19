import pygame
from pygame.sprite import Sprite


class player(Sprite):
    def __init__(self, ai_settings, screen):
        super(player, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load("photo/player.png")
        self.image2 = pygame.image.load("photo/player_transparent.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        self.move_x = [20, -20, 0, 0]
        self.move_y = [0, 0, 20, -20]
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.hide=False
        self.hide_gap=3
        self.hide_during=3
        self.last_hide=-3
        self.hide_ready=False
    def update(self):
        if self.move_up == True and self.rect.top + self.move_y[3]>=0:
            self.rect.centerx = self.rect.centerx + self.move_x[3]
            self.rect.centery = self.rect.centery + self.move_y[3]
        elif self.move_down == True and self.rect.bottom + self.move_y[2]<=self.screen_rect.bottom:
            self.rect.centerx = self.rect.centerx + self.move_x[2]
            self.rect.centery = self.rect.centery + self.move_y[2]
        elif self.move_left==True and self.rect.left + self.move_x[1]>=self.screen_rect.left:
            self.rect.centerx = self.rect.centerx + self.move_x[1]
            self.rect.centery = self.rect.centery + self.move_y[1]
        elif self.move_right==True and self.rect.right + self.move_x[0]<=self.screen_rect.right:
            self.rect.centerx = self.rect.centerx + self.move_x[0]
            self.rect.centery = self.rect.centery + self.move_y[0]
    def blitme(self):
        if self.hide == False:
            self.screen.blit(self.image, self.rect)
        else :
            self.screen.blit(self.image2,self.rect)
