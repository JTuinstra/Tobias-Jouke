from ctypes import windll
from tkinter import *

windll.shcore.SetProcessDpiAwareness(1)


class Boodschappenlijst:

    def __init__(self):
        self.inlijst = []
        self.plaatsX = 50
        self.plaatsY = 110

        self.window = Tk()
        self.window.title('Boodschappenlijst')
        self.window.geometry('500x600')
        self.window.configure(background='#121212')

        ##############################

        self.submit = Button(self.window, text='Submit', font='Arial 12 bold', command=self.antwoord)
        self.entry = Entry(self.window, width=20, font='Arial 15 bold')
        self.lijn = Label(self.window, text='-' * 75, background='#121212', foreground='white')
        self.getInBeeld = Label(self.window, background='#121212', foreground='white', font='Arial 15 bold')

    def plaaten(self):
        self.submit.place(x=350, y=25)
        self.entry.place(x=45, y=28)
        self.lijn.place(x=20, y=85)
        self.getInBeeld.place(x=self.plaatsX, y=self.plaatsY)
        self.window.mainloop()

    def antwoord(self):
        watKomtErin = self.entry.get()

        self.inlijst.append(watKomtErin)


boodlijst = Boodschappenlijst()
boodlijst.plaaten()
