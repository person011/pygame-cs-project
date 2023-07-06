from config import RES
import pygame
from Screens.HomeScreen import HomeScreen

pygame.init()
screen=pygame.display.set_mode(RES)
HomeScreen(screen)