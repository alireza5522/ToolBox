
import tkinter as tk

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        pass


root = tk.Tk()
root.title("برنامه To-Do List")


task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)


add_task_button = tk.Button(root, text="اضافه کردن وظیفه", command=add_task)
add_task_button.pack(pady=5)


tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.pack(pady=10)


delete_task_button = tk.Button(root, text="حذف وظیفه", command=delete_task)
delete_task_button.pack(pady=5)


root.mainloop()
