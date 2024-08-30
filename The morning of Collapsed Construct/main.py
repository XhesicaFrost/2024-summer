import pygame
import game_functions as gf
from Settings import Settings
from pygame.sprite import Group
from player import player
from collapsed_construction import collapsed_construction
from background import Background
from Status import Status
from Button import Button
from Button import Start_button
from Button import End_button
from Button import MODEL_1_button
from Button import End_choose_button
from Photo import Photo
from explosive import Explosive
from explosive import Warning
from realm import Realm
from tainted_carcass import Tainted_carcass
from encounters import Encounter
from collapse_paradigm import Collapse_paradigm_list
from collapse_paradigm import Collapse_paradigm
from Button import Story_mode_choose_button
from Button import End_show_story_button
import stroy as sty
import warnings as wa

def run_wait(screen, ai_settings, background, status, buttons, title):
    gf.check_start(screen, ai_settings, status, buttons)
    gf.update_screen_start(screen, background, status, buttons, title)
    if status.game_active == True:
        ini_choose_buttons(screen, buttons)


def ini_choose_buttons(screen, buttons):
    buttons.empty()
    model_1_button = MODEL_1_button(screen, "photo/model_1.png", "photo/model_1_2.png")
    buttons.add(model_1_button)
    story_mode_choose_button = Story_mode_choose_button(screen, "photo/button-story.png", "photo/button-story-2.png")
    buttons.add(story_mode_choose_button)
    back_button = End_choose_button(screen, "photo/button_back_2.png", "photo/button_back_1.png")
    buttons.add(back_button)
    la = 100
    std_x = 1000
    gap = 200
    for button in buttons:
        button.rect.centerx = std_x
        button.rect.centery = la + gap
        la = button.rect.centery


def run_choose_model(screen, ai_settings, background, status, buttons, title):
    gf.check_start(screen, ai_settings, status, buttons)
    gf.update_screen_start(screen, background, status, buttons, title)
    if status.game_active == False:
        ini_buttons(buttons, screen)
    if status.game_MODEL!=0:
        pygame.mixer.music.load('music/fight.mp3')
        pygame.mixer.music.play(loops=-1)


def ini_buttons(buttons, screen):
    buttons.empty()
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
    pygame.mixer.init()
    wa.filterwarnings("ignore")
    pygame.display.set_caption("The morning of Collapsed Construct")
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    buttons = Group()
    title = Photo(screen, "photo/title-2.png", 300, 150)
    ini_buttons(buttons, screen)
    background = Background(screen)
    status = Status()
    realms = Group()
    Player = player(ai_settings, screen)
    Collapseds = Group()
    explosives = Group()
    warnings = Group()
    messages = Group()
    tainted_carcasses = Group()
    encounter = Encounter(0, 0)
    clock = pygame.time.Clock()
    collapsed_paradigm_list = Collapse_paradigm_list()
    collapsed_paradigms = Group()
    fps = 60
    pygame.mixer.music.load('music/main.mp3')
    pygame.mixer.music.play(loops=-1)
    while True:
        if status.game_active == True and status.game_MODEL == 1:
            gf.check_event(screen, ai_settings, Player, status)
            gf.update_items(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                            tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms)
            gf.update_screen(screen, ai_settings, Player, Collapseds, background, explosives, warnings, messages,
                             realms, tainted_carcasses, collapsed_paradigms,status)
            gf.check_collide(screen, ai_settings, Player, Collapseds, explosives, status, background, warnings, realms,
                             tainted_carcasses, encounter, collapsed_paradigm_list, collapsed_paradigms)
            if status.game_active == False :
                ini_buttons(buttons, screen)
        elif status.game_active == True and status.game_MODEL == 0:
            run_choose_model(screen, ai_settings, background, status, buttons, title)
        elif status.game_active == True and status.game_MODEL ==2:
            sty.update_story(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                            tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms,background)
            if status.game_active==False:
                ini_buttons(buttons,screen)
                background.show=0
        elif status.game_active == False:
            run_wait(screen, ai_settings, background, status, buttons, title)
        clock.tick(fps)
run_game()
