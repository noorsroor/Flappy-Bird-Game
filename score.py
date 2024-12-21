import pygame
from pygame.sprite import Sprite

class Score(Sprite):
    def __init__(self):
        super(Score,self).__init__()
        self.value=0
        self.font_size=25
        self.color=(0,0,0)
        self.font=pygame.font.Font('PixelGameFont.ttf',self.font_size)
        self.image=self.font.render(str(f'Score: {self.value}'),False,self.color)
        self.rect=self.image.get_rect()
        self.rect.x=10
        self.rect.y=10

    def update(self):
        pass

    def update_score(self,value):
        self.value+=value
        self.image=self.font.render(str(f'Score: {self.value}'),False,self.color)
        self.rect=self.image.get_rect()
        self.rect.x=10
        self.rect.y=10
