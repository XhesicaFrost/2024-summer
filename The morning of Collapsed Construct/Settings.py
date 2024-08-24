import pygame


class Settings():
    def __init__(self):
        # 屏幕基本数据
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (138, 188, 209)
        # num区
        self.num_collapseds =1
        self.num_realms=10
        self.num_warnings=5
        self.num_tainted_carcasses=10
        self.explosive_exist = 0.5
        self.warning_exist=1
        self.explosive_gap=30
        self.realm_exist=10
        self.move_x=[1,-1,0,0]
        self.move_y=[0,0,1,-1]
        self.time_speed_up=3
        self.time_speed_down=5
    def reini(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (138, 188, 209)
        # num区
        self.num_collapseds = 1
        self.num_realms = 10
        self.num_warnings = 5
        self.num_tainted_carcasses = 10
        self.explosive_exist = 0.5
        self.warning_exist = 1
        self.explosive_gap = 30
        self.realm_exist = 10
        self.move_x = [1, -1, 0, 0]
        self.move_y = [0, 0, 1, -1]
        self.time_speed_up = 3
        self.time_speed_down = 5
