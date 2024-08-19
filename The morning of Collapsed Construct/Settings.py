import pygame


class Settings():
    def __init__(self):
        # 屏幕基本数据
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (138, 188, 209)
        # num区
        self.num_collapseds = 1
        self.num_warnings=3
        self.explosive_exist = 0.5
        self.warning_exist=1
        self.explosive_gap=30
