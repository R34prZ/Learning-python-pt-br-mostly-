from tkinter import *

class Application:
    def __init__(self, master=None):

        self.font = ("Arial", "12")

        self.frame1 = Frame(master, pady=20)
        self.frame2 = Frame(master, padx=20)
        self.frame3 = Frame(master, padx=20)
        self.frame4 = Frame(master, padx=20)
        self.frame5 = Frame(master, padx=20)
        self.frame6 = Frame(master, padx=20)

        self.label = Label(self.frame1, text='Jumbeerphone v1.2atualizado re-master atualizado', fg='green')
        self.entry = Entry(master, font=self.font )
        self.btn1 = Button(self.frame2, text='=')
        self.btn2 = Button(self.frame2, text='^-^')
        self.btn3 = Button(self.frame2, text='=')
        self.jumbeercasa = Label(self.frame3, text='Jumbeer casa')
        self.btn4 = Button(self.frame3, text='^', bg='azure', fg='green')
        self.jumbeercasasegurança = Label(self.frame4, text='|=|=|=|=|=|=|=|=|=|=|=|=|=|', fg='brown')
        self.jumbeerprogramações = Label(self.frame5, text='₢ Jumbeer programações 2020', bg='black', fg='azure')
        self.créditos = Label(self.frame5, text='R34perZ c3if4d0rZ produções e programações')

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        self.label.pack()
        self.entry.pack()

        self.btn1.pack(side='left')
        self.btn2.pack(side='top')
        self.btn3.pack(side='right')
        self.jumbeercasa.pack(side='right')
        self.jumbeercasasegurança.pack()
        self.btn4.pack(side='left')
        self.jumbeerprogramações.pack()
        self.créditos.pack()

root = Tk()
root.title('Jumbeerphone v1.2')
Application(root)
root.mainloop()