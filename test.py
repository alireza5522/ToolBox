"""import tkinter as tk

class ToolTip(object):
    def __init__(self, widget, text='Tooltip'):
        self.widget = widget
        self.text = text
        self.widget.bind('<Enter>', self.enter)
        self.widget.bind('<Leave>', self.leave)
        self.tw = None

    def enter(self, event=None):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # ایجاد پنجره تولتیپ
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, background='yellow', relief='solid', borderwidth=1,
                         font=("arial", "8", "normal"))
        label.pack(ipadx=1)

    def leave(self, event=None):
        if self.tw:
            self.tw.destroy()
            self.tw = None

# استفاده از کلاس تولتیپ
root = tk.Tk()
btn = tk.Button(root, text="نمونه دکمه")
btn.pack(padx=10, pady=5)
ToolTip(btn, 'این دکمه یک نمونه است')
root.mainloop()
"""

"""import threading
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(1)
        print(i)

# ایجاد ترد
thread = threading.Thread(target=print_numbers)

# شروع ترد
thread.start()

# انتظار برای پایان ترد
thread.join()

print("ترد به پایان رسید.")"""

"""import tkinter as tk

# تابعی که می‌خواهیم اجرا کنیم
def greet(name):
    print(f'سلام {name}!')

# ایجاد پنجره اصلی
window = tk.Tk()
window.title('نمونه دکمه با پارامتر')

# ایجاد دکمه که تابع greet را با پارامتر 'جهان' فراخوانی می‌کند
button = tk.Button(window, text='سلام بگو', command=lambda: greet('جهان'))
button.pack()

# اجرای پنجره
window.mainloop()"""

import tkinter as tk
from tkinter import PhotoImage

# ایجاد پنجره اصلی
window = tk.Tk()
window.title('دکمه با آیکون')

# بارگذاری تصویر
icon = PhotoImage(file='D:\Study\projects\project\links\corno.png')

# ایجاد دکمه با آیکون
button = tk.Button(window, image=icon)
button.pack()

# اجرای پنجره
window.mainloop()

