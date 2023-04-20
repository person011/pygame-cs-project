import pygame 

class StaminaBar:
    def __init__(self, player):
        self.player=player
        self.smallfont = pygame.font.SysFont('Corbel', 35)
       
    def draw(self, screen):
        text = self.smallfont.render(str(self.player.stamina), True, (255, 255, 255))
        screen.blit(text, (5, 140))
        pygame.draw.rect(screen, (0, 0, 0),  [5, 110, 210, 25])
        pygame.draw.rect(screen, (253, 218, 13), [10, 115, self.player.stamina*2, 15])
