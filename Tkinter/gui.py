
import tkinter as tk
from tkinter import messagebox


class gui:


    def __init__(self):
        self.root = tk.Tk()


        self.label = tk.Label(self.root, text="Compiled Successful✨", font=('Arial', 18))
        self.label.pack(padx=10, pady=20)


        self.textbox = tk.Text(self.root, height=5, font=('Arial', 15) )
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="compile", font=('Arial', 15), variable=self.check_state)
        self.check.pack(padx=10, pady=10)


        self.button = tk.Button(self.root, text='process', font=('Arial', 15), command=self.process)
        self.button.pack(padx=10, pady=15)

        self.root.mainloop()


    def process(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))


gui()