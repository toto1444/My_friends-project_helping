import pygame,sys
from pygame.locals import *


pygame.init()
fontObj = pygame.font.Font("font/sans.ttf", 32)
white = (255, 255, 255)
screen = pygame.display.set_mode((1280, 720))
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]

def text(text,b, c=None):
    if c!=None:
        texta = fontObj.render(b, True, white)
        textb = fontObj.render(c, True, white)
        text.append((texta,textb))
    else:
        texta = fontObj.render(b, True, white)
        text.append((texta,))

text(a,"My head hurts. Both my hands and ankles are sore.", "I opened my eyes. I feel a strong light coming in my sight.")
text(a," Probably because I had closed my eyes for a long time, I could not see very well.")
text(a,"It is hard to believe, but I am lying in the room,", " where I’ve never been before. This room is dark, but the laptop and the LED are bright.")
text(a,"I stood up listlessly. It was enough for me to distinguish", " objects in the room because of the LED.")
text(a,"I can see a firmly locked iron door with a password. ", "I still don’t understand what’s going on.")
text(a,"I get close to the door. I hear a sound outside.")
text(a,"[???1]: Our work is done. So why don’t we go out and get some rest?")
text(a,"[???2]: Are you sure? If our boss knows this…")
text(a,"[???1]: Of Course! He’s not gonna able to escape from this room! ", "Stop being a coward and let’s go outside for 30 minutes.")
text(a,"[???2] hmmm…ok, I don’t think we will be scolded just for resting 30 minutes.")
text(a,"They’re walking away. I carefully put my ears to the door. ", "I can hear a sound of the elevator outside.")
text(a,"I just gained valuable information from their conversation.")
text(a,"First, those two people who just left here are guards. ", "Second, I have 30 minutes to escape from this room.")
text(a,"I realized that there is some small note next to the laptop.")
text(a,"I am lucky. Then the given time is 30 minutes. ", "Let's solve the puzzles and escape the room.")
text(a,"")

text(b,"There are books")
text(b,"")

text(c,"It's an old bed")
text(c,"I lifted the blanket")
text(c,"!!!!")
text(c,"I found a mysterious paper")
text(c,"")

text(d,"It's a laptop")
text(d,"It's running a weird program")
text(d,"When i touched it, it suddenly changed to another screen")
text(d,"")

text(e,"It's a cloth")
text(e,"a small piece of paper is in the cloth.")
text(e,"")

text(f,"it's a doorlock. I think we need to solve the question to leave this room.")
text(f,"")