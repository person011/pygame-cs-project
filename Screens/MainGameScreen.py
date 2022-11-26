import pygame
import os
from Properties.button import Button
from Properties.size import size_x, size_y
from Objects.player import Player
from Objects.block import Block, HurtBlock
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
        self.level = pygame.Surface((3050, 1050)).convert()
        self.overlay=pygame.display.get_surface()
        self.level_rect = self.level.get_rect()
        
        self.win_text,self.win_rect = self.make_text()
        self.obstacles = self.make_obstacles()
        #self.block_size=50
    def make_text(self):
        
        font = pygame.font.Font(None, 100)
        message = ""
        text = font.render(message, True, (100,100,175))
        rect = text.get_rect(centerx=self.level_rect.centerx, y=100)
        return text, rect

    def make_obstacles(self):
        block_size=50
        def make_block(x, y, size):
            return (x*size, y*size, size, size)
        walls = [Block(pygame.Color("chocolate"), (0,1000,3000,1)),
                 Block(pygame.Color("chocolate"), (0,0,1,1000)),
                 Block(pygame.Color("chocolate"), (3000,0,1,3000))]
        static = [Block(pygame.Color("black"), make_block(5, 19, block_size)),
                Block(pygame.Color("black"), make_block(6, 18, block_size)),
                Block(pygame.Color("black"), make_block(8, 18, block_size)),
                Block(pygame.Color("black"), make_block(8, 19, block_size)),
                Block(pygame.Color("black"), make_block(8, 17, block_size)),
                  ]
        moving = [HurtBlock(pygame.Color("red"), make_block(10, 19, block_size)),
                  ]#325
        
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
            elif event.type == pygame.KEYDOWN or event.type == pygame.K_w:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    
                    self.player.jump(self.obstacles)
            elif event.type == pygame.KEYUP or event.type == pygame.K_w:
                if event.key == pygame.K_SPACE:
                    self.player.jump_cut()
                    

    def update(self, ):
        
        self.keys = pygame.key.get_pressed()
        self.player.pre_update(self.obstacles)
        self.obstacles.update(self.player, self.obstacles)
        self.player.update(self.obstacles, self.keys, )
        self.update_viewport()

    def draw(self, ):
        
        self.level.fill((82, 84, 84))
        
        
        self.obstacles.draw(self.level)
        self.level.blit(self.win_text, self.win_rect)
        self.player.draw(self.level)
        self.screen.blit(self.level, (0,0), self.viewport)
    def draw_overlay(self):
        
        self.HealthBar.draw(self.overlay)
    def display_fps(self):
        
        caption = "{} - FPS: {:.2f}".format(CAPTION, self.clock.get_fps())
        pygame.display.set_caption(caption)
        #print(caption)
    def main_loop(self):
        
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            self.draw_overlay()
            pygame.display.update()
            self.clock.tick(self.fps)
            self.display_fps()
            
