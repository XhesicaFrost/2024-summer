import pygame
from pygame.sprite import Sprite


class player(Sprite):
    def __init__(self, ai_settings, screen):
        super(player, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load("photo/player.png")
        self.image2 = pygame.image.load("photo/player_transparent.png")
        self.image3 = pygame.image.load("photo/player_2.png")
        self.image4 = pygame.image.load("photo/player_transparent_2.png")
        self.image_corruption=pygame.image.load("photo/player_black.png")
        self.image3_corruption=pygame.image.load("photo/player_2_black.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        self.move_x = [5, -5, 0, 0]
        self.move_y = [0, 0, 5, -5]
        self.move_run_x = [20, -20, 0, 0]
        self.move_run_y = [0, 0, 20, -20]
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.hide = False
        self.hide_gap = 3
        self.hide_during = 3
        self.last_hide = 0
        self.hide_ready = False
        self.direction = 1
        self.run = False
        self.unliner_motion = False
        self.unliner_move_x = [5, -5, -1, 1]
        self.unliner_move_y = [-1, 1, 5, -5]
        self.unliner_move_run_x = [20, -20, -4, 4]
        self.unliner_move_run_y = [-4, 4, 20, -20]
        self.tim=self.hide_gap
    def update(self):
        if self.unliner_motion == False:
            if self.run == False:
                if self.move_up == True:
                    if self.rect.top + self.move_y[3] >= 0:
                        self.rect.centerx = self.rect.centerx + self.move_x[3]
                        self.rect.centery = self.rect.centery + self.move_y[3]
                    else:
                        self.rect.top = 0
                elif self.move_down == True:
                    if self.rect.bottom + self.move_y[2] <= self.screen_rect.bottom:
                        self.rect.centerx = self.rect.centerx + self.move_x[2]
                        self.rect.centery = self.rect.centery + self.move_y[2]
                    else:
                        self.rect.bottom = self.screen_rect.bottom
                elif self.move_left == True:
                    if self.rect.left + self.move_x[1] >= self.screen_rect.left:
                        self.rect.centerx = self.rect.centerx + self.move_x[1]
                        self.rect.centery = self.rect.centery + self.move_y[1]
                    else:
                        self.rect.left = self.screen_rect.left
                    self.direction = 0
                elif self.move_right == True:
                    if self.rect.right + self.move_x[0] <= self.screen_rect.right:
                        self.rect.centerx = self.rect.centerx + self.move_x[0]
                        self.rect.centery = self.rect.centery + self.move_y[0]
                    else:
                        self.rect.right = self.screen_rect.right
                    self.direction = 1
            else:
                if self.move_up == True:
                    if self.rect.top + self.move_run_y[3] >= 0:
                        self.rect.centerx = self.rect.centerx + self.move_run_x[3]
                        self.rect.centery = self.rect.centery + self.move_run_y[3]
                    else:
                        self.rect.top = 0
                elif self.move_down == True:
                    if self.rect.bottom + self.move_run_y[2] <= self.screen_rect.bottom:
                        self.rect.centerx = self.rect.centerx + self.move_run_x[2]
                        self.rect.centery = self.rect.centery + self.move_run_y[2]
                    else:
                        self.rect.bottom = self.screen_rect.bottom
                elif self.move_left == True:
                    if self.rect.left + self.move_run_x[1] >= self.screen_rect.left:
                        self.rect.centerx = self.rect.centerx + self.move_run_x[1]
                        self.rect.centery = self.rect.centery + self.move_run_y[1]
                    else:
                        self.rect.left = self.screen_rect.left
                    self.direction = 0
                elif self.move_right == True:
                    if self.rect.right + self.move_run_x[0] <= self.screen_rect.right:
                        self.rect.centerx = self.rect.centerx + self.move_run_x[0]
                        self.rect.centery = self.rect.centery + self.move_run_y[0]
                    else:
                        self.rect.right = self.screen_rect.right
                    self.direction = 1
        else:
            if self.run == False:
                if self.move_up == True :
                    if self.rect.top + self.unliner_move_y[3] >= 0 :
                        self.rect.centery = self.rect.centery + self.unliner_move_y[3]
                    else :
                        self.rect.top=0
                    if self.rect.right + self.unliner_move_x[3] <= self.screen_rect.right:
                        self.rect.centerx = self.rect.centerx + self.unliner_move_x[3]
                    else:
                        self.rect.right=self.screen_rect.right
                elif self.move_down == True :
                    if self.rect.bottom + self.unliner_move_y[2] <= self.screen_rect.bottom :
                        self.rect.centery = self.rect.centery + self.unliner_move_y[2]
                    else:
                        self.rect.bottom = self.screen_rect.bottom
                    if self.rect.left + self.unliner_move_x[2] >= self.screen_rect.left :
                        self.rect.centerx = self.rect.centerx + self.unliner_move_x[2]
                    else:
                        self.rect.left = self.screen_rect.left
                elif self.move_left == True :
                    if self.rect.left + self.unliner_move_x[1] >= self.screen_rect.left :
                        self.rect.centerx = self.rect.centerx + self.unliner_move_x[1]
                    else:
                        self.rect.left=self.screen_rect.left
                    if self.rect.bottom + self.unliner_move_y[1] <= self.screen_rect.bottom:
                        self.rect.centery = self.rect.centery + self.unliner_move_y[1]
                    else:
                        self.rect.bottom=self.screen_rect.bottom
                    self.direction = 0
                elif self.move_right == True :
                    if self.rect.right + self.unliner_move_x[0] <= self.screen_rect.right :
                        self.rect.centerx = self.rect.centerx + self.unliner_move_x[0]
                    else:
                        self.rect.right=self.screen_rect.right
                    if self.rect.top + self.unliner_move_y[0] >= 0:
                        self.rect.centery = self.rect.centery + self.unliner_move_y[0]
                    else:
                        self.rect.top=self.screen_rect.top
                    self.direction = 1
            else:
                if self.move_up == True:
                    if self.rect.top + self.unliner_move_run_y[3] >= 0:
                        self.rect.centery = self.rect.centery + self.unliner_move_run_y[3]
                    else:
                        self.rect.top = 0
                    if self.rect.right + self.unliner_move_run_x[3] <= self.screen_rect.right:
                        self.rect.centerx = self.rect.centerx + self.unliner_move_run_x[3]
                    else:
                        self.rect.right = self.screen_rect.right
                elif self.move_down == True:
                    if self.rect.bottom + self.unliner_move_run_y[2] <= self.screen_rect.bottom:
                        self.rect.centery = self.rect.centery + self.unliner_move_run_y[2]
                    else:
                        self.rect.bottom = self.screen_rect.bottom
                    if self.rect.left + self.unliner_move_run_x[2] >= self.screen_rect.left:
                        self.rect.centerx = self.rect.centerx + self.unliner_move_run_x[2]
                    else:
                        self.rect.left = self.screen_rect.left
                elif self.move_left == True:
                    if self.rect.left + self.unliner_move_run_x[1] >= self.screen_rect.left:
                        self.rect.centerx = self.rect.centerx + self.unliner_move_run_x[1]
                    else:
                        self.rect.left = self.screen_rect.left
                    if self.rect.bottom + self.unliner_move_run_y[1] <= self.screen_rect.bottom:
                        self.rect.centery = self.rect.centery + self.unliner_move_run_y[1]
                    else:
                        self.rect.bottom = self.screen_rect.bottom
                    self.direction = 0
                elif self.move_right == True:
                    if self.rect.right + self.unliner_move_run_x[0] <= self.screen_rect.right:
                        self.rect.centerx = self.rect.centerx + self.unliner_move_run_x[0]
                    else:
                        self.rect.right = self.screen_rect.right
                    if self.rect.top + self.unliner_move_run_y[0] >= 0:
                        self.rect.centery = self.rect.centery + self.unliner_move_run_y[0]
                    else:
                        self.rect.top = self.screen_rect.top
                    self.direction = 1

    def blitme(self,status):
        if status.image_corruption==True:
            if self.direction == 1:
                self.screen.blit(self.image_corruption, self.rect)
            else:
                self.screen.blit(self.image3_corruption, self.rect)
        elif self.hide == False:
            if self.direction == 1:
                self.screen.blit(self.image, self.rect)
            else:
                self.screen.blit(self.image3, self.rect)
        else:
            if self.direction == 1:
                self.screen.blit(self.image2, self.rect)
            else:
                self.screen.blit(self.image4, self.rect)
    def reini(self):
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.hide_ready = False
        self.direction = 1
        self.run = False
        self.unliner_motion = False
