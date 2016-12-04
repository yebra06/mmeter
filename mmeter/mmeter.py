from tkinter import *


class App(Frame):

    def __init__(self, master=None):
        """App constructor

        Initialize main gui frame and setup virp components.
        virp = voltage current resistance power.
        """
        super().__init__(master)
        self.virp_labels = ('Voltage (V)', 'Current (I)', 'Resistance (R)', 'Power (P)')
        self.virp_entries = {label: Entry(self) for label in self.virp_labels}
        self.create_menu()
        self.create_calculator()
        self.pack()

    def create_menu(self):
        """Create main menu

        Using Menu component, create a main menu bar and add
        Button components to each Menu.
        """
        main_menu = Menu(self.master)
        self.master.config(menu=main_menu)

        # Create file menu bar option.
        file = Menu(main_menu)
        file.add_command(label='Exit', command=self.quit)
        main_menu.add_cascade(label='File', menu=file)
        Button(self, text='Quit', command=self.quit)

        # Create edit option.
        edit = Menu(main_menu)
        main_menu.add_cascade(label='Edit', menu=edit)

    def create_calculator(self):
        """Create calculator module

        Create Entry components with corresponding Label from list
        of labels and retrieve user input. Send a dict of user input
        values to Calculator to calculate ohms and kirchoffs laws.
        """
        for k, v in dict(enumerate(self.virp_labels, start=1)).items():
            Label(self, text=v, padx=5, pady=5).grid(row=k)
            self.virp_entries[v].grid(row=k, column=1)

        # Button to calculate given entries.
        Button(self, text='Calculate',
            command=self.calculate
        ).grid(row=len(self.virp_labels)+1, column=1)

    def calculate(self):
        """Calculate equations."""
        v, i, r, p = (
            self.virp_entries[lab].get() for lab in self.virp_labels
        )

    def quit(self):
        root.destroy()


if __name__ == '__main__':
    root = Tk()
    root.title('MMeter')
    root.geometry('500x500')
    app = App(master=root)
    app.mainloop()
