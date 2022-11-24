import time
from tkinter import *
from tkinter import messagebox


def mainscreen():
    window = Tk()
    window.title('KOVAAKS INTO HACK')
    window.geometry('700x700')


    scherm = Frame(window, width=700, height=700, background='red')
    scherm.pack()

    frame = Frame(window, width=600, height=600, background='dark red')
    frame.place(x=50, y=50)

    def login():
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
                            command=lambda: [window.destroy(), mainscreen()])
            logout.place(x=400, y=150)



        else:
            messagebox.showerror(title='ERROR', message='FOUTE GEGEVENS')

    titel = Label(window, text='HACKS VAN TOBIAS', font='Papyrus 25 bold', background='dark red')
    titel.place(x=125, y=75)

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


mainscreen()
