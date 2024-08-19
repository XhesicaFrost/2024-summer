import pygame
import game_functions as gf
from  Settings import Settings
import game_functions as gf
from pygame.sprite import Group
from player import player
from collapsed_construction import collapsed_construction
from background import Background
from Status import Status
def run_wait(screen,ai_settings,background,status):
    gf.check_start(screen,ai_settings,status)
    gf.update_screen_start(screen,background,status)

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )
    background=Background(screen)
    status=Status()
    Player=player(ai_settings,screen)
    Collapsed=collapsed_construction(ai_settings,screen)
    Collapseds=Group()
    clock = pygame.time.Clock()
    fps = 120
    while True:
        if status.game_active == True:
            gf.check_event(screen,ai_settings,Player)
            gf.update_items(screen,ai_settings,Player,Collapsed)
            gf.update_screen(screen,ai_settings,Player,Collapsed,background)
        else :
            run_wait(screen,ai_settings,background,status)
        clock.tick(fps)
run_game()