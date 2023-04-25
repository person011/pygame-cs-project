import pygame
from Properties._Physics import _Physics
from math import sin, cos, radians

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
    def update(self):
        self.move()
    def check_collisions(self, offset, index, obstacles):
        
        unaltered = True
        self.rect[index] += offset[index]
        while pygame.sprite.spritecollideany(self, obstacles):
            self.rect[index] += (1 if offset[index]<0 else -1)
            unaltered = False
        return unaltered
    def move(self):
        direction=90
        self.rect.x += cos(radians(direction)) * self.speed
        self.rect.y += sin(radians(direction)) * self.speed
    def draw(self, surface):
        
        surface.blit(self.main_image, self.rect)