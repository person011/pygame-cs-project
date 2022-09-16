import pygame
from pygame.locals import *

def screen_resize(width, height, event):
    if event.type == QUIT: pygame.display.quit()
    """elif event.type == VIDEORESIZE:
            width, height = event.size
            if width < 600:
                width = 600
            if height < 400:
                height = 400
            screen = pygame.display.set_mode((width,height), HWSURFACE|DOUBLEBUF|RESIZABLE)"""