from ctypes import windll
from tkinter import *

producten = []

windll.shcore.SetProcessDpiAwareness(1)
window = Tk()
window.title('Boodschappenlijstje')
window.geometry('500x600')
window.configure(background='#121212')

entry = Entry(window, font='Arial 20 bold', width=13)
entry.place(x=60, y=10)

lijn = Label(window, text='-' * 73, background='#121212', foreground='#F0F8FF')
lijn.place(x=25, y=60)

eersteY = 90
nieuweX = 35
testX = 0
if testX == 9:
    nieuweX = 350
    eersteY = 90


def antwoordinscherm():
    global eersteY
    global testX
    global nieuweX
    global producten
    if testX == 10:
        nieuweX = 250
        eersteY = 90
    antwoord = entry.get()
    if antwoord in producten:
        print('Zit al in')
    else:
        producten.append(antwoord)
        print('Zit nu wel in')
    entryinscreen = Label(window, text='1 x ' + antwoord, font='arial 20 bold', background='#121212',
                          foreground='#F0F8FF')
    entryinscreen.place(x=nieuweX, y=eersteY)
    eersteY += 50
    testX += 1


submit = Button(window, text='Submit', font='Arial 13 bold', background='#F0F8FF', command=antwoordinscherm)
submit.place(x=315, y=10)

window.mainloop()
