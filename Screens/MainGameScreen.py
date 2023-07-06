import pygame

from Objects.player import Player
from Objects.bat import Bat
from Objects.block import Block
from Objects.health_bar import HealthBar
from Objects.stamina_bar import StaminaBar
from config import *
from Objects.fps import show_fps
from MainGameScreenConfig import *
from Properties.make_block import make_block
from Properties.round_up_down import *
from Properties.make_and_add_mountains_to_game import make_and_add_mountains_to_game
from Properties.make_and_add_caves_to_game import make_and_add_caves_to_game


class MainGameScreen(object):
    
    def __init__(self):
        
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        #print(self.screen_rect)
        self.clock = pygame.time.Clock()
        self.fps = 60.0
        self.keys = pygame.key.get_pressed()
        self.done = False
        self.player = Player((50,30), 8, (50, 30))
        self.bat=Bat((200, 300), 8)
        self.viewport = self.screen.get_rect()
        #print(self.viewport)
        self.HealthBar=HealthBar(self.player)
        self.StaminaBar=StaminaBar(self.player)
        #3050, 1050
        #10050, 2050
        self.level = pygame.Surface((WALL_WIDTH+50, WALL_HEIGHT+50)).convert()
        #print(self.level)
        self.overlay=pygame.display.get_surface()
        self.level_rect = self.level.get_rect()
        
        #print(self.level_rect)
        #self.win_text,self.win_rect = self.make_text()
        self.all_walls=self.make_walls()
        self.walls=self.all_walls[0]
        self.walls_as_list=self.all_walls[1]
        self.obstacles = self.make_obstacles()
        #self.all_obstacles=[self.walls, self.obstacles]
        self.chunk_location=pygame.Rect([0, 0, BLOCK_SIZE*CHUNK_SIZE, BLOCK_SIZE*CHUNK_SIZE])
        self.all_obstacles=pygame.sprite.Group()
        print("loading done")
        #self.block_size=50
    def make_text(self):
        
        font = pygame.font.Font(None, 100)
        message = str(self.fps)
        fps = font.render(message, True, (100,100,175))
        
    def seperate_to_chunks(self, blocks, chunk_size):
        chunks={}
        list_chunks={}
        for y in range(int(WALL_HEIGHT/50)):
            for x in range(int(WALL_WIDTH/50)):
                #print(x*chunk_size, y*chunk_size)
                chunks[f"chunk {x*chunk_size} {y*chunk_size}"]=[[], x*chunk_size, y*chunk_size]
                list_chunks[f"chunk {x*chunk_size} {y*chunk_size}"]=[[], x*chunk_size, y*chunk_size]
        #count=0
        for i in blocks:
            #print(f"chunk {self.floor_to_chunk_size(i.rect.x/50, chunk_size)} {self.floor_to_chunk_size(i.rect.y/50, chunk_size)}")
            if f"chunk {round_down(round(i.rect.x/50), chunk_size)} {round_down(round(i.rect.y/50), chunk_size)}" in chunks:
                #count+=1
                #print(f"chunk {self.floor_to_chunk_size(int(i.rect.x/50), chunk_size)} {self.floor_to_chunk_size(int(i.rect.y/50), chunk_size)}")
                chunks[f"chunk {round_down(round(i.rect.x/50), chunk_size)} {round_down(round(i.rect.y/50), chunk_size)}"][0].append(i)
                list_chunks[f"chunk {round_down(round(i.rect.x/50), chunk_size)} {round_down(round(i.rect.y/50), chunk_size)}"][0].append(i)
        #print(len(blocks))
        #print(count)
        for i in chunks:
            #print(i, chunks[i][0])
            chunks[i][0]=pygame.sprite.Group(chunks[i][0])
        return chunks, list_chunks
    def block_list_to_dict(self, blocks):
        dict={}
        for i in blocks:
            dict[f"block {i.rect.x} {i.rect.y}"]=i
        return dict
    def make_walls(self):
        walls = [Block((0, WALL_HEIGHT,WALL_WIDTH,1),color=pygame.Color("chocolate"), type="wall"),
                 Block((0,0,1,WALL_HEIGHT),color=pygame.Color("chocolate"), type="wall"),
                 Block((WALL_WIDTH,0,1,WALL_HEIGHT),color=pygame.Color("chocolate"), type="wall"),
                 Block((0,0,WALL_WIDTH,0),color=pygame.Color("chocolate"), type="wall")]
        return (pygame.sprite.Group(walls), walls)
    def make_obstacles(self):
        
            #60
        
        #static= [Block(make_block(i, i%60, block_size), color=pygame.Color("black")) for i in range(1200)]
        static= []
        
        
        for i in range(200):
            for ii in range(80):
                static.append(Block(make_block(i, 100-ii, BLOCK_SIZE)))
        
        moving=[]
        #10, -11, 100, 20
        
        
        make_and_add_mountains_to_game((0, 10, 200, 10), 40, static)
        make_and_add_caves_to_game((0, 10, 200, 100), static, (0.45, 4, 3, 10))
        
        return self.block_list_to_dict(static)

    def update_viewport(self):
        
        
        self.viewport.center = self.player.rect.center
        #print(self.viewport.center)
        self.viewport.clamp_ip(self.level_rect)

    def event_loop(self, available_chunks):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONUP:

                #code below in this if statement should be at the bottom
                pass
            if self.keys[pygame.K_ESCAPE]:
                self.done = True 
            
            elif event.type == pygame.KEYDOWN or event.type == pygame.K_w:
                
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    
                    self.player.jump(available_chunks)
                if event.key==pygame.K_p:
                    self.player.potion(20)
                    #print(1)
                if event.key==pygame.K_0:
                    if self.player.is_invinsible==False:
                        self.player.is_invinsible=True
                    else:
                        self.player.is_invinsible=False
            elif event.type == pygame.KEYUP or event.type == pygame.K_w:
                if event.key == pygame.K_SPACE:
                    self.player.jump_cut()
            elif event.type==self.player.timer_event:
                self.player.hurt_player_timer_event()
            
            #elif event.type == pygame.KEYDOWN:
    def get_available_chunks_but_better(self, obstacles, type="list"):
        if type=="list":
            available_chunks=[]
            
            for i in range(int(round_up(self.viewport.width, BLOCK_SIZE)/BLOCK_SIZE+2)):
                for ii in range(int(round(round_up(self.viewport.height, BLOCK_SIZE)/BLOCK_SIZE)+2)):
                    if f"block {round_down(self.viewport.x, BLOCK_SIZE)+BLOCK_SIZE*i} {round_down(self.viewport.y, BLOCK_SIZE)+BLOCK_SIZE*ii}" in obstacles:
                        available_chunks.append(obstacles[f"block {round_down(self.viewport.x, BLOCK_SIZE)+BLOCK_SIZE*i} {round_down(self.viewport.y, BLOCK_SIZE)+BLOCK_SIZE*ii}"])
        else:
            
            available_chunks=pygame.sprite.Group()
            for i in range(int(round_up(self.viewport.width, BLOCK_SIZE)/BLOCK_SIZE+2)):
                for ii in range(int(round_up(self.viewport.height, BLOCK_SIZE)/BLOCK_SIZE+2)):
                    if f"block {round_down(self.viewport.x, BLOCK_SIZE)+BLOCK_SIZE*i} {round_down(self.viewport.y, BLOCK_SIZE)+BLOCK_SIZE*ii}" in obstacles:
                        available_chunks.add(obstacles[f"block {round_down(self.viewport.x, BLOCK_SIZE)+BLOCK_SIZE*i} {round_down(self.viewport.y,BLOCK_SIZE)+BLOCK_SIZE*ii}"])
        return available_chunks
    def get_available_chunks(self, obstacles, type="list"):
        if type=="list":
            available_chunks=[]
            for chunk in obstacles:
                
                
                if len(obstacles[chunk][0])>0:
                
                #print(chunk_rect.colliderect(point))
                    self.chunk_location.x=obstacles[chunk][1]*BLOCK_SIZE
                    self.chunk_location.y=obstacles[chunk][2]*BLOCK_SIZE
                    
                    if self.viewport.colliderect(self.chunk_location):
                        
                        available_chunks.append(obstacles[chunk][0])
                        
            
            return available_chunks
        else:
            available_chunks=pygame.sprite.Group()
            for chunk in obstacles:
                
                self.chunk_location.x=self.player.rect[0]-RES[0]
                self.chunk_location.y=self.player.rect[1]-RES[1]
                if self.viewport.colliderect(self.chunk_location):
                    available_chunks.add(obstacles[chunk][0])
            return available_chunks
    def update(self, all_obstacles):
        
        self.keys = pygame.key.get_pressed()
        self.player.pre_update(all_obstacles)
        
        all_obstacles.update(self.player, self.walls)
        self.clock.tick(self.fps)
        self.player.update(all_obstacles, self.keys, )
        #self.bat.update(self.player)
        self.update_viewport()
        #t1 = tm.perf_counter() - t0
        #print("Time elapsed: ", t1)
    def draw(self, all_obstacles):
        
        #self.level.fill((82, 84, 84))
        self.level.fill((3, 177, 252))
        
        
        all_obstacles.draw(self.level)
        
        self.walls.draw(self.level)
        self.player.draw(self.level)
        self.bat.draw(self.level)
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
            #t0= tm.perf_counter()
            #print(pygame.mouse.get_pos())
            available_chunks=self.get_available_chunks_but_better(self.obstacles)
        
            
            all_obstacles_list=[]
            for block in available_chunks:
                
                all_obstacles_list.append(block)
            #print(all_obstacles_list)
            
            all_obstacles_list.extend(self.walls_as_list)
            self.all_obstacles.empty()
            self.all_obstacles.add(all_obstacles_list)
            self.event_loop(self.all_obstacles)
            self.update(self.all_obstacles)
            self.draw(self.all_obstacles)
            self.draw_overlay()
            #t1 = tm.perf_counter() - t0
            #print("Time elapsed: ", t1)
            pygame.display.update()
            
            
            self.display_fps()
            
            
