#-*- encoding : utf-8 -*-
from graphics import *
import pygame
from pygame.locals import *
import subprocess

Window_Width, Window_Height = 600, 450
win = GraphWin('UJ Simulator', Window_Width, Window_Height)
win.setCoords(0,0,3,8)
text = ''

FPS = 30
SCREENWIDTH  = 1280
SCREENHEIGHT = 720
# amount by which base can maximum shift to left
PIPEGAPSIZE  = 100 # gap between upper and lower part of pipe
BASEY        = SCREENHEIGHT * 0.79
# image, sound and hitmask  dicts
IMAGES, SOUNDS, HITMASKS = {}, {}, {}


#The first function for the Start setup
def main():
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('UJ SIMULATOR')

    Start=Text(Point(1.5, 3), 'START')
    Start.setSize(30)
    Start.draw(win)
    start = Rectangle(Point(0.75,2.5), Point(2.25,3.5)).draw(win)

    Setting=Text(Point(1.5, 1.25), 'SETTING')
    Setting.setSize(30)
    Setting.draw(win)
    setting = Rectangle(Point(0.75,0.75), Point(2.25, 1.75)).draw(win)

    return start, setting



#This may not be necessary.
def gameStart():

    ourScreen = pygame.display.set_mode((600, 450))
    ourScreen.fill((255, 255, 255))
    pygame.display.set_caption('UJ Simulator')
    finish = False

    pygame.mouse.set_cursor(*pygame.cursors.arrow)

    font = pygame.font.Font(None, 80)
    text_1 = 'Gaming Start'

    size_1 = font.size(text_1)
    ren_1 = font.render(text_1, 0, (250, 240, 230), (5, 5, 5))
    ourScreen.blit(ren_1, (10, 10))

    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

            pygame.display.flip()

#This is a fuction for the setting slide that pop out after clicking SETTING button.
def gameSetting():
    ourScreen = pygame.display.set_mode((600, 450))
    ourScreen.fill((0, 0, 0))
    pygame.display.set_caption('UJ Simulator')
    finish = False

    pygame.mouse.set_cursor(*pygame.cursors.arrow)

    font = pygame.font.Font(None, 80)
    text_1 = 'Settings'

    size_1 = font.size(text_1)
    ren_1 = font.render(text_1, 0, (250, 250, 250), (5, 5, 5))
    ourScreen.blit(ren_1, (10, 10))

    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

            pygame.display.flip()
    pygame.quit()


#Function for a button. Basically, This sets boundaries that we can click on.
def button(point, rectangle):
    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()


#This function is the first slide of the narration.
#This is the part where I'm struggling.
#I tired to make if statements inside this function, so I can make another button, but it doesn't work.
def START():
    Window_for_narration = Rectangle(Point(0,0), Point(3,8))
    Window_for_narration.setFill('white')
    Window_for_narration.setOutline('white')
    Window_for_narration.draw(win)

    Narration = Text(Point(0.33,7.5), 'oneday')
    Narration.setSize(30)
    Narration.draw(win)


    Next_button = Rectangle(Point(2.4, 1.2), Point(2.9, 0.4))
    Next_button.setWidth(3)
    Next_button.setOutline('black')
    Next_button.draw(win)

    Next = Text(Point(2.65, 0.8), 'Next')
    Next.setSize(20)
    Next.draw(win)

    def Narration_1():
        Window_for_narration_1 = Rectangle(Point(0, 0), Point(3, 8))
        Window_for_narration_1.setOutline('white')
        Window_for_narration_1.setFill('white')
        Window_for_narration_1.draw(win)

    if button(win.getMouse(), Next_button):
        Narration_1()



#It's not working right now. I didn't call this function yet.
def bgMusic():
    pygame.mixer.init()
    bg = pygame.mixer.Sound('audio/bgmusic.wav')
    bg.play()


#This is a defined function for a setting.
def SETTING():
    pygame.init()
    gameSetting()
    pygame.quit()


#I called main() function here.
start, setting = main()

#This is a loop for the buttons.
while True:
    clickPoint = win.getMouse()

    if clickPoint is None:  # so we can substitute checkMouse() for getMouse()
        text.setText("")
    elif button(clickPoint, start):
        START()
    elif button(clickPoint, setting):
        SETTING()