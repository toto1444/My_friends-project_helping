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
pygame.display.set_icon(favicon)

startButton = pygame.image.load("img/start.png")
leaderboardButton = pygame.image.load("img/leaderboard.png")
achievementButton = pygame.image.load("img/achievement.png")
settingsButton = pygame.image.load("img/settings.png")
galleryButton = pygame.image.load("img/gallery.png")
exitButton = pygame.image.load("img/exit.png")
backButton = pygame.image.load("img/back.png")

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
    start = True
    while start:
        screen.blit(startMenu, (0, 0))
        for startScreen in pygame.event.get():
            if startScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
            button(inventoryButton, 10, 3, getRect(inventoryButton).width, getRect(inventoryButton).height, inventory)
            button(settingsInGameButton, 10, 120, getRect(settingsInGameButton).width, getRect(settingsInGameButton).height, settingsInGame)
            pygame.display.update()

            introdialog.dialogue()
            

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