import pygame
import random
from pygame.sprite import Sprite

class Bird(Sprite):
    
    def __init__(self):
        super(Bird,self).__init__()
    
        self.imgs_explosion = [pygame.image.load(f"images/boom{i}.png").convert_alpha() for i in range(1, 9)]
        self.img_index = 1
        self.img_explosion = self.imgs_explosion[self.img_index]

        self.frame_length_max=5
        self.frame_length= self.frame_length_max

        self.images = [pygame.image.load(f"images/bird{i}.png").convert_alpha() for i in range(1, 7)]
        self.image_index = random.randint(0, 5)
        self.image = self.images[self.image_index]
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/40, self.image.get_height()/40))
        self.is_destroyed=False
        self.is_invincible= False

        self.rect = self.image.get_rect()
        self.rect.y=random.randrange(80,550)
        self.rect.x=1200
        self.vel_y=0
        self.snd_hit=pygame.mixer.Sound('sounds/hit2.ogg') 
        self.hp=2
        self.vel_x=random.randrange(3,8)
        self.lives=3
        

    def update(self,score):
        if self.rect.right < 0:
                self.kill()
                score.update_score(-5)
        self.rect.y +=self.vel_y
        self.rect.x -=self.vel_x
        if self.is_destroyed:
            max_index= 8 -1
            if self.frame_length ==0:
                    self.image=self.imgs_explosion[self.img_index]
                    self.image = pygame.transform.scale(self.image, (self.image.get_width()/4, self.image.get_height()/4))
                    self.img_index +=1
                    if self.img_index>max_index:
                        self.kill()
                    else:
                        self.frame_length =self.frame_length_max
            else:
                self.frame_length-=1
                
                
    def get_hit(self,score):
        if not self.is_invincible:
            self.hp -=1
            if self.hp <=0:
                self.snd_hit.play()
                score.update_score(5)
                self.is_invincible=True
                self.is_destroyed=True
                self.rect.x=self.rect.x +10
                self.rect.y=self.rect.y +10
                self.image=self.imgs_explosion[self.img_index]
                self.image = pygame.transform.scale(self.image, (self.image.get_width()/2, self.image.get_height()/2))
        else:
            pass
