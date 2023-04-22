import pygame
from Screens.HomeScreen import HomeScreen
pygame.init()
    #16:9 screen size
from config import RES


screen=pygame.display.set_mode(RES)
HomeScreen(screen)

