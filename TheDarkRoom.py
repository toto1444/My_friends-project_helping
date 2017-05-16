_author_ = 'kang11136'

from graphics import *

def main():
    win = GraphWin("Mytitle", 1366, 768)
    title = Image(Point(0,0), "titlepage.gif")
    title.draw(win)
    start = Image(Point(260, 500), "start.png")
    start.draw(win)
    achievement = Image(Point(660, 500), "achievement.png")
    achievement.draw(win)
    gallery = Image(Point(1060, 500), "gallery.png")
    gallery.draw(win)
    settings = Image(Point(260, 600), "settings.png")
    settings.draw(win)
    leaderboard = Image(Point(660, 600), "leaderboard.png")
    leaderboard.draw(win)
    exit = Image(Point(1060, 600), "exit.png")
    exit.draw(win)
    message = Text(Point(660, 200), "The Dark Room")
    message.setSize(33)
    message.setFace("helvetica")
    message.setTextColor("red")
    message.draw(win)


    win.getMouse()
    win.close()

main()

