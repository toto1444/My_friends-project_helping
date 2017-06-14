import pygame
#import pygame._view
from pygame.locals import *
from math import *
import time
import random
import os
from cx_Freeze import setup, Executable
import json
import sys
import webbrowser
import txt.introtxt
import pickle # for save game

def GetTime():
   return int(round(time.time() * 1000))


def RandNb(min, max):
   return random.randint(min, max)

def IsTime(cooldown):
   if GetTime() > cooldown:
      return True
   else:
      return False

def Write(window, font, text, coords, colour=(0, 0, 0)):
   window.blit(font.render(str(text), 1, colour), coords)

def DrawProgressbar(window, x, y, width, height, colours=[(0, 0, 0), (0, 155, 0), (55, 155, 55)], progress=0):
   DrawRect(window, (x, y, width, height), colours[2], 0) #Display background
   DrawRect(window, (x+1, y+1, progress*(width-2), height-2), colours[1], 0) #Display progress
   DrawRect(window, (x, y, width, height), colours[0], 1) #Display border


def DrawLine(window, points, colour=(255, 255, 255), thickness=1):
   pygame.draw.lines(window, colour, False, points, thickness)



def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, answer):
  pygame.font.init()
  current_string = []
  display_box(screen, answer + ": " + str.join("",current_string))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, answer + ": " + str.join("",current_string))
  return str.join("",current_string)

def get():
  st=ask(screen, "Answer")
  return int(st)

def text(textlist,i):
    p=0
    screen.blit(pygame.transform.scale(image[i], (scale_x, scale_y)), (0, 0))
    commontext(textlist[p])
    p += 1
    while p < len(textlist):
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_SPACE:
                screen.blit(pygame.transform.scale(image[i], (scale_x, scale_y)), (0, 0))
                effect.play()
                commontext(textlist[p])
                p += 1
        pygame.display.update()

def commontext(b):
    screen.blit(window, (0, 520))
    if len(b)==1:
        screen.blit(b[0], (20, 540))
    else:
        screen.blit(b[0], (20, 540))
        screen.blit(b[1], (20, 580))

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, textColor)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def getRect(pic):
    picR = pic.get_rect()
    return picR

def quitGame():
    pygame.quit()
    sys.exit()

def button(pic, x, y):
    picR = getRect(pic)
    picR.x=x
    picR.y=y
    screen.blit(pic, picR)
    return picR

def unpause():
    global pause
    pause = False

def paused():
    screen.blit(settingsMenu, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        button(startButton, 150, 450, getRect(startButton).width, getRect(startButton).height, unpause)
        pygame.display.update()
        clock.tick(FPS)

def inventory():
    while True:
        screen.blit(inventoryMenu, (0, 0))
        br = button(arrowLeft, 1150, 60)
        for startScreen in pygame.event.get():
            if startScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
            if startScreen.type == MOUSEBUTTONDOWN:
                x,y = startScreen.pos
                if br.collidepoint(x,y):
                    return
        pygame.display.update()
        clock.tick(FPS)
