from vaginalcex_like import *

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

FPS = 60
size = (1280,720)
white = (255, 255, 255)
black = (0, 0, 0)
scale_x = 1280
scale_y = 720
coin = 0

pygame.display.set_caption("The Dark Room") #Title of the game

cooldowns = {
   "start": 0,
}

clock = pygame.time.Clock()
width = 1280 #Game width
height = 720 #Game height

images = {
    "star": pygame.image.load("img/star.png").convert_alpha(),
    "time" : pygame.image.load("img/time.png").convert_alpha(),
}

screen = pygame.display.set_mode((width, height))#Set window size
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

saveButton = pygame.image.load("img/SaveButton.png") #save button
saveButton = pygame.transform.scale(saveButton, (175, 50)) # image resize
loadButton = pygame.image.load("img/Submit-Button.png") #load button
loadButton = pygame.transform.scale(loadButton, (175, 50)) # image resize
s_loadButton = pygame.image.load("img/S-loadButton.png") #load button
s_loadButton = pygame.transform.scale(s_loadButton, (100, 100)) # image resize

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

dialogue = pygame.image.load("img/dialogue.png")
startdiag = pygame.image.load("img/startdiag.png")
startdiag = pygame.image.load("img/startdiag.png")
chap1_1 = pygame.image.load("img/chap1_1.png")
chap1_1 = pygame.transform.scale(chap1_1, (1280, 720))
chap1_2 = pygame.image.load("img/chap1_2.png")
chap1_2 = pygame.transform.scale(chap1_2, (1280, 720))
chap1_3 = pygame.image.load("img/chap1_3.png")
chap1_3 = pygame.transform.scale(chap1_3, (1280, 720))
image = [chap1_1,chap1_2,chap1_3]

pygame.mixer.music.load('sounds/Menu.wav')
effect = pygame.mixer.Sound('sounds/Text.wav')
mumble = pygame.mixer.Sound('sounds/mumble2.wav')
startdiag = pygame.image.load("img/startdiag.png")
dialogue1 = pygame.image.load('img/dialogue1.png')
dialogue2 = pygame.image.load('img/dialogue2.png')


font = pygame.font.SysFont(None, 48)
textColor = (0, 0, 0)
backgroundColor = (255, 255, 255)


achievements = {
   "I can't hold all of these!": {"description": "Finish a normal game with at least\n2500 points.", "locked": True},
   "Sex!": {"description": "Finish the game with \nleast 1000 points.", "locked": True},
}

achievementNames = [
   "I can't live any more!",
   "Sex!",
]

class foo:
    attr = 'A class attribute' # Game state save class!

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
            button(saveButton, 1050, 170, getRect(saveButton).width, getRect(saveButton).height, gameMenu) #Making..... save
            button(loadButton, 1050, 230, getRect(saveButton).width, getRect(saveButton).height, gameMenu) #Making..... save
            pygame.display.update()
            clock.tick(FPS)

def start():
    pygame.mixer.music.stop()
    screen.fill(white)
    screen.blit(startdiag, (0, 0))

    cooldowns["start"] = GetTime() + 10000

    p = 0
    event = True;
    event1 = False;
    event2 = False;
    b2 = button(inventoryButton, 10, 3)
    b3 = button(settingsInGameButton, 10, 120)
    while event:
        for startScreen in pygame.event.get():
            screen.blit(images["time"], (width-images["time"].get_width(), images["star"].get_height()+10)) #Display time image
            if IsTime(cooldowns["start"]):
                displayTime = "%02d:%02d:%02d" % ((GetTime()-cooldowns["start"])//3600000, (GetTime()-cooldowns["start"])//60000-((GetTime()-cooldowns["start"])//3600000*60), (GetTime()-cooldowns["start"])//1000-((GetTime()-cooldowns["start"])//60000*60))
                Write(screen, font, displayTime, (width-images["star"].get_width()-font.size(displayTime)[0]-5, 2*images["star"].get_height()+10-font.size(displayTime)[1])) #Display time

            if startScreen.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if startScreen.type == pygame.KEYDOWN and p<len(txt.introtxt.a):
                screen.fill(white)
                screen.blit(startdiag, (0, 0))
                button(inventoryButton, 10, 3)
                button(settingsInGameButton, 10, 120)
                if startScreen.key == K_SPACE:
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
        if p==len(txt.introtxt.a):
            event=False
            event1=True
        pygame.display.update()
        clock.tick(FPS)
    i=0
    books = pygame.Rect(700,60,200,200)
    bed = pygame.Rect(600,500,800,150)
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
                        screen.blit(pygame.transform.scale(image[i], (scale_x, scale_y)), (0, 0))
                    else:
                        i-=1
                        screen.blit(pygame.transform.scale(image[i], (scale_x, scale_y)), (0, 0))
                if(b4.collidepoint(x,y)):
                    if(i==2):
                        i=0
                        screen.blit(pygame.transform.scale(image[i], (scale_x, scale_y)), (0, 0))
                    else:
                        i+=1
                        screen.blit(pygame.transform.scale(image[i], (scale_x, scale_y)), (0, 0))
                if(books.collidepoint(x,y)) and i == 0:
                    text(txt.introtxt.b,i)
                if (bed.collidepoint(x, y)) and i == 1:
                    text(txt.introtxt.c,i)
                    if quiz(quiz1_1img, 64):
                        solvedquizzes += 1
        screen.blit(pygame.transform.scale(image[i], (scale_x, scale_y)), (0, 0))
        screen.blit(leftside, (80, 360))
        screen.blit(rightside, (1120, 360))
        button(inventoryButton, 10, 3)
        button(settingsInGameButton, 10, 120)
        pygame.display.update()
        clock.tick(FPS)

def settings():
    while True:
        screen.blit(settingsMenu, (0, 0))
        bquit = button(exitButton, 1050, 110)
        bback = button(backButton, 1050, 50)
        bsave = button(saveButton, 1050, 170) # for save
        bload = button(loadButton, 1050, 230) # for load
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
                if bsave.collidepoint(x,y):
                    with open("savelife.FuckCSE101", "wb") as f:
                        pickle.dump(foo, f)
                    return
                #if bload.collidepoint(x,y):
                #    with open("savelife.FuckCSE101", "rb") as f:
                #        foo = pickle.load(f)
        pygame.display.update()
        clock.tick(FPS)

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
            clock.tick(FPS)

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
            clock.tick(FPS)

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
            clock.tick(FPS)

def quiz(img, answer):
    tries=0;
    while True:
        inventory= button(inventoryButton, 10, 3)
        setting = button(arrowLeft, 1150, 60)
        gameload = button(s_loadButton, 1150, 80)
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
            return False
        pygame.display.update()
        clock.tick(FPS)

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
        clock.tick(FPS)

gameMenu()