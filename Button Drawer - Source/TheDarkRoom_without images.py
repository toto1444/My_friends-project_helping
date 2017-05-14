_author_ = 'kang111369748'

import pygame
from pygame.locals import*

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

YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT = pygame.Rect(XMARGIN+BUTTONSIZE+BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONGAPSIZE)
REDRECT = pygame.Rect(XMARGIN, YMARGIN+BUTTONSIZE+BUTTONGAPSIZE, BUTTONSIZE, BUTTONGAPSIZE)
GREENRECT = pygame.Rect(XMARGIN+BUTTONSIZE+BUTTONGAPSIZE, YMARGIN+BUTTONSIZE+BUTTONGAPSIZE, BUTTONSIZE, BUTTONGAPSIZE)

pad_width = 1280
pad_height = 540
pygame.init()
Display = pygame.display.set_mode((1280, 540))

def Menu(x, y):
    global display, menuImage, menutext
    display.blit(menuImage, (x, y))

def Titletext():
    global display
    font = pygame.font.Font('freesansbold.ttf', 32)
    textSurf = font.render('The Dark Room!', True, BLACK, WHITE)
    textRect = textSurf.get_rect()
    textRect.center = (100, 16)
    display.blit(textSurf, textRect)

def rungame():
    global display
    menu_x = 0
    GameCrash = False
    while not GameCrash:
        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                GameCrash = True
        display.fill(WHITE)

        pygame.draw.rect(display, RED, (150, 550, 100, 50))


        Menu(menu_x, 0)
        pygame.display.update()
    pygame.quit()
#def MenuBack():
#    menuImage = pygame.image.load('files/titlepage.png')
#    menuImage = pygame.transform.scale(menuImage, (1280, 540))
#    menuImage = pygame.Surface.convert_alpha(menuImage, (1280, 540))
#    return menuImage

def initgame():
    global display, menuImage
    pygame.init()
    display = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('The Dark Room')
#    MenuBack()
    Titletext()
    rungame()
initgame()