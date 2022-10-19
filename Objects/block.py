import pygame

class Block(pygame.sprite.Sprite):
    """A class representing solid obstacles."""
    def __init__(self, color, rect):
        """The color is an (r,g,b) tuple; rect is a rect-style argument."""
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.image.fill(color)
        self.type = "normal"