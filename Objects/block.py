import pygame
from Properties.collision import Collide
class Box:
    def __init__(self, screen, spawn_x, spawn_y, image):
        self.screen=screen
        self.x=spawn_x
        self.y=spawn_y
        self.width=width
        self.height=height
        self.image=image
    def collision(self, player):
        collide=Collide(self.x, self.y, self.width, self.height, player.x, player.y, player.width, player.height)
        if collide.collide_right():
            player.x-=player.vel
        
        if collide.collide_left():
            player.x+=player.vel
        player.bottom_t=collide.collide_bottom()
        player.top_t=collide.collide_top()
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))