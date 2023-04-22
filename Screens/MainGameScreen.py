import pygame
import os
from Properties.button import Button
from Properties.size import size_x, size_y
from Objects.player import Player
from Objects.block import Block, HurtBlock
from Objects.health_bar import HealthBar
from Objects.stamina_bar import StaminaBar
from config import *
from Objects.fps import show_fps
from MainGameScreenConfig import *
from Properties.make_block import make_block
from Objects.landscape import Landscape
from Properties.make_mountains import make_mountain
from Objects.block import block_map

class MainGameScreen(object):
    
    def __init__(self):
        
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        #print(self.screen_rect)
        self.clock = pygame.time.Clock()
        self.fps = 60.0
        self.keys = pygame.key.get_pressed()
        self.done = False
        self.player = Player((50,300), 4, (50, 300))
        self.viewport = self.screen.get_rect()
        #print(self.viewport)
        self.HealthBar=HealthBar(self.player)
        self.StaminaBar=StaminaBar(self.player)
        #3050, 1050
        self.level = pygame.Surface((5050, 2050)).convert()
        self.overlay=pygame.display.get_surface()
        self.level_rect = self.level.get_rect()
        #print(self.level_rect)
        #self.win_text,self.win_rect = self.make_text()
        
        self.obstacles = self.make_obstacles()
        #self.block_size=50
    def make_text(self):
        
        font = pygame.font.Font(None, 100)
        message = str(self.fps)
        fps = font.render(message, True, (100,100,175))
        #rect = fps.get_rect(centerx=self.level_rect.centerx, y=100)
        #fps = self.smallfont.render(str(MainGameScreen.fps), True, (255, 255, 255))
        
        #return fps, rect
    
    def make_obstacles(self):
        walls = [Block((0, WALL_HEIGHT,WALL_WIDTH,1),color=pygame.Color("chocolate"), type="wall"),
                 Block((0,0,1,WALL_HEIGHT),color=pygame.Color("chocolate"), type="wall"),
                 Block((WALL_WIDTH,0,1,WALL_HEIGHT),color=pygame.Color("chocolate"), type="wall"),
                 Block((0,0,WALL_WIDTH,0),color=pygame.Color("chocolate"), type="wall")]
            #60
        
        #static= [Block(make_block(i, i%60, block_size), color=pygame.Color("black")) for i in range(1200)]
        static= [Block( make_block(12, 9, BLOCK_SIZE), color=pygame.Color("black"))]
        """for i in range(100):
            for ii in range(10):
                static.append(Block(make_block(i, 19-ii, block_size), color=pygame.Color("black")))"""
        
        for i in range(100):
            for ii in range(1):
                static.append(Block(make_block(i, 39-ii, BLOCK_SIZE), color=pygame.Color("black")))
        #moving = [HurtBlock(make_block(10, 9, block_size), color=pygame.Color("red")),
                  #]#325
        moving=[]
        #10, -11, 100, 20
        landscape=Landscape((0, 23, 100, 15), block_map)
        for i in range(10):
            make_mountain(landscape)
        
        #landscape.print(show_coordinates=True)
        landscape.add_landscape_to_game(static)
        
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
        for obstacle in self.obstacles:
            #if obstacle.rect.x>self.player.rect[0]-res[0]/2 and obstacle.rect.x<self.player.rect[0]+res[0]/2:
            if obstacle.type!="wall":
                
                if obstacle.rect.x>self.player.rect[0]-(RES[0]+BLOCK_SIZE) and obstacle.rect.x<self.player.rect[0]+(RES[0]+BLOCK_SIZE):
                    if obstacle.rect.y>self.player.rect[1]-(RES[1]+BLOCK_SIZE) and obstacle.rect.y<self.player.rect[1]+(RES[1]+BLOCK_SIZE):
                        obstacle.update(self.player, self.obstacles)
            else:
                obstacle.update(self.player, self.obstacles)
        #self.obstacles.update(self.player, self.obstacles)
        
        self.player.update(self.obstacles, self.keys, )
        
        self.update_viewport()

    def draw(self, ):
        
        self.level.fill((82, 84, 84))
        
        for obstacle in self.obstacles:
            if obstacle.type!="wall":
                if obstacle.rect.x>self.player.rect[0]-(RES[0]+BLOCK_SIZE) and obstacle.rect.x<self.player.rect[0]+(RES[0]+BLOCK_SIZE):
                    if obstacle.rect.y>self.player.rect[1]-(RES[1]+BLOCK_SIZE) and obstacle.rect.y<self.player.rect[1]+(RES[1]+BLOCK_SIZE):
                        obstacle.draw(self.level)
            else:
                obstacle.draw(self.level)
        #self.obstacles.draw(self.level)
        #self.level.blit(self.win_text, self.win_rect)
        self.player.draw(self.level)
        self.screen.blit(self.level, (0,0), self.viewport)
    def draw_overlay(self):
        
        self.HealthBar.draw(self.overlay)
        self.StaminaBar.draw(self.overlay)
        show_fps(self.overlay, self.clock.get_fps())
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
            
