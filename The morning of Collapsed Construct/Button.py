import time
import pygame.font
from pygame.sprite import Sprite
import sys

class Button(Sprite):
    def __init__(self, screen, path1, path2):
        super(Button, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image1 = pygame.image.load(path1)
        self.image2 = pygame.image.load(path2)
        self.rect = self.image1.get_rect()
        self.chosen = False

    def blitme(self):
        if self.chosen == 1:
            self.screen.blit(self.image2, self.rect)
        else:
            self.screen.blit(self.image1, self.rect)
class Start_button(Button):
    def __init__(self, screen, path1, path2):
        super().__init__(screen,path1, path2)

    def act(self, status,aim=None):
        if self.chosen == True:
            status.game_active = True
            now_tim=time.time()
            status.game_start_time=now_tim
class End_button(Button):
    def __init__(self,screen,path1,path2):
        super().__init__(screen,path1,path2)
    def act(self,status,aim=None):
        if self.chosen==True:
            sys.exit()
class MODEL_1_button(Button):
    def __init__(self,screen,path1,path2):
        super().__init__(screen,path1,path2)
    def act(self,status):
        if self.chosen== True :
            status.game_MODEL=1
            now_tim = time.time()
            status.game_start_time = now_tim
class End_choose_button(Button):
    def __init__(self,screen,path1,path2):
        super().__init__(screen,path1,path2)
    def act(self,status,aim=None):
        if self.chosen == True :
            status.game_active=False


class Story_mode_choose_button(Button):
    def __init__(self,screen,path1,path2):
        super().__init__(screen,path1,path2)
    def act(self,status,aim=None):
        if self.chosen == True :
            status.game_MODEL=2
            status.game_active=True
            now_tim = time.time()
            status.game_start_time = now_tim

class End_show_story_button(Button):
    def __init__(self,screen,path1,path2):
        super().__init__(screen,path1,path2)
    def act(self,status,aim=None):
        if self.chosen == True :
            status.show_story=False