from tkinter import *


class App(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

    def quit(self):
        root.destroy()

if __name__ == '__main__':
    root = Tk()
    root.title('MMeter')
    root.geometry('500x500')
    app = App(master=root)
    app.mainloop()
