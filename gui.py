# tkinter qt...
from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.helloLabel = Label(self, text='hello world')
        self.helloLabel.pack()
        self.quitBtn = Button(self, text='quit', command=self.quit)
        self.quitBtn.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.helloBtn = Button(self, text='hello', command=self.hello)
        self.helloBtn.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','hello %s'% name)


app = Application()
app.master.title('hello world')
app.mainloop()