import random, sys, time, pygame
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FLASHSPEED = 500 #milliseconds
FLASHDELAY = 200
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (155,0,0)
BRED = (255,0,0)
GREEN = (0,155,0)
BGREEN = (0,255,0)
BLUE = (0,0,155)
BBLUE = (0,0,255)
YELLOW = (155,155,0)

bgColor = WHITE

XMARGIN = int((WINDOWWIDTH - (2*BUTTONSIZE)-BUTTONGAPSIZE)/2)
YMARGIN = int((WINDOWHEIGHT - (2*BUTTONSIZE)-BUTTONGAPSIZE)/2)

YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT = pygame.Rect(XMARGIN+BUTTONSIZE+BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONGAPSIZE)
REDRECT = pygame.Rect(XMARGIN, YMARGIN+BUTTONSIZE+BUTTONGAPSIZE, BUTTONSIZE, BUTTONGAPSIZE)
GREENRECT = pygame.Rect(XMARGIN+BUTTONSIZE+BUTTONGAPSIZE, YMARGIN+BUTTONSIZE+BUTTONGAPSIZE, BUTTONSIZE, BUTTONGAPSIZE)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Simulate')

    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)

    infoSurf = BASICFONT.render('Match the pattern by cliking on the button or using the Q, W, A, S keys.', 1, BLACK)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10, WINDOWHEIGHT - 25)

    while True:
        clickedButton = None
        DISPLAYSURF.fill(bgColor)
        drawButtons()

        scoreSurf = BASICFONT.render('score: ', + str(score), 1, YELLOW)