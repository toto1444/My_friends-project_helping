import pygame, txt.introtxt, time, introdialog
from pygame.locals import*

pygame.init()

size = width, height = 1280, 720
white = 255, 255, 255
black = 0, 0, 0


clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
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

leftside = pygame.image.load("img/leftside.png")
rightside = pygame.image.load("img/rightside.png")

quiz1_1img = pygame.image.load("img/quiz1.png")
quiz1_2img = pygame.image.load("img/quiz2.png")
quiz1_3img = pygame.image.load("img/quiz3.png")

dialogue = pygame.image.load("img/dialogue.png")
chap1_1 = pygame.image.load("img/chap1_1.png")
chap1_2 = pygame.image.load("img/chap1_2.png")
chap1_3 = pygame.image.load("img/chap1_3.png")

pygame.display.set_icon(favicon)

startButton = pygame.image.load("img/start.png")
leaderboardButton = pygame.image.load("img/leaderboard.png")
achievementButton = pygame.image.load("img/achievement.png")
settingsButton = pygame.image.load("img/settings.png")
galleryButton = pygame.image.load("img/gallery.png")
exitButton = pygame.image.load("img/exit.png")
backButton = pygame.image.load("img/back.png")
quizButton = pygame.image.load("img/test_black.png")

pygame.mixer.music.load('sounds/Menu.wav')

font = pygame.font.SysFont(None, 48)
textColor = (0, 0, 0)
backgroundColor = (255, 255, 255)

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
    quit()

def button(pic, x, y, w, h,  action=None):
    picR = getRect(pic)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        picR.x = x
        picR.y = y
        screen.blit(pic, picR)


        if click[0] == 1 and action != None:
            action()
    else:
        picR.x = x
        picR.y = y
        screen.blit(pic, picR)

def unpause():
    global pause
    pause = False

def paused():
    screen.blit(settingsMenu, (0, 0))

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button(startButton, 150, 450, getRect(startButton).width, getRect(startButton).height, unpause)
        pygame.display.update()
        clock.tick(60)

def inventory():
    inventory = True
    while inventory:
        screen.blit(inventoryMenu, (0, 0))
        for startScreen in pygame.event.get():
            if startScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
        button(arrowLeft, 1150, 60, getRect(arrowLeft).width, getRect(arrowLeft).height, start)
        pygame.display.update()
        clock.tick(60)

def inventory1():
    inventory = True
    while inventory:
        screen.blit(inventoryMenu, (0, 0))
        for startScreen in pygame.event.get():
            if startScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
        button(arrowLeft, 1150, 60, getRect(arrowLeft).width, getRect(arrowLeft).height, start1)
        pygame.display.update()
        clock.tick(60)

def inventory2():
    inventory = True
    while inventory:
        screen.blit(inventoryMenu, (0, 0))
        for startScreen in pygame.event.get():
            if startScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
        button(arrowLeft, 1150, 60, getRect(arrowLeft).width, getRect(arrowLeft).height, start2)
        pygame.display.update()
        clock.tick(60)

def inventory3():
    inventory = True
    while inventory:
        screen.blit(inventoryMenu, (0, 0))
        for startScreen in pygame.event.get():
            if startScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
        button(arrowLeft, 1150, 60, getRect(arrowLeft).width, getRect(arrowLeft).height, start3)
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
            button(backButton, 1050, 50, getRect(backButton).width, getRect(backButton).height, start1)
            button(exitButton, 1050, 110, getRect(exitButton).width, getRect(exitButton).height, gameMenu)
            pygame.display.update()
            clock.tick(60)

def settingsInGame1():
    settingsInGame = True
    while settingsInGame:
        screen.blit(settingsMenu, (0, 0))
        for settingsScreen in pygame.event.get():
            if settingsScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
            button(backButton, 1050, 50, getRect(backButton).width, getRect(backButton).height, start1)
            button(exitButton, 1050, 110, getRect(exitButton).width, getRect(exitButton).height, gameMenu)
            pygame.display.update()
            clock.tick(60)

def settingsInGame2():
    settingsInGame = True
    while settingsInGame:
        screen.blit(settingsMenu, (0, 0))
        for settingsScreen in pygame.event.get():
            if settingsScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
            button(backButton, 1050, 50, getRect(backButton).width, getRect(backButton).height, start2)
            button(exitButton, 1050, 110, getRect(exitButton).width, getRect(exitButton).height, gameMenu)
            pygame.display.update()
            clock.tick(60)

def settingsInGame3():
    settingsInGame = True
    while settingsInGame:
        screen.blit(settingsMenu, (0, 0))
        for settingsScreen in pygame.event.get():
            if settingsScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
            button(backButton, 1050, 50, getRect(backButton).width, getRect(backButton).height, start3)
            button(exitButton, 1050, 110, getRect(exitButton).width, getRect(exitButton).height, gameMenu)
            pygame.display.update()
            clock.tick(60)

def start():
    pygame.mixer.music.stop()
    start = True
    while start:
        screen.blit(dialogue, (0, 0))
        for startScreen in pygame.event.get():
            if startScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
            button(inventoryButton, 10, 3, getRect(inventoryButton).width, getRect(inventoryButton).height, inventory)
            button(settingsInGameButton, 10, 120, getRect(settingsInGameButton).width, getRect(settingsInGameButton).height, settingsInGame)
            pygame.display.update()

            introdialog.dialogue()

            start = False
            start1()

            clock.tick(60)

def start1():
    start1 = True
    while start1:
        screen.blit(chap1_1, (0, 0))
        for start1Screen in pygame.event.get():
            if start1Screen.type == pygame.QUIT:
                pygame.quit()
                quit()
            button(inventoryButton, 10, 3, getRect(inventoryButton).width, getRect(inventoryButton).height, inventory1)
            button(settingsInGameButton, 10, 120, getRect(settingsInGameButton).width, getRect(settingsInGameButton).height, settingsInGame1)
            button(leftside, 80, 360, getRect(leftside).width, getRect(leftside).height, start2)
            button(rightside, 1120,360, getRect(rightside).width, getRect(rightside).height, start3)
            #Player can click below objects
            button(quizButton,300,300, getRect(quizButton).width, getRect(quizButton).height, quiz1_1)
            #Text_In_Start.line1()

            pygame.display.update()
            clock.tick(60)

def start2():
    start2 = True
    while start2:
        screen.blit(chap1_2, (0, 0))
        for start2Screen in pygame.event.get():
            if start2Screen.type == pygame.QUIT:
                pygame.quit()
                quit()
            button(inventoryButton, 10, 3, getRect(inventoryButton).width, getRect(inventoryButton).height, inventory2)
            button(settingsInGameButton, 10, 120, getRect(settingsInGameButton).width, getRect(settingsInGameButton).height, settingsInGame2)
            button(leftside, 80, 360, getRect(leftside).width, getRect(leftside).height, start3)
            button(rightside, 1120, 360, getRect(rightside).width, getRect(rightside).height, start1)
            #Player can click below objects
            button(quizButton,300,300, getRect(quizButton).width, getRect(quizButton).height, quiz1_2)

            pygame.display.update()
            clock.tick(60)

def start3():
    start3 = True
    while start3:
        screen.blit(chap1_3, (0, 0))
        for start3Screen in pygame.event.get():
            if start3Screen.type == pygame.QUIT:
                pygame.quit()
                quit()
            button(inventoryButton, 10, 3, getRect(inventoryButton).width, getRect(inventoryButton).height, inventory3)
            button(settingsInGameButton, 10, 120, getRect(settingsInGameButton).width, getRect(settingsInGameButton).height, settingsInGame3)
            button(leftside, 80, 360, getRect(leftside).width, getRect(leftside).height, start1)
            button(rightside, 1120,360, getRect(rightside).width, getRect(rightside).height, start2)
            #Player can click below objects
            button(quizButton,300,300, getRect(quizButton).width, getRect(quizButton).height, quiz1_3)
            #Text_In_Start.line1()

            pygame.display.update()
            clock.tick(60)

def quiz1_1():
    quiz1 = True
    while quiz1_1:
        screen.blit(quiz1_1img, (0, 0))
        for start1Screen in pygame.event.get():
            if start1Screen.type == pygame.QUIT:
                pygame.quit()
                quit()
            button(inventoryButton, 10, 3, getRect(inventoryButton).width, getRect(inventoryButton).height, inventory)
            button(settingsInGameButton, 10, 120, getRect(settingsInGameButton).width, getRect(settingsInGameButton).height, settingsInGame1)
            button(arrowLeft, 1150, 60, getRect(arrowLeft).width, getRect(arrowLeft).height, start1)
            #input keyboard

            pygame.display.update()
            clock.tick(60)

def quiz1_2():
    pygame.mixer.music.stop()
    quiz2 = True
    while quiz2:
        screen.blit(quiz1_2img, (0, 0))
        for start1Screen in pygame.event.get():
            if start1Screen.type == pygame.QUIT:
                pygame.quit()
                quit()
            button(inventoryButton, 10, 3, getRect(inventoryButton).width, getRect(inventoryButton).height, inventory)
            button(settingsInGameButton, 10, 120, getRect(settingsInGameButton).width, getRect(settingsInGameButton).height, settingsInGame2)
            button(arrowLeft, 1150, 60, getRect(arrowLeft).width, getRect(arrowLeft).height, start2)
            # input keyboard

            pygame.display.update()
            clock.tick(60)

def quiz1_3():
    pygame.mixer.music.stop()
    quiz3 = True
    while quiz3:
        screen.blit(quiz1_3img, (0, 0))
        for start1Screen in pygame.event.get():
            if start1Screen.type == pygame.QUIT:
                pygame.quit()
                quit()
            button(inventoryButton, 10, 3, getRect(inventoryButton).width, getRect(inventoryButton).height, inventory)
            button(settingsInGameButton, 10, 120, getRect(settingsInGameButton).width, getRect(settingsInGameButton).height, settingsInGame3)
            button(arrowLeft, 1150, 60, getRect(arrowLeft).width, getRect(arrowLeft).height, start3)
            #input keyboard

            pygame.display.update()
            clock.tick(60)



def settings():
    settings = True
    while settings:
        screen.blit(settingsMenu, (0, 0))
        for settingsScreen in pygame.event.get():
            if settingsScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
            button(backButton, 1050, 50, getRect(backButton).width, getRect(backButton).height, gameMenu)
            pygame.display.update()
            clock.tick(60)

def achievement():
    achievement = True
    while achievement:
        screen.blit(achievementMenu, (0, 0))
        for achievementScreen in pygame.event.get():
            if achievementScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
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
                quit()
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
                quit()
            button(backButton, 1050, 50, getRect(backButton).width, getRect(backButton).height, gameMenu)
            pygame.display.update()
            clock.tick(60)

def gameMenu():
    pygame.mixer.music.play(-1)
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        screen.blit(menu, (0, 0))

        button(startButton, 150, 500, getRect(startButton).width, getRect(startButton).height, start)
        button(leaderboardButton, 550, 500, getRect(leaderboardButton).width, getRect(leaderboardButton).height, leaderboard)
        button(achievementButton, 950, 500, getRect(achievementButton).width, getRect(achievementButton).height, achievement)
        button(settingsButton, 150, 600, getRect(achievementButton).width, getRect(achievementButton).height, settings)
        button(galleryButton, 550, 600, getRect(achievementButton).width, getRect(achievementButton).height, gallery)
        button(exitButton, 950, 600, getRect(achievementButton).width, getRect(achievementButton).height, quitGame)

        pygame.display.update()
        clock.tick(60)

gameMenu()