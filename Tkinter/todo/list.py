import tkinter as tk

# Save tasks to a file
def save(lst, filename):
    with open(filename, 'w') as f:
        for item in lst:
            f.write(f"{item}\n")

# Load tasks from a file
def load(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

# Function to handle saving tasks
def save_task():
    task = textbox.get("1.0", tk.END).strip()
    if task:
        tasks.append(task)
        save(tasks, 'pylist.txt')
        textbox1.insert(tk.END, task + "\n")
        textbox.delete("1.0", tk.END)

def main():
    global textbox, textbox1, tasks

    root = tk.Tk()
    root.title("Todo App")

    # Load tasks from file
    tasks = load('pylist.txt')

    label = tk.Label(root, text="Save your Tasks", font=('Arial', 18))
    label.pack(padx=20, pady=30)

    textbox = tk.Text(root, height=2, font=('Arial', 12))
    textbox.pack(padx=20, pady=10)

    btnsave = tk.Button(root, text="Save", font=('Arial', 13), command=save_task)
    btnsave.pack(padx=10)

    textbox1 = tk.Text(root, height=20, font=('Arial', 13))
    textbox1.pack(padx=20, pady=30)

    # Display previously saved tasks
    for task in tasks:
        textbox1.insert(tk.END, task + "\n")

    root.mainloop()

if __name__ == '__main__':
    main()


