import pygame
import sys 
import random
from settings import Sittings
import functions as fun
from startb import Start
from player import Player
from bird import Bird
from pygame.sprite import Sprite
from shot import Shot
from bird_spawner import BirdSpawner
from score import Score
from lives import Lives
from alert_box import AlertBox


def run_game():
    #pygame initialization
    pygame.mixer.pre_init(44100, -16 , 2, 512)
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    
    #Display setup
    ai_setting = Sittings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Shooting Flappy Birds")
    icon_image = pygame.image.load("images/bird.png")
    pygame.display.set_icon(icon_image) 
    bg_color = (230, 230, 230)

    #Object setup
    start = Start(screen)

    player=Player(screen)
    sprite_group=pygame.sprite.Group()
    sprite_group.add(player) 

    shots=pygame.sprite.Group()

    bird_spawner=BirdSpawner()

    score=Score()
    score_group=pygame.sprite.Group()
    score_group.add(score)

    lives=Lives(3)
    lives_group=pygame.sprite.Group()
    lives_group.add(lives)
    
    alert_box_group=pygame.sprite.Group()
    alert_box=AlertBox(score.value,screen)
    alert_box_group.add(alert_box)

    while True:
        pygame.mixer.music.load('sounds/Start_bg.mp3')
        pygame.mixer.music.set_volume(.4)
        pygame.mixer.music.play(loops=True)
        spawn_timer=random.randrange(30,120)
        fun.check_event(screen,player,shots,start,sprite_group)
        #check if the game is started (to decide which screen to show)
        while not start.game_started:
            fun.start_screen(ai_setting, screen, start,player,shots,sprite_group)
        else:    
            fun.game_screen(ai_setting, screen,player,shots,start,bird_spawner,sprite_group,score_group,score,lives_group,lives,alert_box_group)
        
        if not player.is_alive:
            while not start.game_started:
                fun.start_screen(ai_setting, screen, start,player,shots,sprite_group)
            else:    
                fun.game_screen(ai_setting, screen,player,shots,start,bird_spawner,sprite_group,score_group,score,lives_group,lives,alert_box_group)
run_game()








