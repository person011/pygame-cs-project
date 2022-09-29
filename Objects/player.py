#from tkinter import image_names
import pygame

#from Properties.size import size, size_x, size_y
import math
import time
class Player:
    def __init__(self, screen, spawn_x, spawn_y, width, height, image):
        self.x=spawn_x
        self.y=spawn_y
        self.width=width
        self.height=height
        self.vel=10
        self.l_touched=False
        self.isJump = False
        self.jumpCount = 10
        self.image=image
        self.screen=screen
    def movement(self, keys):
        
        
        if keys[pygame.K_LEFT]:
            if self.l_touched==False:
                self.x-=self.vel
        elif keys[pygame.K_RIGHT]:
            self.x+=self.vel
    def jump(self):
        pygame.time.delay(5)
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.4 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
     
    def draw(self):
        pygame.draw.rect(self.screen, (0, 255, 0),[self.x, self.y, self.width, self.height])