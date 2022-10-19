import pygame
from Properties._Physics import _Physics

class Player(_Physics, pygame.sprite.Sprite):

    def __init__(self,location,speed):
        
        _Physics.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/square.png')
        #self.image = pygame.Surface((30,55)).convert()
        #self.image.fill(pygame.Color("red"))
        self.image_left=pygame.transform.flip(self.image, True, False)
        self.main_image=self.image
        self.rect = self.image.get_rect(topleft=location)
        self.speed = speed
        #-9, -3
        self.jump_power = -12.0
        self.jump_cut_magnitude = -3.0
        self.on_moving = False
        self.collide_below = False

    def check_keys(self, keys):
        
        self.x_vel = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.main_image=self.image_left
            self.x_vel -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.main_image=self.image
            self.x_vel += self.speed

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
        
        if not self.fall and not self.check_above(obstacles):
            self.y_vel = self.jump_power
            self.fall = True
            self.on_moving = False

    def jump_cut(self):
        
        if self.fall:
            if self.y_vel < self.jump_cut_magnitude:
                self.y_vel = self.jump_cut_magnitude

    def pre_update(self, obstacles):
        
        self.collide_below = self.check_below(obstacles)
        self.check_moving(obstacles)

    def update(self, obstacles, keys):
        
        self.check_keys(keys)
        self.get_position(obstacles)
        self.physics_update()

    def draw(self, surface):
        
        surface.blit(self.main_image, self.rect)
