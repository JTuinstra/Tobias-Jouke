from tkinter import *


class CokkieBalzz:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x700')
        self.window.configure(background='white')
        self.window.title('Cockieball')

        self.coinsPerClick = 1
        self.balance = 0
        self.winkelItems = {'item1': '$24,99',
                            'item2': 'Item2',
                            'item3': 'Item3',
                            'item4': 'Item4', }

        self.cookieImage = PhotoImage(file='C:\\Users\\jouke\\Downloads\\cookie.png')
        self.shopicon = PhotoImage(file='C:\\Users\\jouke\\Downloads\\shopicon.png')

        self.balanceOnScreen = Label(self.window,  # <----Geld boven scherm
                                     text=self.balance,
                                     background='white',
                                     font='Arial 30 bold')

        self.shopKnop = Button(self.window,
                               image=self.shopicon,
                               borderwidth=0,
                               background='gray', command=self.shop)

        self.cookie = Button(self.window,
                             image=self.cookieImage,
                             background='white',
                             borderwidth=0,
                             activebackground='white', command=self.click)

        #####################################################################################################
        self.shopScherm = Canvas(self.window, height=600, width=500, background='white')

        self.itemLabel1 = Label(self.window, text=self.winkelItems['item1'], font='Arial 18 bold')
        self.itemLabel2 = Label(self.window, text=self.winkelItems['item2'], font='Arial 18 bold')
        self.itemLabel3 = Label(self.window, text=self.winkelItems['item3'], font='Arial 18 bold')
        self.itemLabel4 = Label(self.window, text=self.winkelItems['item4'], font='Arial 18 bold')

        self.item1 = Button(self.window, text=self.winkelItems['item1'], font='Arial 18 bold',
                            command=lambda: self.extraction(5))

        self.item2 = Button(self.window, text=self.winkelItems['item2'], font='Arial 18 bold',
                            command=lambda: self.extraction(500))

        self.item3 = Button(self.window, text=self.winkelItems['item3'], font='Arial 18 bold',
                            command=lambda: self.extraction(1500))

        self.item4 = Button(self.window, text=self.winkelItems['item4'], font='Arial 18 bold',
                            command=lambda: self.extraction(5000))
        #####################################################################################################

    def plaatsen(self):
        self.cookie.place(x=100, y=125)
        self.shopKnop.place(x=400, y=500)

        self.balanceOnScreen.pack(pady=30)

        self.window.mainloop()

    def click(self):
        self.balance += self.coinsPerClick
        self.balanceOnScreen.configure(text=self.balance)

    def extraction(self, usage):
        self.balance-=usage
        self.balanceOnScreen.configure(text=self.balance)

    def shop(self):
        self.shopScherm.pack()

        self.itemLabel1.place(x=60, y=300)
        self.itemLabel2.place(x=375, y=300)
        self.itemLabel3.place(x=60, y=500)
        self.itemLabel4.place(x=375, y=500)

        ##########################################
        if self.balance >= 5:
            self.item1.place(x=60, y=300)

        elif self.balance >= 500:
            self.item2.place(x=375, y=300)

        elif self.balance >= 1500:
            self.item3.place(x=60, y=500)

        elif self.balance >= 5000:
            self.item4.place(x=375, y=500)


clicker = CokkieBalzz()
clicker.plaatsen()
