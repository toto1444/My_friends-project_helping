import pygame


pygame.init()
fontObj = pygame.font.Font("font/sans.ttf", 32)
white = 255, 255, 255
screen = pygame.display.set_mode((1280, 720))
window = pygame.image.load("txt/txtwin2.png")
global i

def commontext2(a, b):
    screen.blit(window, (0, 520))
    screen.blit(a, (20, 540))
    screen.blit(b, (20, 580))

def commontext(a):
    screen.blit(window, (0, 520))
    screen.blit(a, (20, 540))


def line1():
    textSurfaceObj = fontObj.render("My head hurts. Both my hands and ankles are sore.", True, white)
    ts2 = fontObj.render("I opened my eyes. I feel a strong light coming in my sight.", True, white)
    commontext2 (textSurfaceObj, ts2)

def line2():
    textSurfaceObj = fontObj.render(" Probably because I had closed my eyes for a long time, I could not see very well.", True, white)
    commontext (textSurfaceObj)

def line3():
    textSurfaceObj = fontObj.render("It is hard to believe, but I am lying in the room,", True, white)
    ts2 = fontObj.render(" where I’ve never been before. This room is dark, but the laptop and the LED are bright.", True, white)
    commontext2 (textSurfaceObj, ts2)

def line4():
    textSurfaceObj = fontObj.render("I stood up listlessly. It was enough for me to distinguish", True, white)
    ts2 = fontObj.render(" objects in the room because of the LED.", True, white)
    commontext2 (textSurfaceObj, ts2)

def line5():
    textSurfaceObj = fontObj.render("I can see a firmly locked iron door with a password. ", True, white)
    ts2 = fontObj.render("I still don’t understand what’s going on.", True, white)
    commontext2 (textSurfaceObj, ts2)

def line6():
    textSurfaceObj = fontObj.render("I get close to the door. I hear a sound outside.", True, white)
    commontext (textSurfaceObj)

def line7():
    textSurfaceObj = fontObj.render("[???1]: Our work is done. So why don’t we go out and get some rest?", True, white)
    commontext (textSurfaceObj)

def line8():
    textSurfaceObj = fontObj.render("[???2]: Are you sure? If our boss knows this…", True, white)
    commontext (textSurfaceObj)

def line9():
    textSurfaceObj = fontObj.render("[???1]: Of Course! He’s not gonna able to escape from this room! ", True, white)
    ts2 = fontObj.render("  Stop being a coward and let’s go outside for 30 minutes.", True, white)
    commontext2 (textSurfaceObj, ts2)

def line10():
    textSurfaceObj = fontObj.render("[???2] hmmm…ok, I don’t think we will be scolded just for resting 30 minutes.", True, white)
    commontext (textSurfaceObj)

def line11():
    textSurfaceObj = fontObj.render("They’re walking away. I carefully put my ears to the door. ", True, white)
    ts2 = fontObj.render("I can hear a sound of the elevator outside.", True, white)
    commontext2 (textSurfaceObj, ts2)

def line12():
    textSurfaceObj = fontObj.render("I just gained valuable information from their conversation.", True, white)
    commontext (textSurfaceObj)

def line13():
    textSurfaceObj = fontObj.render("First, those two people who just left here are guards. ", True, white)
    ts2 = fontObj.render("Second, I have 30 minutes to escape from this room.", True, white)
    commontext2 (textSurfaceObj, ts2)

def line14():
    textSurfaceObj = fontObj.render("I realized that there is some small note next to the laptop.", True, white)
    commontext (textSurfaceObj)

def line15():
    textSurfaceObj = fontObj.render("I am lucky. Then the given time is 30 minutes. ", True, white)
    ts2 = fontObj.render("Let's solve the puzzles and escape the room.", True, white)
    commontext2 (textSurfaceObj,ts2)

if __name__ == '__main__':
    i