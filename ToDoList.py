import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()


def delete_task():
    selection_task = listbox.curselection()
    for task in reversed(selection_task):
        listbox.delete(task)
    save_tasks()

def save_tasks():
    
    tasks = listbox.get(0, tk.END)

    with open("Tasks.txt", "w") as fichier:
        for task in tasks:
            fichier.write(task + "\n")

def charger_tasks():
    try:
        with open("Tasks.txt", "r") as fichier:
            tasks = fichier.readlines()
        
        for task in tasks:
            listbox.insert(tk.END, task.strip())
    
    except FileNotFoundError:
        with open("Tasks.txt", "w"):
            pass


# Add and name a window
window = tk.Tk()
window.title(" My To Do List 🥰")

# Styles
window.geometry("500x600")
window.configure(bg="#f0f0f0")
window.option_add("*Font", "Arial 12")

frame = tk.Frame(window, bg="#008CBA")
frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)


# Creation of the List
listbox = tk.Listbox(window, width=40, height=20)
listbox.pack(pady=10)

entry = tk.Entry(window, width=30)
entry.pack(pady=5)


add_button = tk.Button(window, text="Add",bg="#008CBA", fg="#ffffff", relief=tk.RAISED, command=add_task)
add_button.pack(pady=5, fill=tk.X)

delete_button = tk.Button(window, text="Delete", bg="#FF5733", fg="#ffffff", relief=tk.RAISED, command=delete_task)
delete_button.pack(pady=5, fill=tk.X)

charger_tasks()

window.mainloop()
