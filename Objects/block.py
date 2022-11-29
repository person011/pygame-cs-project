import pygame
import time


class Block(pygame.sprite.Sprite):
    """A class representing solid obstacles."""
    def __init__(self, rect, image=None, color=None):
        """The color is an (r,g,b) tuple; rect is a rect-style argument."""
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(rect)
        if image==None:
            self.image = pygame.Surface(self.rect.size).convert()
            self.image.fill(color)
        else:
            self.image=pygame.image.load(image)
        self.type = "normal"
        
class HurtBlock(Block):
    def __init__(self, rect, image=None, color=None):
        
        Block.__init__(self, rect, image, color)
        self.rect2=pygame.Rect([rect[0]-1, rect[1]-1, rect[2]+2, rect[3]+2])
    def update(self, player, obstacles):
        
        obstacles = obstacles.copy()
        obstacles.remove(self)
        now = pygame.time.get_ticks()
        self.hurt_player(now, player)
        

    def hurt_player(self, now, player):
        #print(player.on_moving,pygame.sprite.collide_rect(self,player))
        
        #print(self.rect2.colliderect(player.rect), 123)
    
        #print(player.rect.topleft)
        if player.on_moving is self or pygame.sprite.collide_rect(self,player) or self.rect2.colliderect(player.rect):
            
            #print(player.check_collisions(offset, axis, obstacles))

            player.hurt_player(10)
            

            
                

    