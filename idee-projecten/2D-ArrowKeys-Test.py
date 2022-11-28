from tkinter import *
from ctypes import windll
import random

windll.shcore.SetProcessDpiAwareness(1)
y = 0


class MovingProject:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('300x300')
        self.player = Label(self.window, text=".", font='Arial 32 bold')
        self.randomDot = Label(self.window, text=".", font='Arial 32 bold', fg='green')
        self.xCoordinate = 135
        self.yCoordinate = 90
        self.randomX = random.randint(50, 250)
        self.randomY = random.randint(50, 250)

    def move(self):
        self.window.bind('<Right>', self.moveRight)
        self.window.bind('<Left>', self.moveLeft)
        self.window.bind('<Up>', self.moveUp)
        self.window.bind('<Down>', self.moveDown)
        self.player.place(x=self.xCoordinate, y=self.yCoordinate)
        self.window.mainloop()

    def placeRandom(self):
        self.randomDot.place(x=self.randomX, y=self.randomY)

    def samePlace(self):
        if self.player == self.randomDot:
            # voor nu ff niks (waarschijnlijk gaan we dit ook niet gebruiken)
            pass
        self.move()

    def moveRight(self, event):
        self.xCoordinate += 3
        self.samePlace()

    def moveLeft(self, event):
        self.xCoordinate -= 3
        self.samePlace()

    def moveDown(self, event):
        self.yCoordinate += 3
        self.samePlace()

    def moveUp(self, event):
        self.yCoordinate -= 3
        self.samePlace()


subject = MovingProject()
subject.placeRandom()
subject.move()

# next I have to make something like if it is at the same spot as target then _something_
