import pygame
from pygame.sprite import Sprite

class Lives(Sprite):
    def __init__(self, num_lives):
        super(Lives, self).__init__()
        self.image = pygame.image.load("images/heart1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 10, self.image.get_height() // 10))
        self.rect = self.image.get_rect()
        self.rect.y = 10
        self.rect.x = 1100
        self.num_of_lives = num_lives
        self.vel_x = 10
        



    def update_life(self,lives_group,num):    
        for i in range(num):
            heart = Lives(num)  # Pass the current number of lives
            heart.rect.x -= i * (heart.rect.width + 5)  # Adjust the x-coordinate to space hearts out
            lives_group.add(heart)
    
    def draw(self, screen):
        for lives in self.groups():
            screen.blit(lives.image, lives.rect)

    def clear_lives(self,lives_group):
        for live in lives_group:
            live.kill()




        



