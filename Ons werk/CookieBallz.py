from tkinter import *


class CokkieBalzz:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x700')
        self.window.configure(background='white')
        self.window.title('Cockieball')

        self.coinsPerClick = 1
        self.DoubleCost=10
        self.balance = 0
        self.cookieImage = PhotoImage(file='cookie.png')
        self.shopicon = PhotoImage(file='shopicon.png')
        self.snorcookie = PhotoImage(file='snor_cookie.png')

        self.balanceOnScreen = Label(self.window,  # <----Geld boven scherm
                                     text=self.balance,
                                     background='white',
                                     font='Arial 30 bold')

        self.shopKnop = Button(self.window,
                               image=self.shopicon,
                               borderwidth=0,
                               background='white', command=self.shop)

        self.cookie = Button(self.window,
                             image=self.cookieImage,
                             background='white',
                             borderwidth=0,
                             activebackground='white', command=self.click)

        self.dubbelCoins = Button(self.window,text='Double Coins',font='Arial 15 bold',
                                  borderwidth=0,
                                  activebackground='white',command=lambda: self.aankoop(self.DoubleCost))
        self.costdubbel=Label(self.window,text='Cost: '+str(self.DoubleCost),background='white',font='Arial 15 bold')

        self.shopScherm = Canvas(self.window, height=600, width=500, background='white')

        self.prijzen = {
            'snor': 5
            # Hier dus alle andere dingen die je kan kopen.
        }
        #####################################################################################################
        # KNOPPEN & LABELS
        self.snor = Button(image=self.snorcookie, command=lambda: self.aankoop(self.prijzen['snor']))
        # KNOPPEN & LABELS
        #####################################################################################################

    def plaatsen(self):
        self.cookie.place(x=100, y=125)
        self.shopKnop.place(x=400, y=500)
        self.dubbelCoins.place(x=50, y=500)

        self.balanceOnScreen.pack(pady=30)
        self.costdubbel.place(x=50,y=550)

        self.window.mainloop()

    def click(self):
        self.balance += self.coinsPerClick
        self.balanceOnScreen.configure(text=self.balance)

    def shop(self):
        self.shopScherm.pack()
        self.snor.place(x=90, y=200)

    def removing(self):
        self.makingSure.destroy()
        self.dubbelCoins.place(x=50, y=525)

    def aankoop(self, amountOfCoins):
        self.makingSure = Frame(self.window, highlightbackground="black", highlightthickness=5, height=200, width=250,
                                bg='white', bd=5)
        self.makingSure.place(y=150, x=150)

        notEnoughCoins = Label(self.makingSure, background='white',
                               text=f"You don't have enough coins to buy that.\n\nThis costs {amountOfCoins}")
        areYouSure = Label(self.makingSure, background='white', text='Are you sure you want to buy that?')


        ###############################################################################
        yes = Button(self.makingSure, text='Yes', bg='green', command=lambda: ifPressedYes())
        no = Button(self.makingSure, text='no', bg='red', command=self.removing)
        ok = Button(self.makingSure, text='ok', background='green', height=50, width=50,
                    command=self.removing)
        ###############################################################################

        if amountOfCoins==self.DoubleCost:
            self.dubbelCoins.destroy()

        if amountOfCoins <= self.balance:
            areYouSure.place(x=10, y=10)
            yes.place(x=50, y=100)
            no.place(x=150, y=100)

            def ifPressedYes():
                self.balance -= amountOfCoins
                self.coinsPerClick *= 2
                self.balanceOnScreen.configure(text=self.balance)
                self.makingSure.destroy()
                self.dubbelCoins.place(x=50,y=525)

        else:
            notEnoughCoins.place(x=10, y=10)
            ok.place(x=100, y=100, height=50, width=50)




clicker = CokkieBalzz()
clicker.plaatsen()
