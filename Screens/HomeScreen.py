import pygame
from Properties.button import Button
from Properties.screen_resize import screen_resize
from Screens.MainGameScreen import MainGameScreen

def HomeScreen(screen):

    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    height = screen.get_height()
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = smallfont.render('quit', True, color)
    text2 = smallfont.render('play', True, color)
    #print(text.get_width())
    quitButton=Button(380, 630, 180, 90, text)
    toMainButton=Button(380, 330, 180, 90, text2)
    while True:
        
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():

            screen_resize(ev)
            
            if quitButton.pressed(ev, mouse)==True:
                pygame.quit()
            if toMainButton.pressed(ev, mouse)==True:
                MainGameScreen().main_loop()
        screen.fill((230, 230, 230))
        mouse = pygame.mouse.get_pos()
        
        
        quitButton.hovering_color(color_dark, color_light, screen, mouse)
        toMainButton.hovering_color(color_dark, color_light, screen, mouse)
            
        
        pygame.display.update()