import pygame
import game_functions as gf
from Settings import Settings
import game_functions as gf
from pygame.sprite import Group
from player import player
from collapsed_construction import collapsed_construction
from background import Background
from Status import Status
from Button import Button
from Button import Start_button
from Button import End_button
from Photo import Photo
from explosive import Explosive
from explosive import Warning


def run_wait(screen, ai_settings, background, status, buttons, title):
    gf.check_start(screen, ai_settings, status, buttons)
    gf.update_screen_start(screen, background, status, buttons, title)


def ini_buttons(buttons, screen):
    button_start = Start_button(screen, "photo/button-start-1.png", "photo/button-start-2.png")
    buttons.add(button_start)
    button_end = End_button(screen, "photo/button-end-1.png", "photo/button-end-2.png")
    buttons.add(button_end)
    la = -100
    std_x = 1000
    gap = 400
    for button in buttons:
        button.rect.centerx = std_x
        button.rect.centery = la + gap
        la = button.rect.centery


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    buttons = Group()
    title = Photo(screen, "photo/title-1.png", 300, 150)
    ini_buttons(buttons, screen)
    background = Background(screen)
    status = Status()
    Player = player(ai_settings, screen)
    Collapsed = collapsed_construction(ai_settings, screen)
    Collapseds = Group()
    explosives = Group()
    warnings = Group()
    messages = Group()
    clock = pygame.time.Clock()
    fps = 60
    while True:
        if status.game_active == True:
            gf.check_event(screen, ai_settings, Player)
            gf.update_items(screen, ai_settings, Player, Collapseds, explosives, warnings, messages)
            gf.update_screen(screen, ai_settings, Player, Collapseds, background, explosives, warnings, messages)
            gf.check_collide(screen, ai_settings, Player, Collapseds, explosives,status,background,warnings)
        else:
            run_wait(screen, ai_settings, background, status, buttons, title)
        clock.tick(fps)


run_game()
