import time
from ctypes import windll
from tkinter import *
from tkinter import messagebox

windll.shcore.SetProcessDpiAwareness(1)


def mainPage():
    homepage = Tk()
    homepage.geometry('700x700')
    homepage.title('Homepage')
    homepage.configure(background='#121212')

    ########################################################
    # CHEATPALEIS!
    ########################################################
    def hackPaleis():
        homepage.title('KOVAAKS INTO HACK')
        homepage.title('HackPaleis')

        scherm = Frame(homepage, width=700, height=700, background='red')
        scherm.pack()

        frame = Frame(homepage, width=600, height=600, background='dark red')
        frame.place(x=50, y=50)

        def login(event):
            username = ''
            capital = 'Tobias'
            password = ''

            if enterUser.get() == username or capital and enterPass.get() == password:
                messagebox.showinfo(title='VALID', message='LOGIN SUCCESVOL')
                time.sleep(2)

                titel.destroy()
                usernameLabel.destroy()
                enterUser.destroy()
                passwordLabel.destroy()
                enterPass.destroy()
                submit.destroy()

                logtitel = Label(homepage, text='CHEATPALEIS VAN TOBIAS', font='Papyrus 23 bold', background='dark red')
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

                csgo = Label(homepage, font='Arial 20 bold', text='CSGO', background='dark red')
                csgo.place(x=100, y=275)

                injectcsgo = Button(homepage, text='Inject CSGO hack', font='Arial 10 bold', background='dark red',
                                    activebackground='red', command=lambda: injectedcsgo(True))
                injectcsgo.place(x=300, y=275)

                valorant = Label(homepage, text='VALORANT', font='Arial 20 bold', background='dark red')
                valorant.place(x=100, y=375)

                injectvalo = Button(homepage, text='Inject VALO hack', font='Arial 10 bold', background='dark red',
                                    activebackground='red', command=lambda: injectedvalo(True))
                injectvalo.place(x=300, y=375)

                teris = Label(homepage, text='TETRIS.IO', font='Arial 20 bold', background='dark red')
                teris.place(x=100, y=475)

                injecttetris = Button(homepage, text='Inject TETRIS hack', font='Arial 10 bold', background='dark red',
                                      activebackground='red', command=lambda: injectedtetr(True))
                injecttetris.place(x=300, y=475)

                letter = Label(homepage, text='LETTERLEAGUE', font='Arial 20 bold', background='dark red')
                letter.place(x=100, y=575)

                injectletter = Button(homepage, text='Inject LETTER LEAGUE hack', font='Arial 10 bold',
                                      background='dark red',
                                      activebackground='red', command=lambda: injectedletter(True))
                injectletter.place(x=400, y=575)

                logout = Button(homepage, text='Uitloggen', font='Arial 20 bold', background='red',
                                activebackground='red',
                                command=lambda: [homepage.destroy(), mainPage()])
                logout.place(x=400, y=150)



            else:
                messagebox.showerror(title='ERROR', message='FOUTE GEGEVENS')

        titel = Label(homepage, text='HACKS VAN TOBIAS', font='Papyrus 25 bold', background='dark red')
        titel.place(x=70, y=75)

        usernameLabel = Label(homepage, text='Username:', font='Arial 20 bold', background='dark red')
        usernameLabel.place(x=175, y=200)

        passwordLabel = Label(homepage, text='Password:', font='Arial 20 bold', background='dark red')
        passwordLabel.place(x=175, y=300)

        enterUser = Entry(homepage, font='Arial 20 bold', background='red', foreground='dark red')
        enterUser.place(x=175, y=250)

        enterPass = Entry(homepage, font='Arial 20 bold', background='red', foreground='dark red', show='*')
        enterPass.place(x=175, y=350)

        submit = Button(homepage, text='Submit', font='Arial 20 bold', background='dark red', activebackground='red',
                        command=lambda: login(''))
        submit.place(x=175, y=400)

        homepage.bind('<Return>', login)

    ########################################################
    # CHEATPALEIS!
    ########################################################

    ########################################################
    # BOODSCHAPPENLIJSTJE!
    ########################################################
    class Boodschappenlijst:

        def __init__(self):
            self.arrow = PhotoImage(file='arrow.png')
            self.arrowKnop = Button(homepage, image=self.arrow)
            self.inlijst = []
            self.plaatsX = 50
            self.plaatsY = 60
            self.countFornextRow = 0
            self.productCount = 1

            ##############################

            homepage.bind('<Return>', self.antwoord)
            homepage.title('Boodschappenlijstje')
            homepage.geometry('500x600')
            self.submit = Button(homepage, text='Submit', font='Arial 12 bold', command=self.antwoord)
            self.entry = Entry(homepage, width=20, font='Arial 15 bold')
            self.lijn = Label(homepage, text='-' * 75, background='#121212', foreground='white')
            self.exitKnop = Button(homepage, text='Exit', font='arial 10 bold',
                                   command=lambda: [homepage.destroy(), mainPage()])

        def plaaten(self):
            self.submit.place(x=350, y=25)
            self.entry.place(x=45, y=28)
            self.lijn.place(x=20, y=85)
            self.exitKnop.place(x=445, y=30)

        def antwoord(self, event=None):
            if len(self.entry.get()) <= 11:  # <----checking if length is too long

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

                self.getInBeeld = Label(homepage, text=str(self.productCount) + ' x ' + self.entry.get(),
                                        background='#121212', foreground='white', font='Arial 15 bold')
                self.getInBeeld.place(x=self.plaatsX, y=self.plaatsY)

            else:
                messagebox.showinfo(title='Te lang', message='Dit woord is te lang.')

    ########################################################
    # BOODSCHAPPENLIJSTJE!
    ########################################################

    ########################################################
    # Knoppen in homepage
    ########################################################

    def callBoodlijst():
        knopBoodLijst.destroy()
        tobiasHackerPaleis.destroy()
        boodlijst = Boodschappenlijst()
        boodlijst.plaaten()

    def callHackPaleis():
        knopBoodLijst.destroy()
        tobiasHackerPaleis.destroy()
        hackPaleis()

    knopBoodLijst = Button(homepage, text='Boodschappenlijst', font='Arial 20 bold', width=35, command=callBoodlijst)
    knopBoodLijst.pack()

    tobiasHackerPaleis = Button(homepage, text='Tobias Hack Paleis', font='Arial 20 bold', width=35,
                                background='light blue', command=callHackPaleis, )
    tobiasHackerPaleis.pack()

    ########################################################
    # Knoppen in homepage
    ########################################################

    homepage.mainloop()


mainPage()
