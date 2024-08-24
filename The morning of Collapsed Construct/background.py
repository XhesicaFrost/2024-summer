import pygame
import pygame.image


class Background():
    def __init__(self,screen,show=0):
        self.image1=pygame.image.load("photo/background-1-1.png")
        self.image2=pygame.image.load("photo/background2-1.png")
        self.image3=pygame.image.load("photo/background3.png")
        self.image_camp= pygame.image.load("photo/background_camp.png")
        self.image_forest = pygame.image.load("photo/background_forest.png")
        self.image_help=pygame.image.load("photo/background_help.png")
        self.image_safe=pygame.image.load("photo/background_safe.png")
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.rect=self.screen_rect
        self.show=show
    def blitme1(self):
        self.screen.blit(self.image1,self.rect)
    def blitme2(self):
        self.screen.blit(self.image2,self.rect)
    def blitme3(self):
        self.screen.blit(self.image3,self.rect)
    def showme(self):
        if self.show==0:
            self.screen.blit(self.image3,self.rect)
        if self.show==1:
            self.screen.blit(self.image_camp,self.rect)
        if self.show==2:
            self.screen.blit(self.image_forest,self.rect)
        if self.show==3:
            self.screen.blit(self.image_help,self.rect)
        if self.show==4:
            self.screen.blit(self.image_safe,self.rect)