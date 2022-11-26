from tkinter import *
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)


class Boodschappenlijst:
    def __init__(self):
        self.producten = []
        self.eersteY = 90
        self.nieuweX = 35
        self.testX = 0
        self.count = 1
        self.window = Tk()
        self.entry = Entry(self.window, font='Arial 20 bold', width=13)
        self.lijn = Label(self.window, text='-' * 73, background='#121212', foreground='#F0F8FF')
        self.submit = Button(self.window, text='Submit', font='Arial 13 bold', background='#F0F8FF',
                             command=self.antwoordinscherm)

    def antwoordinscherm(self):
        if self.testX == 10:
            self.nieuweX = 250
            self.eersteY = 90
        self.antwoord = self.entry.get()
        self.producten.append(self.antwoord)
        if self.antwoord in self.producten:
            print('Zit al in')

        else:
            self.producten.append(self.antwoord)
            print('Zit nu wel in')
        self.entryInScreen = Label(self.window,
                                   text='1 x ' + self.antwoord,
                                   font='arial 20 bold',
                                   background='#121212',
                                   foreground='#F0F8FF')
        self.entryInScreen.place(x=self.nieuweX, y=self.eersteY)
        self.eersteY += 50
        self.testX += 1

    def createwindow(self):
        self.window.configure(background='#121212')
        self.window.geometry('500x600')
        self.entry.place(x=60, y=10)
        self.lijn.place(x=25, y=60)
        self.submit.place(x=360, y=10)
        self.window.mainloop()


boodschappenlijsje = Boodschappenlijst()
boodschappenlijsje.createwindow()
