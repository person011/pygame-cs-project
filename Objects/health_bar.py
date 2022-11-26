import pygame 

class HealthBar:
    def __init__(self, player):
        self.player=player
        self.smallfont = pygame.font.SysFont('Corbel', 35)
       
    def draw(self, screen):
        text = self.smallfont.render(str(self.player.health), True, (255, 255, 255))
        screen.blit(text, (5, 80))
        pygame.draw.rect(screen, (0, 0, 0),  [5, 50, 210, 25])
        pygame.draw.rect(screen, (255, 0, 0), [10, 55, self.player.health*2, 15])
