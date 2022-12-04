from tkinter import *


class CokkieBalzz:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x700')
        self.window.configure(background='white')
        self.window.title('Cockieball')

        self.coinsPerClick = 1
        self.balance = 0

        self.image = PhotoImage(file='C:\\Users\\jouke\\Downloads\\cookie.png')
        self.balanceOnScreen=Label(self.window,text=self.balance,background='white',font='Arial 30 bold')

        self.cookie = Button(self.window,
                             image=self.image,
                             background='white',
                             borderwidth=0,
                             activebackground='white',command=self.click)


    def plaatsen(self):
        self.cookie.place(x=100, y=125)
        self.balanceOnScreen.pack(pady=30)
        self.window.mainloop()

    def click(self):
        self.balance+=self.coinsPerClick
        self.balanceOnScreen.configure(text=self.balance)



clicker = CokkieBalzz()
clicker.plaatsen()
