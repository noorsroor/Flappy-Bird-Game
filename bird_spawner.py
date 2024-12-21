import pygame
from bird import Bird
import random


class BirdSpawner:
    def __init__(self):
        self.bird_group=pygame.sprite.Group()
        self.spawn_timer=random.randrange(30,120)

    def update(self,score):
        self.bird_group.update(score)
        if self.spawn_timer==0:
            self.spawn_bird()
            self.spawn_timer=random.randrange(30,120)
        else:
            self.spawn_timer-=1

    def spawn_bird(self):
        new_bird=Bird()
        self.bird_group.add(new_bird)

    def clear_birds(self):
        for bird in self.bird_group:
            bird.kill()