import pygame
import os
from Properties.button import Button
from Properties.size import size_x, size_y
from Properties.screen_resize import screen_resize
from Objects.player import Player
from config import FPS
def MainGameScreen(screen):

    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    height = screen.get_height()
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = smallfont.render('quit', True, color)
    text2 = smallfont.render('play', True, color)
    print(text.get_width())
    character_img=pygame.image.load("Images/square.png")
    #quitButton=Button(380, 630, 180, 90, text)
    #toMainButton=Button(380, 330, 180, 90, text2)
    player=Player(screen, 0, 920, 80, 160, character_img)
    while True:
        pygame.time.delay(FPS)
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():

            screen_resize(ev)
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP:
                    # Start to jump by setting isJump to True.
                    player.isJump = True
            """if quitButton.pressed(ev, mouse)==True:
                pygame.quit()
            if toMainButton.pressed(ev, mouse)==True:
                pass"""
        keys = pygame.key.get_pressed()
        screen.fill((230, 230, 230))
        mouse = pygame.mouse.get_pos()
        
        
        #quitButton.hovering_color(color_dark, color_light, screen, mouse)
        #toMainButton.hovering_color(color_dark, color_light, screen, mouse)
        player.movement(keys)
        player.jump()
        player.draw()
        
        pygame.display.update()