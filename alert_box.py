import pygame
from pygame.sprite import Sprite

class AlertBox(Sprite): 
    def __init__(self,score,screen):
        super(AlertBox,self).__init__()
        self.screen=screen
        self.font_size=60
        self.color=(255, 0, 0)
        self.font=pygame.font.Font('PixelGameFont.ttf',self.font_size)
        self.image=self.font.render(str(f'GAME OVER  YOUR SCORE: {score}'),False,self.color)
        self.rect=self.image.get_rect()
        self.rect.center = screen.get_rect().center
        self.vel_y=0
        self.vel_x=0


    def update(self,score,screen):
        self.image=self.font.render(str(f'GAME OVER  YOUR SCORE: {score}'),False,self.color)
        self.rect=self.image.get_rect()
        self.rect.center = screen.get_rect().center
        self.vel_y=0
        self.vel_x=0
