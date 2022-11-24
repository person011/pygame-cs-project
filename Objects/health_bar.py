import pygame 

class HealthBar:
    def __init__(self, player):
        self.player=player

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0),  [5, 50, 210, 25])
        pygame.draw.rect(screen, (255, 0, 0), [10, 55, self.player.health*2, 15])
