import pygame

class Start:
    def __init__(self, screen):
        self.game_started = False
        self.screen=screen
        self.image=pygame.image.load("images/start.png")
        self.image=pygame.transform.scale(self.image, (200, 100))
        self.rect=self.image.get_rect(center=(400, 200))
        self.screen_rect=self.screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx

    def start_game(self,isstart):
        self.game_started = isstart
        pygame.mixer.music.load('sounds/game_bg1.mp3')
        pygame.mixer.music.set_volume(.1)
        pygame.mixer.music.play(loops=True)


    def draw(self):
        self.screen.blit(self.image,self.rect)