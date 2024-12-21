import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, screen):
        super(Player,self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/4, self.image.get_height()/4))
        self.rect = self.image.get_rect()
        self.rect.left = 50
        self.rect.centery = screen.get_rect().centery
        self.moving_up=False
        self.moving_down=False
        self.hp=1
        self.lives=3
        self.is_alive=True

    def get_rect(self):
        return self.rect.centery
    
    def update(self):
        if self.moving_up and self.rect.top > 10 :
            self.rect.centery-=10
        elif self.moving_down and self.rect.bottom <650:
            self.rect.centery+=10
   
    def get_hit(self):
        self.hp -=1
        if self.hp<=0:
            self.hp=0
            self.death()
          
    def death(self):
        self.lives -=1
        if self.lives <=0:
           self.lives=0
           self.is_alive=False
           self.image=pygame.transform.scale(self.image, (self.image.get_width()/100, self.image.get_height()/100))
           tap=pygame.mixer.Sound('sounds/gameOver2.wav')
           tap.play()
        self.hp=1

    def draw(self):
        self.screen.blit(self.image, self.rect)
        #self.screen.blit(self.home, self.home_rect)