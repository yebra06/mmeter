#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk


class App(tk.Frame):

    def __init__(self, parent):
        """App constructor

        Initialize main gui frame and setup virp components.
        virp: voltage current resistance power
        """
        tk.Frame.__init__(self, parent)
        self.root = parent
        self.root.title('MMeter')
        self.init_gui()

    def init_gui(self):
        """Initialize widgets

        Set up gui widgets onto grid layout.
        """
        self.grid(column=0, row=0, sticky='nsew')

        # Error to be shown when user submits form with missing inputs.
        self.missing_input_err = tk.StringVar()
        self.error_missing_input_label = tk.Label(self, text='', anchor=tk.CENTER,
            textvariable=self.missing_input_err).grid(row=0, columnspan=2)

        # Create labels and place them on the grid.
        self.virp_labels = ('Voltage (V)', 'Current (I)', 'Resistance (R)', 'Power (P)')
        self.virp_entries = {label: tk.Entry(self) for label in self.virp_labels}
        for k, v in dict(enumerate(self.virp_labels, start=1)).items():
            tk.Label(self, text=v).grid(row=k+1)
            self.virp_entries[v].grid(row=k+1, column=1)

        # Calculate virp values from form entries.
        self.calc_btn = tk.Button(self, text='Calculate',
            command=self.calculate).grid(row=len(self.virp_labels)+2, column=0)

        # Clear form button.
        self.clear_btn = tk.Button(self, text='Clear',
            command=self.clear_form).grid(row=len(self.virp_labels)+2, column=1)

    def calculate(self):
        """Calculate equations from virp entries.

        Calculate given inputs and display errors if any. An error will occur
        if the user doesn't provide more than 1 values for Ohms law.
        """
        mul = lambda x, y: float(x) * float(y)
        div = lambda x, y: float(x) / float(y)

        # Get input values
        v, i, r, p = (self.virp_entries[lab].get() for lab in self.virp_labels)

        # Count number of form entries.
        input_counter = 0

        # Note: In python3, division is converted to float automagically.
        if v and i:
            p = mul(v, i)
            r = div(v, i)
            input_counter += 1
        elif v and r:
            p = div(float(v)**2, r)
            i = div(v, r)
            input_counter += 1
        elif v and p:
            i = div(p, v)
            r = div(v, i)
            input_counter += 1
        elif i and r:
            v = mul(i, r)
            p = mul(i, v)
            input_counter += 1
        elif i and p:
            v = div(p, i)
            r = div(v, i)
            input_counter += 1
        elif r and p:
            v = mul(i, r)
            i = div(i, r)
            input_counter += 1
        else:
            if input_counter > 1:
                self.missing_input_err.set('')
            else:
                self.missing_input_err.set('Please provide at least 2 values.')

        self.update_form(v, i, r, p)

    def update_form(self, v, i, r, p):
        """Update form

        Update form values based on user inputs. First, the existing entries
        are deleted and then updated.
        """
        self.virp_entries['Voltage (V)'].delete(0, tk.END)
        self.virp_entries['Voltage (V)'].insert(0, float(v))
        self.virp_entries['Current (I)'].delete(0, tk.END)
        self.virp_entries['Current (I)'].insert(0, float(i))
        self.virp_entries['Resistance (R)'].delete(0, tk.END)
        self.virp_entries['Resistance (R)'].insert(0, float(r))
        self.virp_entries['Power (P)'].delete(0, tk.END)
        self.virp_entries['Power (P)'].insert(0, float(p))

    def clear_form(self):
        """Clear form data

        Delete all existing entries in the form.
        """
        self.virp_entries['Voltage (V)'].delete(0, tk.END)
        self.virp_entries['Current (I)'].delete(0, tk.END)
        self.virp_entries['Resistance (R)'].delete(0, tk.END)
        self.virp_entries['Power (P)'].delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    App(root)
    root.mainloop()
