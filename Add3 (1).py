import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task before adding!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def update_task():
    try:
        selected = listbox.curselection()[0]
        new_task = entry.get()
        if new_task:
            tasks[selected] = new_task
            update_listbox()
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter updated task text!")
    except:
        messagebox.showwarning("Warning", "Select a task to update!")

# Entry field
entry = tk.Entry(root, font="lucida 15")
entry.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", width=15, command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", width=15, command=delete_task).pack(pady=5)
tk.Button(root, text="Update Task", width=15, command=update_task).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, font="lucida 13", width=40, height=10)
listbox.pack(pady=10)

root.mainloop()
