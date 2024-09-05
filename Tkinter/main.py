import tkinter as tk



root = tk.Tk()

root.geometry("600x500")
root.title("Nixor")


label = tk.Label(root, text="P2P Network", font=('Arial', 18))
label.pack(padx=20, pady=30)


textbox = tk.Text(root, height=2, font=('Arial', 16))
textbox.pack(padx=10)


button = tk.Button(root, text="pair", font=('Arial', 18))
button.pack(padx=5, pady=10)

btnframe = tk.Frame(root)
btnframe.columnconfigure(0, weight=1)
btnframe.columnconfigure(1, weight=1)
btnframe.columnconfigure(2, weight=1)

btn1 = tk.Button(btnframe, text='1', font=('Arial', 12))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(btnframe, text='2', font=('Arial', 12))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(btnframe, text='3', font=('Arial', 12))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4  = tk.Button(btnframe, text='4', font=('Arial', 12))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(btnframe, text='5', font=('Arial', 12))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(btnframe, text='6', font=('Arial', 12))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btnframe.pack(fill='x')

root.mainloop()