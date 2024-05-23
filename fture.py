"""
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


root.mainloop()"""
"""
from cryptography.fernet import Fernet

# تولید کلید رمزنگاری
key = Fernet.generate_key()

# ایجاد یک نمونه از کلاس Fernet با کلید
fernet = Fernet(key)

# رمزنگاری رشته
plaintext = "Hello, world!"
ciphertext = fernet.encrypt(plaintext.encode())

# رمزگشایی رشته
decrypted_text = fernet.decrypt(ciphertext).decode()
print(ciphertext,decrypted_text)"""

"""import os
from zipfile import ZipFile

def zip_directory(directory_path, output_zip_path):

    with ZipFile(output_zip_path, 'w') as zipf:
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory_path)
                zipf.write(file_path, arcname=arcname)

# Example usage:
directory_to_zip = input()
output_zip_file = input()
n = directory_to_zip.split("\\")
output_zip_file += "\\"+n[-1]+".zip"
print(directory_to_zip,output_zip_file)
zip_directory(directory_to_zip, output_zip_file)
print(f"Directory '{directory_to_zip}' has been zipped to '{output_zip_file}'.")"""

import tkinter as tk

def close_window():
    global is_window_open
    is_window_open = False
    root.destroy()

def check_window_status():
    if is_window_open:
        print("The window is open.")
    else:
        print("The window is closed.")

root = tk.Tk()
root.title("Check Window Status")
root.geometry("300x200")

is_window_open = True

close_button = tk.Button(root, text="Close Window", command=close_window)
close_button.pack()

check_button = tk.Button(root, text="Check Status", command=check_window_status)
check_button.pack()

root.mainloop()


