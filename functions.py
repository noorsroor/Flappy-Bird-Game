import pygame
import sys
from startb import Start
import math
from player import Player
from shot import Shot
from bird_spawner import BirdSpawner

#check event function 
def check_event(screen,player,shots,start,sprite_group):
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit
            elif event.type==pygame.KEYDOWN:
                if event.key ==pygame.K_UP:
                    player.moving_up=True
                elif event.key ==pygame.K_DOWN:
                    player.moving_down=True
                elif event.key==pygame.K_SPACE:
                    if player.is_alive:
                        if len(shots)<10:
                            new_shot=Shot(screen,player)
                            shots.add(new_shot)
                            new_shot.end_shoot.play()
            elif event.type==pygame.KEYUP:
                if event.key ==pygame.K_UP:
                    player.moving_up=False
                elif event.key ==pygame.K_DOWN:
                    player.moving_down=False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                if start.rect.collidepoint(event.pos):
                    tap=pygame.mixer.Sound('sounds/tap1.wav')
                    tap.play()
                    if player.is_alive:
                       start.start_game(True)
                    else:
                        start.start_game(False)
    pygame.display.flip()



            
        
#function to create the start screen 
def start_screen(ai_setting, screen, start,player,shots,sprite_group):
    background = pygame.image.load("images/SBackground.png")
    background = pygame.transform.scale(background, (ai_setting.screen_width, ai_setting.screen_height))
    screen.blit(background, (0, 0))
    start.draw()
    check_event(screen,player,shots,start,sprite_group)




#function to create the game screen 
def game_screen(ai_setting, screen,player,shots,start,bird_spawner,sprite_group,score_group,score,lives_group,lives,alert_box_group):
    clock = pygame.time.Clock()
    FPS = 60
    bg = pygame.image.load("images/bg.png").convert()
    bg_width = bg.get_width()
   
    scroll = 0
    scroll_speed = 10
    tiles = ai_setting.screen_width // bg_width + 2
    
    num=3

    run = True
    while run:
        clock.tick(FPS)
        for i in range(tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))

        sprite_group.update()
        sprite_group.draw(screen)
        
        bird_spawner.update(score)
        bird_spawner.bird_group.draw(screen)
        
        lives.update_life(lives_group,num)
        lives_group.draw(screen)
        

        for shot in shots.sprites():
            if shot.rect.left <= ai_setting.screen_width:
                shot.update()
                shot.draw()
            else:
                shots.remove (shot) 
 
       
        #Check Collision..................................
        collided=pygame.sprite.groupcollide(shots , bird_spawner.bird_group , True,False)
        for shot ,bird in collided.items():
            bird[0].get_hit(score)
            if not bird[0].is_invincible:
                pass
        


        collided=pygame.sprite.groupcollide(sprite_group , bird_spawner.bird_group , False,True)
        for plr, bird in collided.items():
                plr.get_hit()
                print(player.lives)
                
     
           

        score_group.update()
        score_group.draw(screen)
        
         
         #check for game over 
        if not player.is_alive:
            bird_spawner.clear_birds()
            lives.clear_lives(lives_group)
            alert_box_group.update(score.value,screen)
            alert_box_group.draw(screen)
            start.start_game(False)
            start.draw()
            

        #check event.........................................
        check_event(screen,player,shots,start,sprite_group)
        pygame.display.flip()

        # Scroll background
        scroll -= scroll_speed

        # Reset scroll
        if abs(scroll) > bg_width:
            scroll = 0


    
    pygame.quit()


