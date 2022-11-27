from ctypes import windll
from tkinter import *
from tkinter import messagebox

windll.shcore.SetProcessDpiAwareness(1)


class Boodschappenlijst:

    def __init__(self):
        self.inlijst = []
        self.plaatsX = 50
        self.plaatsY = 60
        self.countFornextRow = 0
        self.productCount = 1

        self.window = Tk()
        self.window.title('Boodschappenlijst')
        self.window.geometry('500x600')
        self.window.configure(background='#121212')

        ##############################

        self.window.bind('<Return>', self.antwoord)
        self.submit = Button(self.window, text='Submit', font='Arial 12 bold', command=self.antwoord)
        self.entry = Entry(self.window, width=20, font='Arial 15 bold')
        self.lijn = Label(self.window, text='-' * 75, background='#121212', foreground='white')

    def plaaten(self):
        self.submit.place(x=350, y=25)
        self.entry.place(x=45, y=28)
        self.lijn.place(x=20, y=85)
        self.window.mainloop()

    def antwoord(self, event=None):
        if len(self.entry.get()) <= 11:  #<----checking if length is too long

            if self.countFornextRow == 10:  # <-----positioning
                self.plaatsX = 270
                self.plaatsY = 110

            # If statements voor wat er in entry zit
            if self.entry.get() in self.inlijst:
                self.countFornextRow = self.countFornextRow
                self.productCount += 1


            else:
                self.inlijst.append(self.entry.get())
                self.plaatsY += 50
                self.countFornextRow += 1
                self.productCount = 1
            # If statements voor wat er in entry zit

            self.getInBeeld = Label(self.window, text=str(self.productCount) + ' x ' + self.entry.get(),
                                    background='#121212', foreground='white', font='Arial 15 bold')
            self.getInBeeld.place(x=self.plaatsX, y=self.plaatsY)

        else:
            messagebox.showinfo(title='Te lang', message='Dit woord is te lang.')


boodlijst = Boodschappenlijst()
boodlijst.plaaten()
