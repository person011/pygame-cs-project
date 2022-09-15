import pygame
import os

pygame.init()
res = (500, 600)


#screen=pygame.display.set_mode((500, 600))
screen = pygame.display.set_mode(res, pygame.RESIZABLE)

color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('quit', True, color)
text2 = smallfont.render('play', True, color)
while True:
    mouse = pygame.mouse.get_pos()
    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 180 <= mouse[0] <= 180 + 140 and 330 <= mouse[1] <= 330 + 40:
                pygame.quit()
            if 180 <= mouse[0] <= 180 + 140 and 130 <= mouse[1] <= 130 + 40:
                #main()
                pass
    screen.fill((230, 230, 230))
    mouse = pygame.mouse.get_pos()
    if 180 <= mouse[0] <= 180 + 140 and 330 <= mouse[1] <= 330 + 40:
        pygame.draw.rect(screen, color_light, [180, 330, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [180, 330, 140, 40])
    if 180 <= mouse[0] <= 180 + 140 and 130 <= mouse[1] <= 130 + 40:
        pygame.draw.rect(screen, color_light, [180, 130, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [180, 130, 140, 40])
    screen.blit(text, (180 + 50, 330))
    screen.blit(text2, (180 + 50, 130))
    pygame.display.update()

