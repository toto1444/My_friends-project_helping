import pygame, txt.introtxt, time, introdialog, main
from pygame.locals import*

pygame.init()

inventoryButton = pygame.image.load("img/inventoryButton.png")
settingsInGameButton = pygame.image.load("img/settingsButton.png")
inventoryMenu = pygame.image.load("img/inventory.png")
arrowLeft = pygame.image.load("img/arrow.png")

def inventory():
    inventory = True
    while inventory:
        main.screen.blit(inventoryMenu, (0, 0))
        for startScreen in pygame.event.get():
            if startScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
        main.button(arrowLeft, 1150, 60, main.getRect(arrowLeft).width, main.getRect(arrowLeft).height, start)
        pygame.display.update()
        main.clock.tick(60)


def settingsInGame():
    settingsInGame = True
    while settingsInGame:
        main.screen.blit(main.settingsMenu, (0, 0))
        for settingsScreen in pygame.event.get():
            if settingsScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
            main.button(main.backButton, 1050, 50, main.getRect(main.backButton).width, main.getRect(main.backButton).height, start)
            main.button(main.exitButton, 1050, 110, main.getRect(main.exitButton).width, main.getRect(main.exitButton).height, main.gameMenu)
            pygame.display.update()
            main.clock.tick(60)


def start():
    pygame.mixer.music.stop()
    start = True
    while start:
        main.screen.blit(main.startMenu, (0, 0))
        for startScreen in pygame.event.get():
            if startScreen.type == pygame.QUIT:
                pygame.quit()
                quit()
            main.button(inventoryButton, 10, 3, main.getRect(inventoryButton).width, main.getRect(inventoryButton).height, inventory)
            main.button(settingsInGameButton, 10, 120, main.getRect(settingsInGameButton).width, main.getRect(settingsInGameButton).height, settingsInGame)
            pygame.display.update()

            introDialog()

            main.clock.tick(60)

def introDialog():
    introdialog.dialogue()
    pygame.quit()
