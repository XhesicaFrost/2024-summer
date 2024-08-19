import pygame
import pygame.image


class Background():
    def __init__(self,screen):
        self.image1=pygame.image.load("photo/background1.png")
        self.image2=pygame.image.load("photo/background2.png")
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.rect=self.screen_rect
    def blitme1(self):
        self.screen.blit(self.image1,self.rect)
    def blitme2(self):
        self.screen.blit(self.image2,self.rect)
