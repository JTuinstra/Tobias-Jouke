# Ik wil met een class de 'blueprint' van de homepage maken
from tkinter import *
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)  # NOTE: Deze windll en deze command heb ik online gevonden.
# NOTE: Dit zorgt ervoor dat de text in de window heel scherp is.
window = Tk()
window.geometry('900x400')
window.configure(background='#121212')

textOnTop = Label(window, text="Homepage", font='Antipasto', fg='white', bg='#121212', padx=20, pady=5)
textOnTop.grid(row=0, column=0)


class Homepage:
    def __init__(self, knoptext, row, column, command = print("No command added")):
        self.knoptext = knoptext
        self.row = row
        self.column = column
        self.command = command

    def placeknop(self):
        knopOnScreen = Button(window, text=self.knoptext, padx=30, pady=20, command=self.command)
        knopOnScreen.grid(row=self.row, column=self.column)


# We kunnen er ook bij doen dat we hieronder de commands van de knoppen gelijk kunnen kiezen.
knop1 = Homepage('Knop1', 1, 0, lambda:print("Hello"))
knop2 = Homepage('Knop2', 2, 0)
knop1.placeknop(), knop2.placeknop()

window.mainloop()

# Dit is allemaal gewoon ff een main concept voor wat we kunnen doen.
