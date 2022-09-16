import pygame
from Properties.size import size_x, size_y

class Button:
    def __init__(self, x, y, width, height, text):
        self.height=size_y(height)
        self.width=size_x(width)
        self.x=size_x(x)
        self.y=size_y(y)
        self.text=text
    def pressed(self, ev, mouse):
        
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height:
                return True
        return False
    def hover(self, mouse):
        
        if self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height:
            return True
        return False
    def draw_rt(self, color, screen):
        pygame.draw.rect(screen, color, [self.x, self.y, self.width, self.height])
        screen.blit(self.text, (self.x +(self.width/2-self.text.get_width()/2), self.y+(self.height/2-self.text.get_height()/2)))
    def hovering_color(self, color1, color2, screen, mouse):
        if self.hover(mouse)==True:
            self.draw_rt(color2, screen)
        else:
            self.draw_rt(color1, screen)