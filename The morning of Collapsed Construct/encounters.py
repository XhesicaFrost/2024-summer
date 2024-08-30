import random

import pygame
import game_functions as gf
from message import Message
from explosive import Warning
from tainted_carcass import Tainted_carcass
from collapsed_construction import collapsed_construction as Collapsed_construction

class Encounter():
    def __init__(self, now_tim, kind):
        self.kind = kind
        self.begin = now_tim
        self.gap = [0, 3, 2, 3,3]
        self.warning_gap = [0, 0.8, 0.5, 1,0.5]
        self.clear_gap = [0, 0.3, 0.3, 0.3,0.5]
        self.clear = 0
        self.exe = 0
        self.la_change=now_tim
        self.tim=0
    def reini(self,now_tim,kind):
        self.clear = 0
        self.exe = 0
        self.la_change = now_tim
        self.tim = 0
        self.kind = kind
        self.begin = now_tim
        self.gap = [0, 3, 2, 3, 3]
        self.warning_gap = [0, 0.8, 0.5, 1, 0.5]
        self.clear_gap = [0, 0.3, 0.3, 0.3, 0.5]

def encounter_clear_1(Collapseds, explosives, warnings, realms, tainted_carcasses):
    Collapseds.empty()
    explosives.empty()
    # warnings.empty()
    # realms.empty()
    tainted_carcasses.empty()


def encounter_clear_2(Collapseds, explosives, warnings, realms, tainted_carcasses):
    # Collapseds.empty()
    # explosives.empty()
    # warnings.empty()
    # realms.empty()
    # tainted_carcasses.empty()
    return


def encounter_clear_3(Collapseds, explosives, warnings, realms, tainted_carcasses):
    Collapseds.empty()
    explosives.empty()
    # warnings.empty()
    # realms.empty()
    tainted_carcasses.empty()


def encounter_clear_4(Collapseds, explosives, warnings, realms, tainted_carcasses):
    #Collapseds.empty()
    # explosives.empty()
    # warnings.empty()
    # realms.empty()
    tainted_carcasses.empty()


def encounter_2_carcasses(screen, ai_settings, now_tim, tainted_carcasses):
    k = random.randint(1, 4)
    if k == 1:
        gap = random.randint(10, ai_settings.screen_height - 300)
        for i in range(10, gap, 70):
            tainted_carcass = Tainted_carcass(screen, 0, i, 0)
            tainted_carcasses.add(tainted_carcass)
        for i in range(gap + 300, ai_settings.screen_height, 70):
            tainted_carcass = Tainted_carcass(screen, 0, i, 0)
            tainted_carcasses.add(tainted_carcass)
    if k == 2:
        gap = random.randint(10, ai_settings.screen_height - 300)
        for i in range(10, gap, 70):
            tainted_carcass = Tainted_carcass(screen, ai_settings.screen_width, i, 1)
            tainted_carcasses.add(tainted_carcass)
        for i in range(gap + 300, ai_settings.screen_height, 70):
            tainted_carcass = Tainted_carcass(screen, ai_settings.screen_width, i, 1)
            tainted_carcasses.add(tainted_carcass)
    if k == 3:
        gap = random.randint(10, ai_settings.screen_width - 300)
        for i in range(10, gap, 70):
            tainted_carcass = Tainted_carcass(screen, i, 0, 2)
            tainted_carcasses.add(tainted_carcass)
        for i in range(gap + 300, ai_settings.screen_width, 70):
            tainted_carcass = Tainted_carcass(screen, i, 0, 2)
            tainted_carcasses.add(tainted_carcass)
    if k == 4:
        gap = random.randint(10, ai_settings.screen_width - 300)
        for i in range(10, gap, 70):
            tainted_carcass = Tainted_carcass(screen, i, ai_settings.screen_height, 3)
            tainted_carcasses.add(tainted_carcass)
        for i in range(gap + 300, ai_settings.screen_width, 70):
            tainted_carcass = Tainted_carcass(screen, i, ai_settings.screen_height, 3)
            tainted_carcasses.add(tainted_carcass)


def encounter_1_bombing(screen, ai_settings, now_time, warnings,k=0):
    if k==0 or k>4:
        k = random.randint(1, 4)
    cnt = 0
    ran_wid = random.randint(140, 160)
    if k == 1:
        for i in range(10, ai_settings.screen_width, ran_wid):
            warning = Warning(ai_settings, screen, i, 0, i, ai_settings.screen_height, now_time + 0.1 * cnt)
            warning.tim -= 0.5
            cnt += 1
            warnings.add(warning)
    if k == 2:
        for i in range(ai_settings.screen_width, 10, -ran_wid):
            warning = Warning(ai_settings, screen, i, 0, i, ai_settings.screen_height, now_time + 0.1 * cnt)
            warning.tim -= 0.5
            cnt += 1
            warnings.add(warning)

    if k == 3:
        for i in range(10, ai_settings.screen_height, ran_wid):
            warning = Warning(ai_settings, screen, 0, i, ai_settings.screen_width, i, now_time + 0.1 * cnt)
            warning.tim -= 0.5
            cnt += 1
            warnings.add(warning)

    if k == 4:
        for i in range(ai_settings.screen_width, 10, -ran_wid):
            warning = Warning(ai_settings, screen, 0, i, ai_settings.screen_width, i, now_time + 0.1 * cnt)
            warning.tim -= 0.5
            cnt += 1
            warnings.add(warning)


def encounter_3_airstrike(screen, ai_settings, now_time, warnings, Player):
    k = random.randint(1, 2)
    ran_wid = random.randint(20, 30)
    if k == 1:
        cnt = 0
        # print("A")
        for i in range(Player.rect.centerx, ai_settings.screen_width - 50, ran_wid):
            if i <= 50:
                continue
            warning = Warning(ai_settings, screen, i, 0, i, ai_settings.screen_height, now_time + 0.2 * cnt)
            warning.tim -= 0.5
            cnt += 1
            warnings.add(warning)
            if cnt > 30:
                break
        cnt = 0
        for i in range(Player.rect.centerx, 50, -ran_wid):
            if i >= ai_settings.screen_width - 50:
                continue
            warning = Warning(ai_settings, screen, i, 0, i, ai_settings.screen_height, now_time + 0.2 * cnt)
            warning.tim -= 0.5
            cnt += 1
            warnings.add(warning)
            if cnt > 30:
                break
    if k == 2:
        cnt = 0
        # print("A")
        for i in range(Player.rect.centery, ai_settings.screen_height - 50, ran_wid):
            if i <= 50:
                continue
            warning = Warning(ai_settings, screen, 0, i, ai_settings.screen_width, i, now_time + 0.2 * cnt)
            warning.tim -= 0.5
            cnt += 1
            warnings.add(warning)
            if cnt > 30:
                break
        cnt = 0
        for i in range(Player.rect.centerx, 50, -ran_wid):
            if i > ai_settings.screen_height - 50:
                continue
            warning = Warning(ai_settings, screen, 0, i, ai_settings.screen_width, i, now_time + 0.2 * cnt)
            warning.tim -= 0.5
            cnt += 1
            warnings.add(warning)
            if cnt > 30:
                break

def encounter_4_collapsed_constructions(screen,ai_settings,Player,Collapseds):
    k=random.randint(1,4)
    while 1:
        if k==1 and Player.rect.centerx<=ai_settings.screen_width-100:
            break
        if k==2 and Player.rect.centerx>=100:
            break
        if k==3 and Player.rect.centery<=ai_settings.screen_height-100:
            break
        if k==4 and Player.rect.centery>=100:
            break
        k=(k+1)%4+1
    gap=100
    if k==1:
        for i in range(10,ai_settings.screen_height-10,gap):
            collapsed=Collapsed_construction(ai_settings,screen,True)
            collapsed.transport(ai_settings.screen_width - 200, i)
            collapsed.update_direction(Player)
            Collapseds.add(collapsed)
        #    print(len(Collapseds))
       #     print("A")
    if k==2:
        for i in range(10,ai_settings.screen_height-10,gap):
            collapsed=Collapsed_construction(ai_settings,screen,True)
            collapsed.transport(20, i)
            collapsed.update_direction(Player)
            Collapseds.add(collapsed)
    if k==3:
        gap=200
        for i in range(10,ai_settings.screen_width-10,gap):
            collapsed=Collapsed_construction(ai_settings,screen,True)
            collapsed.transport(i,ai_settings.screen_height-20)
            collapsed.update_direction(Player)
            Collapseds.add(collapsed)
    if k==4:
        gap=200
        for i in range(10,ai_settings.screen_width-10,gap):
            collapsed=Collapsed_construction(ai_settings,screen,True)
            collapsed.transport(i,20)
            collapsed.update_direction(Player)
            Collapseds.add(collapsed)



def encounter_1_create(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                       tainted_carcasses, status, now_tim, encounter):
    if status.game_KEYDOWN == False:
        radio = ai_settings.time_speed_down
    else:
        radio = 1
    encounter.tim -= (now_tim - encounter.la_change) / radio
    encounter.la_change = now_tim
    if encounter.tim>encounter.gap[encounter.kind]-encounter.warning_gap[encounter.kind]:
        message = Message(screen, 200, 100, "!HEAVY BOMBING!", (222, 28, 49), 40, 40)
        messages.add(message)
    elif encounter.exe == 0:
        encounter_1_bombing(screen, ai_settings, now_tim, warnings)
        encounter.exe = 1
    if encounter.tim>encounter.gap[encounter.kind]-encounter.clear_gap[encounter.kind] and encounter.clear == 0:
        encounter.clear = 1
        encounter_clear_1(Collapseds, explosives, warnings, realms, tainted_carcasses)



def encounter_2_create(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                       tainted_carcasses, status, now_tim, encounter):
    if status.game_KEYDOWN == False:
        radio = ai_settings.time_speed_down
    else:
        radio = 1
    encounter.tim -= (now_tim - encounter.la_change) / radio
    encounter.la_change = now_tim
    if encounter.tim>encounter.gap[encounter.kind]-encounter.warning_gap[encounter.kind]:
        message = Message(screen, 200, 100, "!CARCASSES!", (222, 28, 49), 40, 40)
        messages.add(message)
    elif encounter.exe == 0:
        encounter_2_carcasses(screen, ai_settings, now_tim, tainted_carcasses)
        encounter.exe = 1
    if encounter.tim>encounter.gap[encounter.kind]-encounter.clear_gap[encounter.kind] and encounter.clear:
        encounter.clear = 1
        encounter_clear_2(Collapseds, explosives, warnings, realms, tainted_carcasses)



def encounter_3_create(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                       tainted_carcasses, status, now_tim, encounter):
    if status.game_KEYDOWN == False:
        radio = ai_settings.time_speed_down
    else:
        radio = 1
    encounter.tim -= (now_tim - encounter.la_change) / radio
    encounter.la_change = now_tim
    if encounter.tim>encounter.gap[encounter.kind]-encounter.warning_gap[encounter.kind]:
        message = Message(screen, 200, 100, "AIRSTRIKE", (222, 28, 49), 40, 40)
        messages.add(message)
      #  print("len=",len(messages))
    elif encounter.exe == 0:
        encounter_3_airstrike(screen, ai_settings, now_tim, warnings, Player)
        encounter.exe = 1
    if encounter.tim>encounter.gap[encounter.kind]-encounter.clear_gap[encounter.kind] and encounter.clear :
        encounter.clear = 1
        encounter_clear_3(Collapseds, explosives, warnings, realms, tainted_carcasses)

def encounter_4_create(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                       tainted_carcasses, status, now_tim, encounter):
    if status.game_KEYDOWN == False:
        radio = ai_settings.time_speed_down
    else:
        radio = 1
    encounter.tim -= (now_tim - encounter.la_change) / radio
    encounter.la_change = now_tim
    if encounter.tim>encounter.gap[encounter.kind]-encounter.warning_gap[encounter.kind]:
        message = Message(screen, 200, 100, "COLLAPSED_CONSTRUCTIONS", (222, 28, 49), 40, 30)
        messages.add(message)
    elif encounter.exe == 0:
        encounter_4_collapsed_constructions(screen, ai_settings,  Player,Collapseds)
        encounter.exe = 1
        #print("ADD=",len(Collapseds))
    if encounter.tim > encounter.gap[encounter.kind] - encounter.clear_gap[encounter.kind] and encounter.clear :
        encounter.clear = 1
        encounter_clear_4(Collapseds, explosives, warnings, realms, tainted_carcasses)
