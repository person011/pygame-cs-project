import pygame
from Screens.HomeScreen import HomeScreen
pygame.init()
    #16:9 screen size
from config import res


screen=pygame.display.set_mode(res)
HomeScreen(screen)

