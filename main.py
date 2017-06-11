import pygame, txt.introtxt, time, sys
from pygame.locals import*

pygame.init()

size = (1280,720)
white = (255, 255, 255)
black = (0, 0, 0)
scale_x = 1280
scale_y = 720


clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
window = pygame.image.load("txt/txtwin.png")
menu = pygame.image.load("img/menu.png")
settingsMenu = pygame.image.load("img/settingsMenu.png")
achievementMenu = pygame.image.load("img/achievementMenu.png")
leaderboardMenu = pygame.image.load("img/leaderboardMenu.png")
galleryMenu = pygame.image.load("img/galleryMenu.png")
startMenu = pygame.image.load("img/startSample.png")
inventoryButton = pygame.image.load("img/inventoryButton.png")
settingsInGameButton = pygame.image.load("img/settingsButton.png")
inventoryMenu = pygame.image.load("img/inventory.png")
arrowLeft = pygame.image.load("img/arrow.png")
favicon = pygame.image.load("img/icon.png")
pygame.display.set_icon(favicon)

n0 = pygame.image.load("img/0.png")
n0 = pygame.transform.scale(n0, (40, 40))
n1 = pygame.image.load("img/1.png")
n1 = pygame.transform.scale(n1, (40, 40))
n2 = pygame.image.load("img/2.png")
n2 = pygame.transform.scale(n2, (40, 40))
n3 = pygame.image.load("img/3.png")
n3 = pygame.transform.scale(n3, (40, 40))
n4 = pygame.image.load("img/4.png")
n4 = pygame.transform.scale(n4, (40, 40))
n5 = pygame.image.load("img/5.png")
n5 = pygame.transform.scale(n5, (40, 40))
n6 = pygame.image.load("img/6.png")
n6 = pygame.transform.scale(n6, (40, 40))
n7 = pygame.image.load("img/7.png")
n7 = pygame.transform.scale(n7, (40, 40))
n8 = pygame.image.load("img/8.png")
n8 = pygame.transform.scale(n8, (40, 40))
n9 = pygame.image.load("img/9.png")
n9= pygame.transform.scale(n9, (40, 40))
n14 = pygame.image.load("img/14.png")
n14 = pygame.transform.scale(n14, (40, 40))
n25 = pygame.image.load("img/25.png")
n25 = pygame.transform.scale(n25, (40, 40))
n36 = pygame.image.load("img/36.png")
n36 = pygame.transform.scale(n36, (40, 40))
n47 = pygame.image.load("img/47.png")
n47 = pygame.transform.scale(n47, (40, 40))
n58 = pygame.image.load("img/58.png")
n58 = pygame.transform.scale(n58, (40, 40))
n63 = pygame.image.load("img/63.png")
n63 = pygame.transform.scale(n63, (40, 40))
n69 = pygame.image.load("img/69.png")
n69 = pygame.transform.scale(n69, (40, 40))
n410 = pygame.image.load("img/410.png")
n410 = pygame.transform.scale(n410, (40, 40))
aA = pygame.image.load("img/A.png")
aA = pygame.transform.scale(aA, (40, 40))
aB = pygame.image.load("img/B.png")
aB = pygame.transform.scale(aB, (40, 40))
aC = pygame.image.load("img/C.png")
aC = pygame.transform.scale(aC, (40, 40))
aD = pygame.image.load("img/D.png")
aD = pygame.transform.scale(aD, (40, 40))
aE = pygame.image.load("img/E.png")
aE = pygame.transform.scale(aE, (40, 40))
aF = pygame.image.load("img/F.png")
aF = pygame.transform.scale(aF, (40, 40))
aN = pygame.image.load("img/n.png")
aN = pygame.transform.scale(aN, (40, 40))

startButton = pygame.image.load("img/start.png")
leaderboardButton = pygame.image.load("img/leaderboard.png")
achievementButton = pygame.image.load("img/achievement.png")
settingsButton = pygame.image.load("img/settings.png")
galleryButton = pygame.image.load("img/gallery.png")
exitButton = pygame.image.load("img/exit.png")
backButton = pygame.image.load("img/back.png")
quizButton = pygame.image.load("img/test_black.png")


leftside = pygame.image.load("img/leftside.png")
rightside = pygame.image.load("img/rightside.png")
quiz1_1img = pygame.image.load("img/quiz1.png")
quiz1_2img = pygame.image.load("img/quiz2.png")
quiz1_3img = pygame.image.load("img/quiz3.png")
quiz1_4img = pygame.image.load("img/quiz1_4.png")
quiz1_5img = pygame.image.load("img/quiz1_5.png")
quiz1_6img = pygame.image.load("img/quiz1_6.png")
quiz1_7img = pygame.image.load("img/quiz1_7.png")
quiz1_8img = pygame.image.load("img/quiz1_8.png")
quiz1_9img = pygame.image.load("img/quiz1_9.png")
quiz1_10img = pygame.image.load("img/quiz1_10.png")
quiz1_11img = pygame.image.load("img/quiz1_11.png")
quiz1_12img = pygame.image.load("img/quiz1_12.png")

dialogue = pygame.image.load("img/dialogue.png")
startdiag = pygame.image.load("img/startdiag.png")
startdiag = pygame.image.load("img/startdiag.png")
chap1_1 = pygame.image.load("img/chap1_1.png")
chap1_1 = pygame.transform.scale(chap1_1, (1280, 720))
chap1_2 = pygame.image.load("img/chap1_2.png")
chap1_2 = pygame.transform.scale(chap1_2, (1280, 720))
chap1_3 = pygame.image.load("img/chap1_3.png")
chap1_3 = pygame.transform.scale(chap1_3, (1280, 720))
chap2_1 = pygame.image.load("img/chap2_1.png")
chap2_2 = pygame.image.load("img/chap2_2.png")
chap2_3 = pygame.image.load("img/chap2_3.png")
chap3_1 = pygame.image.load("img/chap3_1.png")
chap3_2 = pygame.image.load("img/chap3_2.png")
chap3_3 = pygame.image.load("img/chap3_3.png")
endscene = pygame.image.load("img/endscene.png")
image1 = [chap1_1,chap1_2,chap1_3]
image2 = [chap2_1,chap2_2,chap2_3]
image3 = [chap3_1,chap3_2,chap3_3]

pygame.mixer.music.load('sounds/Menu.wav')
effect = pygame.mixer.Sound('sounds/Text.wav')
mumble = pygame.mixer.Sound('sounds/mumble2.wav')
startdiag = pygame.image.load("img/startdiag.png")
dialogue1 = pygame.image.load('img/dialogue1.png')
dialogue2 = pygame.image.load('img/dialogue2.png')


font = pygame.font.SysFont(None, 48)
textColor = (0, 0, 0)
backgroundColor = (255, 255, 255)

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
    fontobject = pygame.font.Font(None,18)
    pygame.draw.rect(screen, (0,0,0), ((screen.get_width() / 2) - 100,(screen.get_height() / 2) - 10,200,20), 0)
    pygame.draw.rect(screen, (255,255,255), ((screen.get_width() / 2) - 102, (screen.get_height() / 2) - 12, 204,24), 1)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255,255,255)),((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
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
        clock.tick(60)

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
        clock.tick(60)

def settingsInGame():
    settingsInGame = True
    while settingsInGame:
        screen.blit(settingsMenu, (0, 0))
        for settingsScreen in pygame.event.get():
            if settingsScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
            button(backButton, 1050, 50, getRect(backButton).width, getRect(backButton).height, start)
            button(exitButton, 1050, 110, getRect(exitButton).width, getRect(exitButton).height, gameMenu)
            pygame.display.update()
            clock.tick(60)

def start():
    pygame.mixer.music.stop()
    p = 0
    screen.fill(white)
    screen.blit(startdiag, (0, 0))
    event = True;
    event1 = False;
    event2 = False;
    b2 = button(inventoryButton, 10, 3)
    b3 = button(settingsInGameButton, 10, 120)
    while event:
        for startScreen in pygame.event.get():
            if startScreen.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if startScreen.type == pygame.KEYDOWN and p<len(txt.introtxt.a):
                screen.fill(white)
                screen.blit(startdiag, (0, 0))
                button(inventoryButton, 10, 3)
                button(settingsInGameButton, 10, 120)
                if startScreen.key == K_SPACE and startScreen.key == MOUSEBUTTONDOWN:
                    if p>=6 and p<=9 and p%2==0:
                        pygame.mixer.music.load('sounds/mumble1.wav')
                        pygame.mixer.music.play(1)
                        screen.blit(dialogue1, (0, 0))
                    elif p>=6 and p<=9 and p%2==1:
                        pygame.mixer.music.load('sounds/mumble2.wav')
                        pygame.mixer.music.play(1)
                        screen.blit(dialogue2, (0, 0))
                    effect.play()
                    commontext(txt.introtxt.a[p])
                    p = p+1
            if startScreen.type == MOUSEBUTTONDOWN:
                x,y = startScreen.pos
                if(b2.collidepoint(x,y)):
                    inventory()
                    screen.fill(white)
                    screen.blit(startdiag, (0, 0))
                    button(inventoryButton, 10, 3)
                    button(settingsInGameButton, 10, 120)
                    commontext(txt.introtxt.a[p])
                if(b3.collidepoint(x,y)):
                    settings()
                    screen.fill(white)
                    screen.blit(startdiag, (0, 0))
                    button(inventoryButton, 10, 3)
                    button(settingsInGameButton, 10, 120)
                    commontext(txt.introtxt.a[p])
        if p == len(txt.introtxt.a):
            event=False
            event1=True
        pygame.display.update()
        clock.tick(60)
    i=0
    #좌표지정 해야됨
    books = pygame.Rect(700,60,200,200)
    bed = pygame.Rect(600,500,800,150)
    #정확한 좌표 지정 요망
    computer = pygame.Rect(570,400,120,80)
    cloth = pygame.Rect(230,0,70,400)
    doorlock = pygame.Rect(580,280,10,80)

    screen.blit(pygame.transform.scale(image[i], (scale_x, scale_y)), (0, 0))
    b1 = button(leftside, 80, 360)
    b4 = button(rightside, 1120, 360)
    solvedquizzes = 0
    while event1:
        for startScreen in pygame.event.get():
            if startScreen.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if startScreen.type == MOUSEBUTTONDOWN:
                x,y = startScreen.pos
                if(b1.collidepoint(x,y)):
                    if(i==0):
                        i=2
                        screen.blit(pygame.transform.scale(image1[i], (scale_x, scale_y)), (0, 0))
                    else:
                        i-=1
                        screen.blit(pygame.transform.scale(image1[i], (scale_x, scale_y)), (0, 0))
                if(b4.collidepoint(x,y)):
                    if(i==2):
                        i=0
                        screen.blit(pygame.transform.scale(image1[i], (scale_x, scale_y)), (0, 0))
                    else:
                        i+=1
                        screen.blit(pygame.transform.scale(image1[i], (scale_x, scale_y)), (0, 0))
                if(books.collidepoint(x,y)) and i == 0:
                    text(txt.introtxt.b,i)
                if(bed.collidepoint(x, y)) and i == 1:
                    text(txt.introtxt.c,i)
                    if quiz(quiz1_1img, 64):
                        solvedquizzes += 1
                #추가퀴즈 줘야됨
                if(computer.collidepoint(x,y)) and i == 0:
                    text(txt.introtxt.d.i)
                    if quiz(quiz1_2img, ):
                        solvedquizzes += 1
                if(cloth.collidepoint(x,y)) and i == 2:
                    text(txt.introtxt.e.i)
                    if quiz(quiz1_3img, ):
                        solvedquizzes += 1
                if(doorlock.collidepoint(x,y)) and i ==2:
                    text(txt.introtxt.f.i)
                    if quiz(quiz1_4img, 410):
                        solvedquizzes += 1
                if solvedquizzes >= 4:
                    stage2()





        screen.blit(pygame.transform.scale(image[i], (scale_x, scale_y)), (0, 0))
        screen.blit(leftside, (80, 360))
        screen.blit(rightside, (1120, 360))
        button(inventoryButton, 10, 3)
        button(settingsInGameButton, 10, 120)
        pygame.display.update()
        clock.tick(60)

def stage2():
    screen.fill(white)
    screen.blit(startdiag, (0, 0))
    event = True;
    event1 = False;
    event2 = False;
    b2 = button(inventoryButton, 10, 3)
    b3 = button(settingsInGameButton, 10, 120)

    i=0
    #좌표지정 해야됨
    books = pygame.Rect(700,60,200,200)
    bed = pygame.Rect(600,500,800,150)
    #정확한 좌표 지정 요망
    computer = pygame.Rect(570,400,120,80)
    cloth = pygame.Rect(230,0,70,400)
    doorlock = pygame.Rect(580,280,10,80)

    screen.blit(pygame.transform.scale(image[i], (scale_x, scale_y)), (0, 0))
    b1 = button(leftside, 80, 360)
    b4 = button(rightside, 1120, 360)
    solvedquizzes = 0
    while event2:
        for startScreen in pygame.event.get():
            if startScreen.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if startScreen.type == MOUSEBUTTONDOWN:
                x,y = startScreen.pos
                if(b1.collidepoint(x,y)):
                    if(i==0):
                        i=2
                        screen.blit(pygame.transform.scale(image2[i], (scale_x, scale_y)), (0, 0))
                    else:
                        i-=1
                        screen.blit(pygame.transform.scale(image2[i], (scale_x, scale_y)), (0, 0))
                if(b4.collidepoint(x,y)):
                    if(i==2):
                        i=0
                        screen.blit(pygame.transform.scale(image2[i], (scale_x, scale_y)), (0, 0))
                    else:
                        i+=1
                        screen.blit(pygame.transform.scale(image2[i], (scale_x, scale_y)), (0, 0))
                if(books.collidepoint(x,y)) and i == 0:
                    text(txt.introtxt.b,i)
                if(bed.collidepoint(x, y)) and i == 1:
                    text(txt.introtxt.c,i)
                    if quiz(quiz1_5img, a):
                        solvedquizzes += 1
                #추가퀴즈 줘야됨
                if(bed.collidepoint(x,y)):
                    text(txt.introtxt.d.i)
                    if quiz(quiz1_6img, ):
                        solvedquizzes += 1
                if(cloth.collidepoint(x,y)) and i == 2:
                    text(txt.introtxt.e.i)
                    if quiz(quiz1_7img, ):
                        solvedquizzes += 1
                if(doorlock.collidepoint(x,y)) and i ==2:
                    text(txt.introtxt.f.i)
                    if quiz(quiz1_8img, 410):
                        solvedquizzes += 1
                if solvedquizzes >= 4
                    stage3()




        screen.blit(pygame.transform.scale(image[i], (scale_x, scale_y)), (0, 0))
        screen.blit(leftside, (80, 360))
        screen.blit(rightside, (1120, 360))
        button(inventoryButton, 10, 3)
        button(settingsInGameButton, 10, 120)
        pygame.display.update()
        clock.tick(60)

def stage3():
    screen.fill(white)
    screen.blit(startdiag, (0, 0))
    event = True;
    event1 = False;
    event2 = False;
    b2 = button(inventoryButton, 10, 3)
    b3 = button(settingsInGameButton, 10, 120)

    i=0
    #좌표지정 해야됨
    books = pygame.Rect(700,60,200,200)
    bed = pygame.Rect(600,500,800,150)
    #정확한 좌표 지정 요망
    computer = pygame.Rect(570,400,120,80)
    cloth = pygame.Rect(230,0,70,400)
    doorlock = pygame.Rect(580,280,10,80)

    screen.blit(pygame.transform.scale(image[i], (scale_x, scale_y)), (0, 0))
    b1 = button(leftside, 80, 360)
    b4 = button(rightside, 1120, 360)
    solvedquizzes = 0
    while event2:
        for startScreen in pygame.event.get():
            if startScreen.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if startScreen.type == MOUSEBUTTONDOWN:
                x,y = startScreen.pos
                if(b1.collidepoint(x,y)):
                    if(i==0):
                        i=2
                        screen.blit(pygame.transform.scale(image3[i], (scale_x, scale_y)), (0, 0))
                    else:
                        i-=1
                        screen.blit(pygame.transform.scale(image3[i], (scale_x, scale_y)), (0, 0))
                if(b4.collidepoint(x,y)):
                    if(i==2):
                        i=0
                        screen.blit(pygame.transform.scale(image3[i], (scale_x, scale_y)), (0, 0))
                    else:
                        i+=1
                        screen.blit(pygame.transform.scale(image3[i], (scale_x, scale_y)), (0, 0))
                if(books.collidepoint(x,y)) and i == 0:
                    text(txt.introtxt.b,i)
                if(bed.collidepoint(x, y)) and i == 1:
                    text(txt.introtxt.c,i)
                    if quiz(quiz1_9img, 64):
                        solvedquizzes += 1
                #추가퀴즈 줘야됨
                if(bed.collidepoint(x,y)):
                    text(txt.introtxt.d.i)
                    if quiz(quiz1_10img, ):
                        solvedquizzes += 1
                if(cloth.collidepoint(x,y)) and i == 2:
                    text(txt.introtxt.e.i)
                    if quiz(quiz1_11img, ):
                        solvedquizzes += 1
                if(doorlock.collidepoint(x,y)) and i ==2:
                    text(txt.introtxt.f.i)
                    if quiz(quiz1_12img, 410):
                        solvedquizzes += 1
                if solvedquizzes >= 4:
                    endscene()

        screen.blit(pygame.transform.scale(image[i], (scale_x, scale_y)), (0, 0))
        screen.blit(leftside, (80, 360))
        screen.blit(rightside, (1120, 360))
        button(inventoryButton, 10, 3)
        button(settingsInGameButton, 10, 120)
        pygame.display.update()
        clock.tick(60)

def endscene():
    endscene = True
    while endscene:
        screen.blit(endscene, (0, 0))
        for achievementScreen in pygame.event.get():
            if achievementScreen.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #엔드버튼 만들것
            button(backButton, 1050, 50, getRect(backButton).width, getRect(backButton).height, gameMenu)
            pygame.display.update()
            clock.tick(60)

def settings():
    while True:
        screen.blit(settingsMenu, (0, 0))
        bquit = button(exitButton, 1050, 110)
        bback = button(backButton, 1050, 50)
        for settingsScreen in pygame.event.get():
            if settingsScreen.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if settingsScreen.type == MOUSEBUTTONDOWN:
                x,y = settingsScreen.pos
                if bback.collidepoint(x,y):
                    return
                if bquit.collidepoint(x,y):
                    gameMenu()
        pygame.display.update()
        clock.tick(60)

def achievement():
    achievement = True
    while achievement:
        screen.blit(achievementMenu, (0, 0))
        for achievementScreen in pygame.event.get():
            if achievementScreen.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            button(backButton, 1050, 50, getRect(backButton).width, getRect(backButton).height, gameMenu)
            pygame.display.update()
            clock.tick(60)

def gallery():
    gallery = True
    while gallery:
        screen.blit(galleryMenu, (0, 0))
        for galleryScreen in pygame.event.get():
            if galleryScreen.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            button(backButton, 1050, 50, getRect(backButton).width, getRect(backButton).height, gameMenu)
            pygame.display.update()
            clock.tick(60)

def leaderboard():
    leaderboard = True
    while leaderboard:
        screen.blit(leaderboardMenu, (0, 0))
        for leaderboardScreen in pygame.event.get():
            if leaderboardScreen.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            button(backButton, 1050, 50, getRect(backButton).width, getRect(backButton).height, gameMenu)
            pygame.display.update()
            clock.tick(60)

def quiz(img, answer):
    tries=0;
    while True:
        inventory= button(inventoryButton, 10, 3)
        setting = button(arrowLeft, 1150, 60)
        screen.blit(img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                x,y=event.pos
                if inventory.collidepoint(x,y):
                    inventory()
                if setting.collidepoint(x,y):
                    settings()
        ans = get()
        if answer == ans:
            return True
        elif answer != ans:
            tries+=1
        if tries == 5:
            #이곳에다가 You fail 이런거 집어넣고 main menu로 돌아갈것
            return False
        pygame.display.update()
        clock.tick(60)

def gameMenu():
    pygame.mixer.music.play(-1, 0.0)
    screen.blit(menu, (0, 0))
    b1=button(startButton, 150, 500)
    b2=button(leaderboardButton, 550, 500)
    b3=button(achievementButton, 950, 500)
    b4=button(settingsButton, 150, 600)
    b5=button(galleryButton, 550, 600)
    b6=button(exitButton, 950, 600)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                x,y= event.pos
                if b1.collidepoint(x,y):
                    start()
                if b2.collidepoint(x,y):
                    leaderboard()
                if b3.collidepoint(x,y):
                    achievement()
                if b4.collidepoint(x,y):
                    settings()
                if b5.collidepoint(x,y):
                    gallery()
                if b6.collidepoint(x,y):
                    quitGame()


        pygame.display.update()
        clock.tick(60)

gameMenu()