import pygame
from pygame.sprite import Sprite


class Explosive(Sprite):
    def __init__(self, ai_setiings, screen, now_time):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("photo/explosed-2.png")
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect_draw = self.rect.copy()
        self.rect.width = 17
        self.rect.height = 17
        self.rect.center = self.rect_draw.center
        self.begin = now_time
        self.tim = ai_setiings.explosive_exist

    def blitme(self):
        self.rect_draw.center = self.rect.center
        self.screen.blit(self.image, self.rect_draw)
        # self.screen.fill((200,200,200),self.rect)


class Warning(Sprite):
    def __init__(self, ai_settings, screen, start_x, start_y, end_x, end_y, now_time):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect
        self.tim = ai_settings.warning_exist
        self.begin = now_time
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

    def blitme(self, now_tim):
        if 2 * (now_tim - self.begin) <= self.tim:
            pygame.draw.line(self.screen, (194, 31, 48), (self.start_x, self.start_y), \
                             (self.end_x, self.end_y), width=3)
        else:
            pygame.draw.line(self.screen, (92, 174, 240), (self.start_x, self.start_y), \
                             (self.end_x, self.end_y), width=3)
