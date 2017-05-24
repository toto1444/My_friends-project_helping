import pygame, txt.introtxt
from pygame.locals import*

pygame.init()

def dialogue():
    monologue = True
    p = True

    # Main loop
    while monologue:
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    pause = True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        while p:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p = False
                        p2 = True
                        txt.introtxt.line1()
                        pygame.display.update()
                        pygame.display.flip()

        while p2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p2 = False
                        p3 = True
                        txt.introtxt.line2()
                        pygame.display.update()
                        pygame.display.flip()


        while p3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p3 = False
                        p4 = True
                        txt.introtxt.line3()
                        pygame.display.update()
                        pygame.display.flip()

        while p4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p4 = False
                        p5 = True
                        txt.introtxt.line4()
                        pygame.display.update()
                        pygame.display.flip()

        while p5:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p5 = False
                        p6 = True
                        txt.introtxt.line5()
                        pygame.display.update()
                        pygame.display.flip()

        while p6:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p6 = False
                        p7 = True
                        txt.introtxt.line6()
                        pygame.display.update()
                        pygame.display.flip()

        while p7:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p7 = False
                        p8 = True
                        txt.introtxt.line7()
                        pygame.display.update()
                        pygame.display.flip()

        while p8:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p8 = False
                        p9 = True
                        txt.introtxt.line8()
                        pygame.display.update()
                        pygame.display.flip()

        while p9:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p9 = False
                        p10 = True
                        txt.introtxt.line9()
                        pygame.display.update()
                        pygame.display.flip()

        while p10:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p10 = False
                        p11 = True
                        txt.introtxt.line10()
                        pygame.display.update()
                        pygame.display.flip()

        while p11:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p11 = False
                        p12 = True
                        txt.introtxt.line11()
                        pygame.display.update()
                        pygame.display.flip()

        while p12:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p12 = False
                        p13 = True
                        txt.introtxt.line12()
                        pygame.display.update()
                        pygame.display.flip()

        while p13:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p13 = False
                        p14 = True
                        txt.introtxt.line13()
                        pygame.display.update()
                        pygame.display.flip()

        while p14:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p14 = False
                        p15 = True
                        txt.introtxt.line14()
                        pygame.display.update()
                        pygame.display.flip()

        while p15:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        p15 = False
                        monologue = False
                        txt.introtxt.line15()
                        pygame.display.update()
                        pygame.display.flip()