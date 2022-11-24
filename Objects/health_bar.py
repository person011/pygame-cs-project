import pygame 

class HealthBar:
    def __init__(self, player):
        self.player=player

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0),  [0, 50, 200, 50])
