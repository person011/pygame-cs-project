import pygame
class Collide:
    def __init__(self, x1, y1, width1, height1, x2, y2, width2, height2):
        self.x1=x1
        self.y1=y1
        self.width1=width1
        self.height1=height1
        self.x2=x2
        self.y2=y2
        self.width2=width2
        self.height2=height2
    def collide_right(self):
        main_l=pygame.Rect((self.x1, self.y1), (1, self.height1))
        second_r=pygame.Rect((self.x2+self.width2, self.y2), (-1, self.height2))
        if pygame.Rect.colliderect(main_l, second_r):
            return True
        return False
    def collide_left(self):
        main_r=pygame.Rect((self.x1+self.width1, self.y1), (1, self.height1))
        second_l=pygame.Rect((self.x2, self.y2), (1, self.height2))
        if pygame.Rect.colliderect(main_r, second_l):
            return True
        return False
    def collide_bottom(self):
        main_t=pygame.Rect((self.x1, self.y1), (self.width1, -1))
        second_b=pygame.Rect((self.x2, self.y2+self.height2), (self.width2, -self.height2+1))
        if pygame.Rect.colliderect(main_t, second_b):
            
            return True
        return False
    def collide_top(self):
        main_b=pygame.Rect((self.x1, self.y1+self.height1), (self.width1, 1))
        second_t=pygame.Rect((self.x2, self.y2), (self.width2, -1))
        if pygame.Rect.colliderect(main_b, second_t):
            
            return True
        return False
    