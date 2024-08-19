import sys
import pygame
import random

def check_keydown(event,screen,ai_settings,Player):
    if event.key==pygame.K_w:
        Player.move_up=True
    elif event.key==pygame.K_s:
        Player.move_down = True
    elif event.key == pygame.K_a:
        Player.move_left = True
    elif event.key == pygame.K_d:
        Player.move_right = True
    elif event.key ==pygame.K_SPACE:
        Player.hide=True

def check_keyup(event,screen,ai_settings,Player):
    if event.key==pygame.K_w:
        Player.move_up=False
    elif event.key==pygame.K_s:
        Player.move_down = False
    elif event.key == pygame.K_a:
        Player.move_left = False
    elif event.key == pygame.K_d:
        Player.move_right = False
    elif event.key == pygame.K_SPACE:
        Player.hide=False
def check_event(screen, ai_settings, Player):
    events=pygame.event.get()
    if len(events)==0:
        return
    else:
        for event in events:
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                check_keydown(event,screen,ai_settings,Player)
            elif event.type==pygame.KEYUP:
                check_keyup(event,screen,ai_settings,Player)

def update_items(screen,ai_settings,Player,Collapsed):
    Player.update()
    Collapsed.update(Player)
def check_start(screen,ai_settings,status):
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.KEYDOWN:
            status.game_active=True;
def update_screen_start(screen,background,status):
    background.blitme1()
    pygame.display.flip()
def update_screen(screen, ai_settings, Player,Collapsed,background):
       # screen.fill(ai_settings.screen_color)
        background.blitme2()
        Player.blitme()
        Collapsed.blitme()
        pygame.display.flip()

