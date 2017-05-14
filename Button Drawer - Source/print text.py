_author_ = 'kang111369748'
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World!')

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (155,0,0)
BRED = (255,0,0)
GREEN = (0,155,0)
BGREEN = (0,255,0)
BLUE = (0,0,155)
BBLUE = (0,0,255)
YELLOW = (155,155,0)

WINDOWWIDTH = 1280
WINDOWHEIGHT = 540
BUTTONGAPSIZE = 40
BUTTONSIZE = 50

XMARGIN = int((WINDOWWIDTH - (2*BUTTONSIZE)-BUTTONGAPSIZE)/2)
YMARGIN = int((WINDOWHEIGHT - (2*BUTTONSIZE)-BUTTONGAPSIZE)/2)

font = pygame.font.Font('freesansbold.ttf', 32)
textSurf = font.render('Hello world!', True, BLACK, WHITE)
textRect = textSurf.get_rect()
textRect.center = (100, 16)

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurf, textRect)
    DISPLAYSURF.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


    DISPLAYSURF.blit()