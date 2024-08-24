import random
import time
import pygame
import game_functions as gf
from message import Message
import sys
import encounters as enc
from collapse_paradigm import Collapse_paradigm_nonlinear_motion
from collapse_paradigm import Collapse_paradigm_image_corruption

class Story_control():
    def __init__(self,now_tim):
        self.tim=0
        self.now_tim=0
        self.existing=0
        self.begin=now_tim
        self.last_change=now_tim
    def story_1(self,now_tim=None):
        self.reini()
        self.tim=10
        if now_tim!=None:
            self.begin=now_tim
            self.last_change = now_tim
    def story_2(self,now_tim=None):
        self.reini()
        self.tim=10
        self.la_bomb=0
        if now_tim!=None:
            self.begin=now_tim
            self.last_change = now_tim
    def story_3(self,now_tim=None):
        self.reini()
        self.tim=10
        self.la_bomb=0
        if now_tim!=None:
            self.begin=now_tim
            self.last_change = now_tim
    def story_4(self,now_tim=None):
        self.reini()
        self.tim=10
        self.la_bomb=0
        if now_tim!=None:
            self.begin=now_tim
            self.last_change = now_tim
    def reini(self):
        self.tim = 0
        self.now_tim = 0
        self.existing = 0
        self.last_change = 0
def clear_all(Collapseds, explosives, warnings, realms, tainted_carcasses):
    Collapseds.empty()
    explosives.empty()
    warnings.empty()
    realms.empty()
    tainted_carcasses.empty()
def after_story_1_message(screen,ai_settings,messages):
    # Hastily escaping from the sudden attack, you barely managed to reach the research team's previous campsite. However, what you don't know is that Ursus's artillery has already targeted this location.
    message = Message(screen, 150, 50, "Hastily escaping from the sudden attack,", text_color=(241,240,237),background_color=(92,179,204),size=25)
    messages.add(message)
    message = Message(screen, 150, 50,
                      "you barely managed to reach the research team's previous campsite.",
                      text_color=(241,240,237),background_color=(92,179,204), size=25)
    messages.add(message)
    message = Message(screen, 150, 50,\
                      "However, what you don't know is that Ursus's artillery has already ",\
                      text_color=(241,240,237),background_color=(92,179,204),size=25)
    messages.add(message)
    message = Message(screen, 150, 50, \
                      " targeted this location.", \
                      text_color=(241, 240, 237), background_color=(92, 179, 204), size=25)
    messages.add(message)
    message = Message(screen, ai_settings.screen_width / 2, ai_settings.screen_height / 2, "Press Q to continue",
                      text_color=(241, 240, 237), background_color=(67, 178, 68))
    message.blitme()
def after_story_2_message(screen,ai_settings,messages):
    # Under the bombardment of Ursus artillery, you’ve taken refuge in a forest. Clearly, Ursus's military actions have angered the northern demons. But why is the snow black, and why are there some shadowy figures lurking behind the forest?
    message = Message(screen, 150, 50, "Under the bombardment of Ursus artillery,", text_color=(241,240,237),background_color=(92,179,204),size=25)
    messages.add(message)
    message = Message(screen, 150, 50,
                      "you’ve taken refuge in a forest.",
                      text_color=(241,240,237),background_color=(92,179,204), size=25)
    messages.add(message)
    message = Message(screen, 150, 50,\
                      " Clearly, Ursus's military actions have angered the northern demons. ",\
                      text_color=(241,240,237),background_color=(92,179,204),size=25)
    messages.add(message)
    message = Message(screen, 150, 50, \
                      " But why is the snow black,", \
                      text_color=(241, 240, 237), background_color=(92, 179, 204), size=25)
    messages.add(message)
    message = Message(screen, 150, 50, \
                      " and why are there some shadowy figures lurking behind the forest?", \
                      text_color=(241, 240, 237), background_color=(92, 179, 204), size=25)
    messages.add(message)
    message = Message(screen, ai_settings.screen_width / 2, ai_settings.screen_height / 2, "Press Q to continue",
                      text_color=(241, 240, 237), background_color=(67, 178, 68))
    message.blitme()
def after_story_3_message(screen,ai_settings,messages):
    # Under the bombardment of Ursus artillery, you’ve taken refuge in a forest. Clearly, Ursus's military actions have angered the northern demons. But why is the snow black, and why are there some shadowy figures lurking behind the forest?
    message = Message(screen, 150, 50, "You feel yourself losing your sanity, ", text_color=(241,240,237),background_color=(92,179,204),size=25)
    messages.add(message)
    message = Message(screen, 150, 50,
                      "unable to even tell if you're walking in a straight line.",
                      text_color=(241,240,237),background_color=(92,179,204), size=25)
    messages.add(message)
    message = Message(screen, 150, 50,\
                      " Suddenly, the ground emits a bright light, ",\
                      text_color=(241,240,237),background_color=(92,179,204),size=25)
    messages.add(message)
    message = Message(screen, 150, 50, \
                      " and your radio crackles with the voice from headquarters.", \
                      text_color=(241, 240, 237), background_color=(92, 179, 204), size=25)
    messages.add(message)
    message = Message(screen, ai_settings.screen_width / 2, ai_settings.screen_height / 2, "Press Q to continue",
                      text_color=(241, 240, 237), background_color=(67, 178, 68))
    message.blitme()
def after_story_4_message(screen,ai_settings,messages):
    # Under the bombardment of Ursus artillery, you’ve taken refuge in a forest. Clearly, Ursus's military actions have angered the northern demons. But why is the snow black, and why are there some shadowy figures lurking behind the forest?
    message = Message(screen, 150, 50, "Regardless, you've returned to Rhode Island.  ", text_color=(241,240,237),background_color=(92,179,204),size=25)
    messages.add(message)
    message = Message(screen, 150, 50,
                      "You are safe now.",
                      text_color=(241,240,237),background_color=(92,179,204), size=25)
    messages.add(message)
    message = Message(screen, ai_settings.screen_width / 2, ai_settings.screen_height / 2, "Press Q to return to the homepage.",
                      text_color=(241, 240, 237), background_color=(67, 178, 68))
    message.blitme()
def win_story_1(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                            tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms,story_control,background):
    background.show=1
    la_change=time.time()
    pygame.mixer.music.pause()
    message = Message(screen, ai_settings.screen_width/2, ai_settings.screen_height/2, "YOU ESCAPED",text_color=(241,240,237),background_color=(67,178,68))
    message.blitme()
    pygame.display.flip()
    time.sleep(0.5)
   # print("111")
    clear_all(Collapseds, explosives, warnings, realms, tainted_carcasses)
    #print("len=", len(messages))
    time.sleep(1)
    Player.reini()
    while 1:
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key==pygame.K_q:
                status.game_KEYDOWN = False
                status.game_KEYDOWN_cnt = 0
                status.image_corruption = False
                status.chapter=2
                now_tim=time.time()
                encounter.reini(now_tim,0)
                story_control.story_2(now_tim)
                pygame.mixer.music.unpause()
                pygame.event.get()
                return
        background.showme()
        after_story_1_message(screen, ai_settings, messages)
        gf.blit_messages(screen, messages, ai_settings)
      #  print("len=",len(messages))
        pygame.display.flip()
def win_story_2(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                            tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms,story_control,background):
    pygame.mixer.music.pause()
    background.show=2
    la_change=time.time()
    message = Message(screen, ai_settings.screen_width/2, ai_settings.screen_height/2, "YOU ESCAPED",text_color=(241,240,237),background_color=(67,178,68))
    message.blitme()
    pygame.display.flip()
    time.sleep(0.5)
   # print("111")
    clear_all(Collapseds, explosives, warnings, realms, tainted_carcasses)
    #print("len=", len(messages))
    time.sleep(1)
    Player.reini()
    while 1:
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key==pygame.K_q:
                status.game_KEYDOWN = False
                status.game_KEYDOWN_cnt = 0
                status.image_corruption = False
                status.chapter=3
                now_tim=time.time()
                encounter.reini(now_tim,0)
                story_control.story_3(now_tim)
                pygame.mixer.music.unpause()
                pygame.event.get()
                return
        background.showme()
        after_story_2_message(screen, ai_settings, messages)
        gf.blit_messages(screen, messages, ai_settings)
      #  print("len=",len(messages))
        pygame.display.flip()
def win_story_3(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                            tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms,story_control,background):
    pygame.mixer.music.pause()
    background.show=3
    la_change=time.time()
    message = Message(screen, ai_settings.screen_width/2, ai_settings.screen_height/2, "YOU ESCAPED",text_color=(241,240,237),background_color=(67,178,68))
    message.blitme()
    pygame.display.flip()
    time.sleep(0.5)
   # print("111")
    clear_all(Collapseds, explosives, warnings, realms, tainted_carcasses)
    #print("len=", len(messages))
    time.sleep(1)
    Player.reini()
    while 1:
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key==pygame.K_q:
                status.game_KEYDOWN = False
                status.game_KEYDOWN_cnt = 0
                status.image_corruption = False
                status.chapter=4
                now_tim=time.time()
                encounter.reini(now_tim,0)
                story_control.story_4(now_tim)
                pygame.mixer.music.unpause()
                pygame.event.get()
                return
        background.showme()
        after_story_3_message(screen, ai_settings, messages)
        gf.blit_messages(screen, messages, ai_settings)
      #  print("len=",len(messages))
        pygame.display.flip()
def win_story_4(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                            tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms,story_control,background):
    pygame.mixer.music.load('music/win.mp3')
    pygame.mixer.music.play(loops=-1)
    background.show=4
    la_change=time.time()
    message = Message(screen, ai_settings.screen_width/2, ai_settings.screen_height/2, "You are completely safe now",text_color=(241,240,237),background_color=(67,178,68))
    message.blitme()
    pygame.display.flip()
    time.sleep(0.5)
   # print("111")
    clear_all(Collapseds, explosives, warnings, realms, tainted_carcasses)
    #print("len=", len(messages))
    time.sleep(1)
    Player.reini()
    while 1:
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key==pygame.K_q:
                status.game_KEYDOWN = False
                status.game_KEYDOWN_cnt = 0
                gf.reset(Player, Collapseds, explosives, warnings, realms, tainted_carcasses,status,encounter,collapsed_paradigm_list,collapsed_paradigms,ai_settings)
                status.game_active = False
                return
        background.showme()
        after_story_4_message(screen, ai_settings, messages)
        gf.blit_messages(screen, messages, ai_settings)
      #  print("len=",len(messages))
        pygame.display.flip()
def update_story_1(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                            tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms,story_control,background):
        now_tim = time.time()
        if now_tim-story_control.begin<=1:
            message = Message(screen, 150, 50, "LEAVE NOW", background_color=40)
            messages.add(message)
            message = Message(screen, 150, 50, "Collapsed_constuction will track you", background_color=40)
            messages.add(message)
            return
        elif now_tim-story_control.begin<=2:
            message = Message(screen,150,50,"USE WASD TO MOVE",background_color=(43, 155, 175))
            messages.add(message)
        elif now_tim-story_control.begin<=3:
            message = Message(screen,150,50,"USE SPACE TO HIDE",background_color=(43, 155, 175))
            messages.add(message)
        elif now_tim-story_control.begin<=4:
             message = Message(screen,150,50,"USE SHIFT TO RUN",background_color=(43, 155, 175))
             messages.add(message)
        elif now_tim-story_control.begin<=5:
             message = Message(screen, 150, 50, "HIDE FROM ENEMIES", background_color=(43, 155, 175))
             messages.add(message)
             message = Message(screen, 150, 50, "HOLD ON FOR SECONDS", background_color=(43, 155, 175))
             messages.add(message)
             story_control.last_change=now_tim
           #  print("Lastupdate=",story_control.last_change)
        elif story_control.existing<=story_control.tim:
             ai_settings.num_collapseds=5
             gf.random_try_create_collapseds(screen, ai_settings, Player, Collapseds, status)
             radio = gf.get_radio(status, ai_settings)
             story_control.existing += (now_tim-story_control.last_change)/radio
             story_control.last_change=now_tim
        else :
             print("AA")
             win_story_1(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                            tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms,story_control,background)
        #print("last=",story_control.last_change)
        Player.update()
        if now_tim-story_control.begin>=2:
            gf.update_K_SPACE(Player, screen, messages, status, ai_settings)
        gf.update_collapseds(screen, ai_settings, Player, Collapseds,status)
        gf.check_collide(screen, ai_settings, Player, Collapseds, explosives, status, background, warnings, realms,
                         tainted_carcasses, encounter, collapsed_paradigm_list, collapsed_paradigms)


def update_story_2(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                   tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms, story_control,
                   background):
    now_tim = time.time()
    if now_tim - story_control.begin <= 1:
        message = Message(screen, 150, 50, "Target!@#lock$%#", background_color=40)
        messages.add(message)
        message = Message(screen, 150, 50, "Destroy...all---collapsing...bodies", background_color=40)
        messages.add(message)
        return
    elif now_tim-story_control.begin<= 2:
        message = Message(screen, 150, 50, "Glory to@#@Ursus", background_color=40)
        messages.add(message)
    elif now_tim - story_control.begin <= 3:
        message = Message(screen, 150, 50, "Beware of artillery fire", background_color=(43, 155, 175))
        messages.add(message)
        message = Message(screen, 150, 50, "Stay alive", background_color=(43, 155, 175))
        messages.add(message)
    #  print("Lastupdate=",story_control.last_change)
    elif now_tim - story_control.begin <= 9:
        #print(la_bomb,now_tim)
        if now_tim-story_control.la_bomb<=1:
            story_control.last_change = now_tim
        else:
            story_control.last_change = now_tim
            enc.encounter_1_bombing(screen, ai_settings, now_tim, warnings,int(now_tim - story_control.begin))
            story_control.la_bomb=now_tim
    elif story_control.existing <= story_control.tim:
        ai_settings.num_collapseds = 1
        ai_settings.num_warnings=5
        gf.random_try_create_collapseds(screen, ai_settings, Player, Collapseds, status)
        gf.random_try_create_warnings(screen, ai_settings, warnings, explosives, now_tim, status)
        if now_tim-story_control.la_bomb<=3 and encounter.kind==0:
            encounter.kind=random.randint(1,2)
            if encounter.kind==1:
                encounter.kind = 1
                encounter.begin = now_tim
                encounter.tim = encounter.gap[encounter.kind]
                encounter.la_change = now_tim
            if encounter.kind==2:
                encounter.la_change = now_tim
                # return
                encounter.tim = encounter.gap[encounter.kind]
                encounter.kind = 3
                encounter.begin = now_tim
            print("SUS")
        if encounter.kind !=0:
            gf.update_encounter(encounter, now_tim, status, ai_settings)
            print("UPDATE")
            if encounter.kind==1:
                enc.encounter_1_create(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                       tainted_carcasses, status, now_tim, encounter)

            elif encounter.kind==2:
                enc.encounter_3_create(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                                   tainted_carcasses, status, now_tim, encounter)
            story_control.la_bomb = now_tim
        radio = gf.get_radio(status, ai_settings)
        story_control.existing += (now_tim - story_control.last_change) / radio
        story_control.last_change = now_tim
    else:
        print("AA")
        win_story_2(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                    tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms, story_control,
                    background)
    # print("last=",story_control.last_change)
    Player.update()
    gf.update_K_SPACE(Player, screen, messages, status, ai_settings)
    gf.update_collapseds(screen, ai_settings, Player, Collapseds, status)
    gf.update_warnings(screen,ai_settings, warnings, explosives, now_tim, status)
    gf.check_collide(screen, ai_settings, Player, Collapseds, explosives, status, background, warnings, realms,
                     tainted_carcasses, encounter, collapsed_paradigm_list, collapsed_paradigms)
def update_story_3(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                   tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms, story_control,
                   background):
    now_tim = time.time()
    if now_tim - story_control.begin <= 1:
        message = Message(screen, 150, 50, "Tainted_carcass watches you from behind the trees", background_color=40)
        messages.add(message)
    elif now_tim-story_control.begin<= 2:
        message = Message(screen, 150, 50, "realms have darkened the world.", background_color=40)
        messages.add(message)
    #  print("Lastupdate=",story_control.last_change)
    elif now_tim - story_control.begin <= 6:
        #print(la_bomb,now_tim)
        if now_tim-story_control.la_bomb<=1:
            story_control.last_change = now_tim
        else:
            story_control.last_change = now_tim
            k=random.randint(1,2)
            if k==1:
                enc.encounter_4_collapsed_constructions(screen,ai_settings,Player,Collapseds)
            else:
                enc.encounter_2_carcasses(screen, ai_settings, now_tim, tainted_carcasses)
            story_control.la_bomb=now_tim
    elif story_control.existing <= story_control.tim:
        ai_settings.num_collapseds = 2
        ai_settings.num_warnings=3
        ai_settings.num_realms=10
        ai_settings.num_tainted_carcasses=5
        gf.random_try_create_realms(screen, ai_settings, realms, Player, now_tim)
        gf.random_try_create_collapseds(screen, ai_settings, Player, Collapseds, status)
        gf.random_try_create_warnings(screen, ai_settings, warnings, explosives, now_tim, status)
        gf.random_try_create_tainted_carcassed(screen, ai_settings, tainted_carcasses, Player, status)
        if now_tim-story_control.la_bomb<=3 and encounter.kind==0:
            encounter.kind=random.randint(1,4)
            encounter.begin = now_tim
            encounter.tim = encounter.gap[encounter.kind]
            encounter.la_change = now_tim
            print("SUS")
        if encounter.kind !=0:
            gf.update_encounter(encounter, now_tim, status, ai_settings)
            print("UPDATE")
            if encounter.kind==1:
                enc.encounter_1_create(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                       tainted_carcasses, status, now_tim, encounter)
            elif encounter.kind == 2:
                enc.encounter_2_create(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                                       tainted_carcasses, status, now_tim, encounter)
            elif encounter.kind == 3:
                enc.encounter_3_create(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                                       tainted_carcasses, status, now_tim, encounter)
            elif encounter.kind == 4:
                enc.encounter_4_create(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                                       tainted_carcasses, status, now_tim, encounter)
            story_control.la_bomb = now_tim
        radio = gf.get_radio(status, ai_settings)
        story_control.existing += (now_tim - story_control.last_change) / radio
        story_control.last_change = now_tim
    else:
        print("AA")
        win_story_3(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                    tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms, story_control,
                    background)
    # print("last=",story_control.last_change)
    Player.update()
    gf.update_K_SPACE(Player, screen, messages, status, ai_settings)
    gf.update_collapseds(screen, ai_settings, Player, Collapseds, status)
    gf.update_tainted_carcasses(screen, ai_settings, tainted_carcasses, Player,status)
    gf.update_warnings(screen,ai_settings, warnings, explosives, now_tim, status)
    gf.update_realms(screen, ai_settings, realms, Player, now_tim)
    gf.update_tainted_carcasses(screen, ai_settings, tainted_carcasses, Player, status)
    gf.check_collide(screen, ai_settings, Player, Collapseds, explosives, status, background, warnings, realms,
                     tainted_carcasses, encounter, collapsed_paradigm_list, collapsed_paradigms)
def update_story_4(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                   tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms, story_control,
                   background):
    now_tim = time.time()
    if now_tim - story_control.begin <= 1:
        message = Message(screen, 150, 50, "Survive the siege", background_color=(43, 155, 175))
        messages.add(message)
        message = Message(screen, 150, 50, "Rescue is on the way.", background_color=(43, 155, 175))
        messages.add(message)
    elif now_tim-story_control.begin<= 2:
        message = Message(screen, 150, 50, "Hang in there.", background_color=(43, 155, 175))
        messages.add(message)
    #  print("Lastupdate=",story_control.last_change)
    elif now_tim - story_control.begin <= 3:
        #print(la_bomb,now_tim)
        if collapsed_paradigm_list.active[0] ==False:
            collapsed_paradigm_list.active[0] = True
            collapsed_paradigm = Collapse_paradigm_nonlinear_motion(screen, now_tim)
            collapsed_paradigm.act(Player)
            collapsed_paradigms.add(collapsed_paradigm)
        if collapsed_paradigm_list.active[1] == False:
            collapsed_paradigm_list.active[1] = True
            collapsed_paradigm = Collapse_paradigm_image_corruption(screen, now_tim)
            collapsed_paradigm.act(status)
            collapsed_paradigms.add(collapsed_paradigm)
    elif story_control.existing <= story_control.tim:
        ai_settings.num_collapseds = 2
        ai_settings.num_warnings=3
        ai_settings.num_realms=10
        ai_settings.num_tainted_carcasses=5
        gf.random_try_create_realms(screen, ai_settings, realms, Player, now_tim)
        gf.random_try_create_collapseds(screen, ai_settings, Player, Collapseds, status)
        gf.random_try_create_warnings(screen, ai_settings, warnings, explosives, now_tim, status)
        gf.random_try_create_tainted_carcassed(screen, ai_settings, tainted_carcasses, Player, status)
        if now_tim-story_control.la_bomb<=4 and encounter.kind==0:
            encounter.kind=random.randint(1,4)
            encounter.begin = now_tim
            encounter.tim = encounter.gap[encounter.kind]
            encounter.la_change = now_tim
            print("SUS")
        if encounter.kind !=0:
            gf.update_encounter(encounter, now_tim, status, ai_settings)
            print("UPDATE")
            if encounter.kind==1:
                enc.encounter_1_create(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                       tainted_carcasses, status, now_tim, encounter)
            elif encounter.kind == 2:
                enc.encounter_2_create(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                                       tainted_carcasses, status, now_tim, encounter)
            elif encounter.kind == 3:
                enc.encounter_3_create(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                                       tainted_carcasses, status, now_tim, encounter)
            elif encounter.kind == 4:
                enc.encounter_4_create(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                                       tainted_carcasses, status, now_tim, encounter)
            story_control.la_bomb = now_tim
        radio = gf.get_radio(status, ai_settings)
        story_control.existing += (now_tim - story_control.last_change) / radio
        story_control.last_change = now_tim
    else:
        print("AA")
        win_story_4(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                    tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms, story_control,
                    background)
    # print("last=",story_control.last_change)
    Player.update()
    gf.update_K_SPACE(Player, screen, messages, status, ai_settings)
    gf.update_collapseds(screen, ai_settings, Player, Collapseds, status)
    gf.update_tainted_carcasses(screen, ai_settings, tainted_carcasses, Player,status)
    gf.update_warnings(screen,ai_settings, warnings, explosives, now_tim, status)
    gf.update_realms(screen, ai_settings, realms, Player, now_tim)
    gf.update_tainted_carcasses(screen, ai_settings, tainted_carcasses, Player, status)
    gf.check_collide(screen, ai_settings, Player, Collapseds, explosives, status, background, warnings, realms,
                     tainted_carcasses, encounter, collapsed_paradigm_list, collapsed_paradigms)
def update_story(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                            tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms,background):
    now_tim = time.time()
    story_control = Story_control(now_tim)
    story_control.story_1(now_tim)
    fps = 60
    background.show=0
    clock = pygame.time.Clock()
    if status.chapter==0:
        story_control.story_1()
    while True:
        if status.chapter==1:
            gf.check_event(screen,ai_settings, Player, status)
            update_story_1(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                                tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms,story_control,background)
            if status.chapter==2:
                print(status.game_KEYDOWN_cnt,status.game_KEYDOWN)
        if status.chapter==2:
            gf.check_event(screen, ai_settings, Player, status)
            update_story_2(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                           tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms,
                           story_control, background)
        if status.chapter==3:
            gf.check_event(screen, ai_settings, Player, status)
            update_story_3(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                           tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms,
                           story_control, background)
        if status.chapter==4:
            gf.check_event(screen, ai_settings, Player, status)
            update_story_4(screen, ai_settings, Player, Collapseds, explosives, warnings, messages, realms,
                           tainted_carcasses, status, encounter, collapsed_paradigm_list, collapsed_paradigms,
                           story_control, background)
        gf.update_screen(screen, ai_settings, Player, Collapseds, background, explosives, warnings, messages,
                             realms, tainted_carcasses, collapsed_paradigms, status)
        if status.game_active==False:
            return
        clock.tick(fps)