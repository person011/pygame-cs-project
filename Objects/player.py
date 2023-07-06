import pygame
from Properties._Physics import _Physics
from Properties.round_up_down import *
from MainGameScreenConfig import *
from Properties.make_block import *

class Player(_Physics, pygame.sprite.Sprite):

    def __init__(self,location,speed,spawn_point):
        
        _Physics.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/cloak.png')
        #self.image = pygame.Surface((30,55)).convert()
        #self.image.fill(pygame.Color("red"))
        self.image_left=pygame.transform.flip(self.image, True, False)
        self.main_image=self.image
        self.rect = self.image.get_rect(topleft=location)
        self.rect2=pygame.Rect([self.rect[0], self.rect[1], self.rect[2], self.rect[3]])
        self.max_surrounding_size=block_size_to_real_size(2)
        
        
        self.original_speed=speed
        self.speed = speed
        #-9, -3
        self.original_jump_power=-12.7
        self.jump_power = -12.7
        self.jump_cut_magnitude = -3.0
        self.on_moving = False
        self.collide_below = False
        self.main_health=100
        self.health=100
        self.stamina = 100
        self.can_get_hurt=True
        self.spawn_point=spawn_point
        self.start_ticks=pygame.time.get_ticks()
        self.clock = pygame.time.Clock()
        self.timer=2
        self.dt=0
        self.p_presed=0
        self.is_invinsible=False
        self.amount_of_pain=0
        self.timer_event = pygame.USEREVENT+1
        self.original_hurt_player_counter=1
        self.hurt_player_counter=1
        self.hurt_player_has_been_called=False
        self.surrounding_blocks=[]
        pygame.time.set_timer(self.timer_event, 1000)
    def kill_block(self, block_coordinates):
        x, y = pygame.mouse.get_pos()
        print(block_coordinates, 1,round_down(x*BLOCK_SIZE,BLOCK_SIZE), round_down(y*BLOCK_SIZE,BLOCK_SIZE))
        if block_coordinates:
            
            self.surrounding_blocks[block_coordinates].kill()
    def is_block_pressed(self):
        x, y = pygame.mouse.get_pos()
        block_size_x=round_down(x*BLOCK_SIZE,BLOCK_SIZE)
        block_size_y=round_down(y*BLOCK_SIZE,BLOCK_SIZE)
        if (block_size_x, block_size_y) in self.surrounding_blocks:
            return (block_size_x, block_size_y)
        return 
    def get_surrounding_blocks(self, obstacles,type="block object"):
        surrounding_player_rect=pygame.Rect([
            self.rect[0]-self.max_surrounding_size,
            self.rect[1]-self.max_surrounding_size,
            self.rect[2]+2*(self.max_surrounding_size),
            self.rect[3]+2*(self.max_surrounding_size)
            ])
        if type=="block object":
            surrounding_blocks=[]
            for block in obstacles:
                if surrounding_player_rect.colliderect(block.rect):
                    
                        surrounding_blocks.append(block)
        else:
            surrounding_blocks={}
            for block in obstacles:
                if surrounding_player_rect.colliderect(block.rect):
                    
                        surrounding_blocks[(block.rect.x, block.rect.y)]=block   
        
        return surrounding_blocks
    def potion(self, amount):
        
        if self.health<=80:
            self.health+=amount
    
    def hurt_player(self, amount):
        #print(self.can_get_hurt)
        self.hurt_player_has_been_called=True
        if self.is_invinsible==False:
            self.amount_of_pain+=amount
        return self.health-amount
    
    def check_keys(self, keys, obstacles):
        
        self.x_vel = 0
        #self.y_vel=0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.main_image=self.image_left
            self.x_vel -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.main_image=self.image
            self.x_vel += self.speed
        if self.is_invinsible==True:
            
            self.y_vel=0
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                
                if self.check_above(obstacles)==None:
                    self.rect.y-=self.speed
                
                self.y_vel=-self.speed
                
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                
                if len(self.check_below(obstacles))==0:
                    self.rect.y+=self.speed
                self.y_vel=self.speed
            
        if keys[pygame.K_LSHIFT]:
            
            if self.stamina>0:
                self.dashing()
                self.stamina-=1
            else:
                self.speed = self.original_speed
                self.jump_power=self.original_jump_power
        else:
            self.speed = self.original_speed
            self.jump_power=self.original_jump_power
            if self.stamina<100:
                self.stamina+=1
        
            
        
    def dashing(self):
        if self.stamina>0:
            self.speed = 10
            self.jump_power=-17
        

    

    def get_position(self, obstacles):
        
        if not self.fall:
            self.check_falling(obstacles)
        else:
            self.fall = self.check_collisions((0,self.y_vel), 1, obstacles)
        if self.x_vel:
            self.check_collisions((self.x_vel,0), 0, obstacles)

    def check_falling(self, obstacles):
        
        if not self.collide_below:
            self.fall = True
            self.on_moving = False

    def check_moving(self,obstacles):
        
        if not self.fall:
            now_moving = self.on_moving
            any_moving, any_non_moving = [], []
            for collide in self.collide_below:
                if collide.type == "moving":
                    self.on_moving = collide
                    any_moving.append(collide)
                else:
                    any_non_moving.append(collide)
            if not any_moving:
                self.on_moving = False
            elif any_non_moving or now_moving in any_moving:
                self.on_moving = now_moving

    def check_collisions(self, offset, index, obstacles):
        
        unaltered = True
        self.rect[index] += offset[index]
        while pygame.sprite.spritecollideany(self, obstacles):
            self.rect[index] += (1 if offset[index]<0 else -1)
            unaltered = False
        return unaltered

    def check_above(self, obstacles):
        
        self.rect.move_ip(0, -1)
        collide = pygame.sprite.spritecollideany(self, obstacles)
        self.rect.move_ip(0, 1)
        return collide

    def check_below(self, obstacles):
        
        self.rect.move_ip((0,1))
        collide = pygame.sprite.spritecollide(self, obstacles, False)
        self.rect.move_ip((0,-1))
        return collide

    def jump(self, obstacles):
        #for i in obstacles:
        if self.is_invinsible==False:
            if not self.fall and not self.check_above(obstacles):
                self.y_vel = self.jump_power
                self.fall = True
                self.on_moving = False

    def jump_cut(self):
        if self.is_invinsible==False:
            if self.fall:
                if self.y_vel < self.jump_cut_magnitude:
                    self.y_vel = self.jump_cut_magnitude

    def pre_update(self, obstacles):
        self.amount_of_pain=0
        self.hurt_player_has_been_called=False
        self.surrounding_blocks=self.get_surrounding_blocks(obstacles, type="list")

        if self.is_invinsible==False:
            self.collide_below = self.check_below(obstacles)
            self.check_moving(obstacles)
        
    def kill_player(self):
        self.rect.x=self.spawn_point[0]
        self.rect.y=self.spawn_point[1]
        self.health=self.main_health
    def update(self, obstacles, keys):
        
        if self.health<1:
            self.kill_player()
        
        self.check_keys(keys,obstacles)
        self.get_position(obstacles)
        self.get_surrounding_blocks(obstacles)
        #is_block_pressed=self.is_block_pressed()
        #self.kill_block(is_block_pressed)
        if self.is_invinsible==False:
            
            self.physics_update()
        
    def hurt_player_timer_event(self):
        self.hurt_player_counter-=1
        #print(self.amount_of_pain, self.hurt_player_counter)
        if self.hurt_player_counter==0:
            self.hurt_player_counter=self.original_hurt_player_counter
            if self.hurt_player_has_been_called==True:
                self.health-=self.amount_of_pain
                
    def draw(self, surface):
        
        surface.blit(self.main_image, self.rect)
