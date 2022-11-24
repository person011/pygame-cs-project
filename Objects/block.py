import pygame

class Block(pygame.sprite.Sprite):
    """A class representing solid obstacles."""
    def __init__(self, color, rect):
        """The color is an (r,g,b) tuple; rect is a rect-style argument."""
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.image.fill(color)
        self.type = "normal"
class MovingBlock(Block):
    
    def __init__(self, color, rect, end, axis, delay=500, speed=2, start=None):
        
        Block.__init__(self, color, rect)
        self.start = self.rect[axis]
        if start:
            self.rect[axis] = start
        self.axis = axis
        self.end = end
        self.timer = 0.0
        self.delay = delay
        self.speed = speed
        self.waiting = False
        self.type = "moving"

    def update(self, player, obstacles):
        
        obstacles = obstacles.copy()
        obstacles.remove(self)
        now = pygame.time.get_ticks()
        if not self.waiting:
            speed = self.speed
            start_passed = self.start >= self.rect[self.axis]+speed
            end_passed = self.end <= self.rect[self.axis]+speed
            if start_passed or end_passed:
                if start_passed:
                    speed = self.start-self.rect[self.axis]
                else:
                    speed = self.end-self.rect[self.axis]
                self.change_direction(now)
            self.rect[self.axis] += speed
            self.move_player(now, player, obstacles, speed)
        elif now-self.timer > self.delay:
            self.waiting = False

    def move_player(self, now, player, obstacles, speed):
        #print(player.on_moving is self, player)
        if player.on_moving is self or pygame.sprite.collide_rect(self,player):
            
            axis = self.axis
            offset = (speed, speed)
            player.check_collisions(offset, axis, obstacles)
            player.hurt_player(100)
            if pygame.sprite.collide_rect(self, player):
                
                if self.speed > 0:
                    self.rect[axis] = player.rect[axis]-self.rect.size[axis]
                else:
                    self.rect[axis] = player.rect[axis]+player.rect.size[axis]
                self.change_direction(now)

    def change_direction(self, now):
        
        self.waiting = True
        self.timer = now
        self.speed *= -1
