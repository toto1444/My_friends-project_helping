import pygame, txt.introtxt
from pygame.locals import*

pygame.init()

def dialogue():
    for event in pygame.event.get():
        txt.introtxt.line1()
        pygame.display.update()
        pygame.display.flip()
        if event.type == pygame.key.get_pressed:
            if event.key == K_SPACE:
                txt.introtxt.line2()
                pygame.display.update()
                pygame.display.flip()
                if event.type == pygame.key.get_pressed:
                    if event.key == K_SPACE:
                        txt.introtxt.line3()
                        pygame.display.update()
                        pygame.display.flip()
                        if event.type == pygame.key.get_pressed:
                            if event.key == K_SPACE:
                                txt.introtxt.line4()
                                pygame.display.update()
                                pygame.display.flip()
                                if event.type == pygame.key.get_pressed:
                                    if event.key == K_SPACE:
                                        txt.introtxt.line5()
                                        pygame.display.update()
                                        pygame.display.flip()
                                        if event.type == pygame.key.get_pressed:
                                            if event.key == K_SPACE:
                                                txt.introtxt.line6()
                                                pygame.display.update()
                                                pygame.display.flip()
                                                if event.type == pygame.key.get_pressed:
                                                    if event.key == K_SPACE:
                                                        txt.introtxt.line7()
                                                        pygame.display.update()
                                                        pygame.display.flip()
                                                        if event.type == pygame.key.get_pressed:
                                                            if event.key == K_SPACE:
                                                                txt.introtxt.line8()
                                                                pygame.display.update()
                                                                pygame.display.flip()
                                                                if event.type == pygame.key.get_pressed:
                                                                    if event.key == K_SPACE:
                                                                        txt.introtxt.line9()
                                                                        pygame.display.update()
                                                                        pygame.display.flip()
                                                                        if event.type == pygame.key.get_pressed:
                                                                            if event.key == K_SPACE:
                                                                                txt.introtxt.line10()
                                                                                pygame.display.update()
                                                                                pygame.display.flip()
                                                                                if event.type == pygame.key.get_pressed:
                                                                                    if event.key == K_SPACE:
                                                                                        txt.introtxt.line11()
                                                                                        pygame.display.update()
                                                                                        pygame.display.flip()
                                                                                        if event.type == pygame.key.get_pressed:
                                                                                            if event.key == K_SPACE:
                                                                                                txt.introtxt.line12()
                                                                                                pygame.display.update()
                                                                                                pygame.display.flip()
                                                                                                if event.type == pygame.key.get_pressed:
                                                                                                    if event.key == K_SPACE:
                                                                                                        txt.introtxt.line13()
                                                                                                        pygame.display.update()
                                                                                                        pygame.display.flip()
                                                                                                        if event.type == pygame.key.get_pressed:
                                                                                                            if event.key == K_SPACE:
                                                                                                                txt.introtxt.line14()
                                                                                                                pygame.display.update()
                                                                                                                pygame.display.flip()
                                                                                                                if event.type == pygame.key.get_pressed:
                                                                                                                    if event.key == K_SPACE:
                                                                                                                        txt.introtxt.line15()
                                                                                                                        pygame.display.update()
                                                                                                                        pygame.display.flip()


