import pygame
import os
from Properties.button import Button
from Properties.size import size_x, size_y
from Objects.player import Player
from Objects.block import Block, MovingBlock
from Objects.health_bar import HealthBar
from config import *


class MainGameScreen(object):
    
    def __init__(self):
        
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        #print(self.screen_rect)
        self.clock = pygame.time.Clock()
        self.fps = 60.0
        self.keys = pygame.key.get_pressed()
        self.done = False
        self.player = Player((50,875), 4, (50, 875))
        self.viewport = self.screen.get_rect()
        #print(self.viewport)
        self.HealthBar=HealthBar(self.player)
        self.level = pygame.Surface((3050, 1000)).convert()
        
        self.level_rect = self.level.get_rect()
        
        self.win_text,self.win_rect = self.make_text()
        self.obstacles = self.make_obstacles()
        
    def make_text(self):
        
        font = pygame.font.Font(None, 100)
        message = ""
        text = font.render(message, True, (100,100,175))
        rect = text.get_rect(centerx=self.level_rect.centerx, y=100)
        return text, rect

    def make_obstacles(self):
        
        walls = [Block(pygame.Color("chocolate"), (0,980,3000,1)),
                 Block(pygame.Color("chocolate"), (0,0,1,1000)),
                 Block(pygame.Color("chocolate"), (3000,0,1,3000))]
        static = [Block(pygame.Color("black"), (250,880,200,100)),
                
                  ]
        moving = [MovingBlock(pygame.Color("black"), (200,740,75,20), 325, 0),
                  ]
        return pygame.sprite.Group(walls, static, moving)

    def update_viewport(self):
        
        
        self.viewport.center = self.player.rect.center
        #print(self.viewport.center)
        self.viewport.clamp_ip(self.level_rect)

    def event_loop(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if self.keys[pygame.K_ESCAPE]:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.jump(self.obstacles)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player.jump_cut()

    def update(self):
        
        self.keys = pygame.key.get_pressed()
        self.player.pre_update(self.obstacles)
        self.obstacles.update(self.player, self.obstacles)
        self.player.update(self.obstacles, self.keys)
        self.update_viewport()

    def draw(self):
        
        self.level.fill((82, 84, 84))
        self.HealthBar.draw(self.level)
        self.obstacles.draw(self.level)
        self.level.blit(self.win_text, self.win_rect)
        self.player.draw(self.level)
        self.screen.blit(self.level, (0,0), self.viewport)

    def display_fps(self):
        
        caption = "{} - FPS: {:.2f}".format(CAPTION, self.clock.get_fps())
        pygame.display.set_caption(caption)
        #print(caption)
    def main_loop(self):
        
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(self.fps)
            self.display_fps()
