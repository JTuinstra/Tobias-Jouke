from tkinter import *


class CokkieBalzz:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x700')
        self.window.configure(background='white')
        self.window.title('Cockieball')

        self.coinsPerClick = 1
        self.balance = 0

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

    def plaatsen(self):
        self.cookie.place(x=100, y=125)
        self.shopKnop.place(x=400, y=500)

        self.balanceOnScreen.pack(pady=30)

        self.window.mainloop()

    def click(self):
        self.balance += self.coinsPerClick
        self.balanceOnScreen.configure(text=self.balance)

    def shop(self):
        self.shopScherm = Canvas(self.window, height=600, width=500, background='white')
        self.shopScherm.pack()


clicker = CokkieBalzz()
clicker.plaatsen()
