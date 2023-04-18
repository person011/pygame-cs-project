import pygame

def show_fps(screen, fps):
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = smallfont.render("fps: "+str(round(fps, 2)), True, (255, 255, 255))
        
    screen.blit(text, (5,16))