import pygame
from Properties._Physics import _Physics
from math import sin, cos, radians, atan, degrees
import numpy as np

class Bat(pygame.sprite.Sprite):
    def __init__(self, location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/bat.png')
        
        self.image_left=pygame.transform.flip(self.image, True, False)
        self.main_image=self.image
        self.rect = self.image.get_rect(topleft=location)
        self.original_speed=speed
        self.speed = speed
        self.spawn_point=location
    def update(self, player):
        self.move(player)
    def check_collisions(self, offset, index, obstacles):
        
        unaltered = True
        self.rect[index] += offset[index]
        while pygame.sprite.spritecollideany(self, obstacles):
            self.rect[index] += (1 if offset[index]<0 else -1)
            unaltered = False
        return unaltered
    def angle_between(self, p1, p2):
        ang1 = np.arctan2(*p1[::-1])
        ang2 = np.arctan2(*p2[::-1])
        return np.rad2deg((ang1 - ang2) % (2 * np.pi))
    def move(self, player):
        y_coordinates=[self.rect.y, player.rect.y]
        y_coordinates.sort()
        x_coordinates=[self.rect.x, player.rect.x]
        x_coordinates.sort()
        angle=atan((y_coordinates[1]-y_coordinates[0])/(x_coordinates[1]-x_coordinates[0]))
        direction=450-self.angle_between((self.rect.x, self.rect.y), (player.rect.x, player.rect.y))
        #print(direction)
        print(self.rect.x, self.rect.y)
        #direction=115
        #print(angle, degrees(angle))
        self.rect.x += cos(radians(direction)) * self.speed
        self.rect.y += sin(radians(direction)) * self.speed
    def draw(self, surface):
        
        surface.blit(self.main_image, self.rect)