import time
from ctypes import windll
from tkinter import *
from tkinter import messagebox

windll.shcore.SetProcessDpiAwareness(1)
homepage = Tk()
homepage.geometry('700x700')
homepage.title('Homepage')
homepage.configure(background='#121212')


########################################################
# CHEATPALEIS!
########################################################
def hackPaleis():
    window = Tk()
    window.title('KOVAAKS INTO HACK')
    window.geometry('700x700')

    scherm = Frame(window, width=700, height=700, background='red')
    scherm.pack()

    frame = Frame(window, width=600, height=600, background='dark red')
    frame.place(x=50, y=50)

    def login():
        username = 'tobias'
        capital = 'Tobias'
        password = 'wacht'

        if enterUser.get() == username or capital and enterPass.get() == password:
            messagebox.showinfo(title='VALID', message='LOGIN SUCCESVOL')
            time.sleep(2)

            titel.destroy()
            usernameLabel.destroy()
            enterUser.destroy()
            passwordLabel.destroy()
            enterPass.destroy()
            submit.destroy()

            logtitel = Label(window, text='CHEATPALEIS VAN TOBIAS', font='Papyrus 23 bold', background='dark red')
            logtitel.place(x=57, y=75)

            def injectedcsgo(injectcsgo=False):
                if injectcsgo == True:
                    time.sleep(1)
                    messagebox.showinfo(title='Injecting...', message='Almost done.')
                    time.sleep(1)
                    messagebox.showinfo(title='DONE', message='SUCCESFULLY INJECTED')

            def injectedvalo(injectvalo=False):
                if injectvalo == True:
                    time.sleep(1)
                    messagebox.showinfo(title='Injecting...', message='Almost done.')
                    time.sleep(1)
                    messagebox.showinfo(title='DONE', message='SUCCESFULLY INJECTED')

            def injectedtetr(injectTetr=False):
                if injectTetr == True:
                    time.sleep(1)
                    messagebox.showinfo(title='Injecting...', message='Almost done.')
                    time.sleep(1)
                    messagebox.showinfo(title='DONE', message='SUCCESFULLY INJECTED')

            def injectedletter(injectletter=False):
                if injectletter == True:
                    time.sleep(1)
                    messagebox.showinfo(title='Injecting...', message='Almost done.')
                    time.sleep(1)
                    messagebox.showinfo(title='DONE', message='SUCCESFULLY INJECTED')

            csgo = Label(window, font='Arial 20 bold', text='CSGO', background='dark red')
            csgo.place(x=100, y=275)

            injectcsgo = Button(window, text='Inject CSGO hack', font='Arial 10 bold', background='dark red',
                                activebackground='red', command=lambda: injectedcsgo(True))
            injectcsgo.place(x=300, y=275)

            valorant = Label(window, text='VALORANT', font='Arial 20 bold', background='dark red')
            valorant.place(x=100, y=375)

            injectvalo = Button(window, text='Inject VALO hack', font='Arial 10 bold', background='dark red',
                                activebackground='red', command=lambda: injectedvalo(True))
            injectvalo.place(x=300, y=375)

            teris = Label(window, text='TETRIS.IO', font='Arial 20 bold', background='dark red')
            teris.place(x=100, y=475)

            injecttetris = Button(window, text='Inject TETRIS hack', font='Arial 10 bold', background='dark red',
                                  activebackground='red', command=lambda: injectedtetr(True))
            injecttetris.place(x=300, y=475)

            letter = Label(window, text='LETTERLEAGUE', font='Arial 20 bold', background='dark red')
            letter.place(x=100, y=575)

            injectletter = Button(window, text='Inject LETTER LEAGUE hack', font='Arial 10 bold', background='dark red',
                                  activebackground='red', command=lambda: injectedletter(True))
            injectletter.place(x=400, y=575)

            logout = Button(window, text='Uitloggen', font='Arial 20 bold', background='red', activebackground='red',
                            command=lambda: [window.destroy(), hackPaleis()])
            logout.place(x=400, y=150)



        else:
            messagebox.showerror(title='ERROR', message='FOUTE GEGEVENS')

    titel = Label(window, text='HACKS VAN TOBIAS', font='Papyrus 25 bold', background='dark red')
    titel.place(x=70, y=75)

    usernameLabel = Label(window, text='Username:', font='Arial 20 bold', background='dark red')
    usernameLabel.place(x=175, y=200)

    passwordLabel = Label(window, text='Password:', font='Arial 20 bold', background='dark red')
    passwordLabel.place(x=175, y=300)

    enterUser = Entry(window, font='Arial 20 bold', background='red', foreground='dark red')
    enterUser.place(x=175, y=250)

    enterPass = Entry(window, font='Arial 20 bold', background='red', foreground='dark red', show='*')
    enterPass.place(x=175, y=350)

    submit = Button(window, text='Submit', font='Arial 20 bold', background='dark red', activebackground='red',
                    command=login)
    submit.place(x=175, y=400)

    window.mainloop()


########################################################
# CHEATPALEIS!
########################################################


########################################################
# BOODSCHAPPENLIJSTJE!
########################################################
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


    ########################################################
    # BOODSCHAPPENLIJSTJE!
    ########################################################


def bsl():
    boodlijst = Boodschappenlijst()
    boodlijst.plaaten()


knopBoodLijst = Button(homepage, text='Boodschappenlijst', font='Arial 20 bold', width=35, command=bsl)
knopBoodLijst.pack()

tobiasHackerPaleis = Button(homepage, text='Tobias Hack Paleis', font='Arial 20 bold', width=35,
                            background='light blue', command=hackPaleis, )
tobiasHackerPaleis.pack()

homepage.mainloop()
