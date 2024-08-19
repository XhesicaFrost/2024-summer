import sys
import pygame
import random
import math
import time
from collapsed_construction import collapsed_construction
from explosive import Warning
from explosive import Explosive
from message import Message


def swap(x, y):
    return y, x


def check_K_SPACE_DOWN(Player):
    if Player.hide_ready == True:
        now_tim = time.time()
        Player.hide_ready = False
        Player.last_hide = now_tim
        Player.hide = True


def check_keydown(event, screen, ai_settings, Player):
    if event.key == pygame.K_w:
        Player.move_up = True
    elif event.key == pygame.K_s:
        Player.move_down = True
    elif event.key == pygame.K_a:
        Player.move_left = True
    elif event.key == pygame.K_d:
        Player.move_right = True
    elif event.key == pygame.K_SPACE:
        check_K_SPACE_DOWN(Player)


def check_K_SPACE_UP(Player):
    if Player.hide == True:
        now_tim = time.time()
        Player.hide = False
        Player.last_hide = now_tim


def check_keyup(event, screen, ai_settings, Player):
    if event.key == pygame.K_w:
        Player.move_up = False
    elif event.key == pygame.K_s:
        Player.move_down = False
    elif event.key == pygame.K_a:
        Player.move_left = False
    elif event.key == pygame.K_d:
        Player.move_right = False
    elif event.key == pygame.K_SPACE:
        Player.hide = False


def check_event(screen, ai_settings, Player):
    events = pygame.event.get()
    if len(events) == 0:
        return
    else:
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown(event, screen, ai_settings, Player)
            elif event.type == pygame.KEYUP:
                check_keyup(event, screen, ai_settings, Player)


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def create_collapseds(Collapseds, Player, ai_settings, screen):
    collapsed = collapsed_construction(ai_settings, screen)
    limx = ai_settings.screen_width
    limy = ai_settings.screen_height
    while 1:
        x = random.randint(0, limx)
        y = random.randint(0, limy)
        if get_distance(x, y, Player.rect.centerx, Player.rect.centery) > 500:
            collapsed.rect.centerx = x
            collapsed.rect.centery = y
            Collapseds.add(collapsed)
            break;


def end_game(screen, ai_settings, Player, Collapseds,status,background):
    now_tim=time.time()
    during=int(now_tim-status.game_start_time)
    message1=Message(screen,600,320,"YOU HAVE HELD ON FOR ")
    message2=Message(screen,600,390,str(during)+" SECONDS")
    background.blitme3()
    message1.blitme()
    message2.blitme()
    pygame.display.flip()
    time.sleep(3)
    while 1:
        events=pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                status.game_active=False
                return
        background.blitme3()
        message1.blitme()
        message2.blitme()
        pygame.display.flip()



def update_collapsed(screen, ai_settings, Player, Collapseds):
    for collapsed in Collapseds:
        k = random.randint(1, 1000)
        if k == 1:
            Collapseds.remove(collapsed)
    while len(Collapseds) < ai_settings.num_collapseds:
        create_collapseds(Collapseds, Player, ai_settings, screen)
    Collapseds.update(Player)


def create_warning(screen, ai_settings, warnings, now_tim):
    limx = ai_settings.screen_width
    limy = ai_settings.screen_height
    flag = random.randint(0, 2)
    if flag == 0:
        st_x = 0;
        end_x = limx
        st_y = random.randint(0, limy)
        end_y = random.randint(0, limy)
        warning = Warning(ai_settings, screen, st_x, st_y, end_x, end_y, now_tim)
        warnings.add(warning)
    else:
        st_y = 0;
        end_y = limx
        st_x = random.randint(0, limx)
        end_x = random.randint(0, limx)
        warning = Warning(ai_settings, screen, st_x, st_y, end_x, end_y, now_tim)
        warnings.add(warning)


def create_explosive(ai_settings, screen, warning, explosives, now_tim):
    st_x = warning.start_x
    st_y = warning.start_y
    end_x = warning.end_x
    end_y = warning.end_y
    vector_x = end_x - st_x
    vector_y = end_y - st_y
    radio = ai_settings.explosive_gap / math.sqrt((vector_x * vector_x) + (vector_y * vector_y))
    vector_x *= radio
    vector_y *= radio
    bomber_x = st_x
    bomber_y = st_y
    while abs(bomber_x - st_x) <= abs(st_x - end_x) and abs(bomber_y - st_y) <= abs(st_y - end_y):
        explosive = Explosive(ai_settings, screen, now_tim)
        explosive.rect.centerx = bomber_x
        explosive.rect.centery = bomber_y
        explosives.add(explosive)
        bomber_x += vector_x
        bomber_y += vector_y
def update_K_SPACE(Player, screen, messages):
    now_tim = time.time()
    if Player.hide == True:
        if now_tim - Player.last_hide > Player.hide_during:
            Player.hide = False
            last_hide = now_tim
    else:
        if now_tim - Player.last_hide > Player.hide_gap:
            Player.hide_ready = True
    if Player.hide_ready == True:
        message = Message(screen, 150, 50, "READY",background_color=(43, 155, 175))
        messages.add(message)
    else:
        message = Message(screen, 150, 50, "WAITING",background_color=(43, 155, 175))
        messages.add(message)


def update_items(screen, ai_settings, Player, Collapseds, explosives, warnings, messages):
    Player.update()
    update_K_SPACE(Player, screen, messages)
    now_tim = time.time()
    update_collapsed(screen, ai_settings, Player, Collapseds)
    k = random.randint(1, 20)
    if k == 1 and len(warnings) < ai_settings.num_warnings:
        create_warning(screen, ai_settings, warnings, now_tim)
    for warning in warnings:
        if warning.tim + warning.begin <= now_tim:
            create_explosive(ai_settings, screen, warning, explosives, now_tim)
            warnings.remove(warning)
        else:
            break
    for explosive in explosives:
        if explosive.begin + explosive.tim <= now_tim:
            explosives.remove(explosive)
        else:
            break
def reset(Player,Collapseds,explosives,warnings):
    Player.move_left = False
    Player.move_right = False
    Player.move_up = False
    Player.move_down = False
    Player.hide = False
    Player.hide_gap = 3
    Player.hide_during = 3
    Player.last_hide = -3
    Player.hide_ready = False
    Collapseds.empty()
    explosives.empty()
    warnings.empty()
def check_collide(screen, ai_settings, Player, Collapseds, explosives,status,background,warnings):
    len1=0;
    collide_result = pygame.sprite.spritecollide(Player, Collapseds, False)
    len1+=len(collide_result)
    collide_result = pygame.sprite.spritecollide(Player, explosives, False)
    len1 += len(collide_result)
    if len1 != 0 and Player.hide == False:
        end_game(screen, ai_settings, Player, Collapseds,status,background)
    if status.game_active== False:
        reset(Player,Collapseds,explosives,warnings)


def check_buttons(screen, buttons):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for button in buttons:
        if button.rect.collidepoint(mouse_x, mouse_y):
            button.chosen = True
        else:
            button.chosen = False


def check_keydown_start(screen, status, buttons):
    for button in buttons:
        if button.chosen == True:
            button.act(status)


def check_start(screen, ai_settings, status, buttons):
    check_buttons(screen, buttons)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            check_keydown_start(screen, status, buttons)


def update_screen_start(screen, background, status, buttons, title):
    background.blitme1()
    for button in buttons:
        button.blitme()
    title.blitme()
    pygame.display.flip()


def update_screen(screen, ai_settings, Player, Collapseds, background, explosives, warnings, messages):
    # screen.fill(ai_settings.screen_color)
    background.blitme2()
    Player.blitme()
    for collapseds in Collapseds:
        collapseds.blitme()
    for warning in warnings:
        warning.blitme()
    for explosive in explosives:
        explosive.blitme()
    for message in messages:
        message.blitme()
        messages.remove(message)
    pygame.display.flip()
