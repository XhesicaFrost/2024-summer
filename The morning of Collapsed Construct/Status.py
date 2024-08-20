import pygame


class Status():
    def __init__(self):
        self.game_active = False
        self.game_start_time=0
        self.game_KEYDOWN = False
        self.game_KEYDOWN_cnt=0
