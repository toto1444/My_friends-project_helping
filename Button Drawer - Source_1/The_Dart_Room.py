import pygame

pygame.init()

display_width = 1024
display_height = 700

black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (53,115,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Dark Room')
clock = pygame.time.Clock()

def button(message, x, y, w, h, ic, ac, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
	smallText = pygame.font.SysFont("comicsansms",20)
	textSurf, textRect = text_objects(message, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	gameDisplay.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def quitgame():
	pygame.quit()
	quit()

def start():

	start = True
	while start:
		for startScreen in pygame.event.get():
			if startScreen.type == pygame.QUIT:
				pygame.quit()
				quit()

			gameDisplay.fill(white)
			startText = pygame.font.SysFont("comicsanms", 30)
			TS, TR = text_objects("Start", startText)
			TR.topright = ((10, 20),(20, 30))
			gameDisplay.blit(TS, TR)

			pygame.display.update()
			clock.tick(30)


def settings():
	settings = True
	while settings:
		for settingScreen in pygame.event.get():
			if settingScreen.type == pygame.QUIT:
				pygame.quit()
				quit()

			gameDisplay.fill(white)
			settingsText = pygame.font.SysFont("comicsanms", 30)
			TS, TR = text_objects("Settings", settingsText)
			TR.topright = ((10, 20),(20, 30))
			gameDisplay.blit(TS, TR)

			button ("back",150, 450, 100, 50, green, bright_green, game_menu)
			print "YEE"

			pygame.display.update()
			clock.tick(30)

def achievement():
	achievement = True
	while achievement:
		for achievementScreen in pygame.event.get():
			if achievementScreen.type == pygame.QUIT:
				pygame.quit()
				quit()

			gameDisplay.fill(white)
			achievementText = pygame.font.SysFont("comicsanms", 30)
			TS, TR = text_objects("Achievement", achievementText)
			TR.topright = ((10, 20),(20, 30))
			gameDisplay.blit(TS, TR)

			pygame.display.update()
			clock.tick(30)


def gallery():
	game_menu = True
	while gallery:
		for galleryScreen in pygame.event.get():
			if galleryScreen.type == pygame.QUIT:
				pygame.quit()
				quit()

			gameDisplay.fill(white)
			galleryText = pygame.font.SysFont("comicsanms", 30)
			TS, TR = text_objects("Gallery", galleryText)
			TR.topright = ((10, 20),(20, 30))
			gameDisplay.blit(TS, TR)

			pygame.display.update()
			clock.tick(30)

def leaderboard():
	leaderboard = True
	while leaderboard:
		for leaderboardScreen in pygame.event.get():
			if leaderboardScreen.type == pygame.QUIT:
				pygame.quit()
				quit()

			gameDisplay.fill(white)
			leaderboardText = pygame.font.SysFont("comicsanms", 30)
			TS, TR = text_objects("Leaderboard", leaderboardText)
			TR.topright = ((10, 20),(20, 30))
			gameDisplay.blit(TS, TR)

			pygame.display.update()
			clock.tick(30)

def game_menu():
	menu = True
	while menu:
		for intro in pygame.event.get():
			if intro.type == pygame.QUIT:
				pygame.quit()
				quit()

			gameDisplay.fill(white)
			titleText = pygame.font.SysFont("comicsansms", 115)
			TS, TR = text_objects("The Dark Room", titleText)
			TR.center = ((display_width/2),(display_height)/2)
			gameDisplay.blit(TS, TR)

			button("Start", 150, 450, 100, 50, green, bright_green, start)
			button("gallery", 300, 450, 100, 50, green, bright_green, gallery)
			button("achievement", 450, 450, 100, 50, green, bright_green, achievement)
			button("settings", 150, 600, 100, 50, green, bright_green, settings)
			button("leaderboard", 300, 600, 100, 50, green, bright_green, leaderboard)
			button("quit", 450, 600, 100, 50, green, bright_green, quit)

			pygame.display.update()
			clock.tick(30)

game_menu()