import pygame
import pygame.font
from pygame.sprite import Sprite


class Message(Sprite):
    def __init__(self, screen, st_x, st_y, msg,text_color=(46, 49, 124),background_color=None):
        super().__init__()
        self.screen = screen
        self.font = pygame.font.Font("font/DIN1451-36breit-1.ttf", 50)
        self.text_color = text_color
        if background_color!=None :
            self.background_color = background_color
            self.msg_image = self.font.render(msg, True, self.text_color, self.background_color)
        else :
            self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = st_x
        self.msg_image_rect.centery = st_y
    def blitme(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)