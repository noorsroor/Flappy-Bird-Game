import pygame
from pygame.sprite import Sprite

class Shot(Sprite):
    def __init__(self, screen,player ):
        super(Shot,self).__init__()
        self.screen=screen
        self.player=player
        self.image=pygame.image.load("images/shot.png")
        self.image=pygame.transform.scale(self.image, (50, 20))
        self.rect=self.image.get_rect()
        self.rect.left=50
        self.rect.centery =player.get_rect()+18
        self.x=float(player.rect.x)+100
        self.shot_speed=10
        self.end_shoot=pygame.mixer.Sound('sounds/shot2.ogg')

    def update(self):
        self.x +=self.shot_speed
        self.rect.x=self.x

    def draw(self):
        self.screen.blit(self.image,self.rect)  

    