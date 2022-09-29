import pygame
class Box:
    def __init__(self, screen, spawn_x, spawn_y, image):
        self.screen=screen
        self.x=spawn_x
        self.y=spawn_y
        self.image=image
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))