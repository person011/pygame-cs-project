import pygame

class Bat(pygame.sprite.Sprite):
    def __init__(self, location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/bat.png')
        
        self.image_left=pygame.transform.flip(self.image, True, False)
        self.main_image=self.image
        self.rect = self.image.get_rect(topleft=location)
        self.rect2=pygame.Rect([self.rect[0]-1, self.rect[1]-1, self.rect[2]+2, self.rect[3]+3])
        self.original_speed=speed
        self.speed = speed
        self.spawn_point=location
        self.position = pygame.math.Vector2((self.rect.x, self.rect.y))
    def update(self, player):
        self.move(player)
        self.hurt_player(player)
    def check_collisions(self, offset, index, obstacles):
        
        unaltered = True
        self.rect[index] += offset[index]
        while pygame.sprite.spritecollideany(self, obstacles):
            self.rect[index] += (1 if offset[index]<0 else -1)
            unaltered = False
        return unaltered
    def move(self, player):
        
        player_position = player.rect.topleft
        direction = player_position - self.position
        velocity = direction.normalize() * self.speed

        self.position += velocity
        self.rect.topleft = self.position
    def hurt_player(self, player):
        #print(player.on_moving,pygame.sprite.collide_rect(self,player))
        
        #print(self.rect2.colliderect(player.rect), 123)
    
        #print(player.rect.topleft)
        if player.on_moving is self or pygame.sprite.collide_rect(self,player) or self.rect2.colliderect(player.rect):
            
            #print(player.check_collisions(offset, axis, obstacles))

            player.hurt_player(15)
    def draw(self, surface):
        
        surface.blit(self.main_image, self.rect)