import pygame


class Status():
    def __init__(self):
        self.game_active = False
        self.game_start_time=0
        self.game_KEYDOWN = False
        self.game_KEYDOWN_cnt=0
        self.game_MODEL=0#随机无尽模式
        self.image_corruption=False
        self.story_mode=False
        self.show_story=False
        self.chapter=1
    def reini(self):
        self.game_active = False
        self.game_start_time = 0
        self.game_KEYDOWN = False
        self.game_KEYDOWN_cnt = 0
        self.game_MODEL = 0  # 随机无尽模式
        self.image_corruption = False
        self.story_mode = False
        self.show_story = False
        self.chapter = 1
