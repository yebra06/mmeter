from tkinter import *


class App(Frame):

    def __init__(self, master=None):
        """Initialize main gui frame.
        :param master: Main frame.
        """
        super().__init__(master)
        self.pack()

    def quit(self):
        """
        Exit gui application.
        """
        root.destroy()

if __name__ == '__main__':
    root = Tk()
    root.title('MMeter')
    root.geometry('500x500')
    app = App(master=root)
    app.mainloop()
