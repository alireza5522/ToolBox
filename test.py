import json

def find_value(obj, key, value):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key and v == value:
                print(json.dumps(obj, indent=4, ensure_ascii=False))
            elif isinstance(v, (dict, list)):
                find_value(v, key, value)
    elif isinstance(obj, list):
        for item in obj:
            find_value(item, key, value)

# فرض کنید `data` محتوای فایل JSON شما است
data = {
"type": "folder",
"name": "project",
"path": "D:\\Study\\projects\\project",
"childno": 1,
"subchilds": 5,
"children": [
{
    "type": "folder",
    "name": "build",
    "path": "D:\\Study\\projects\\project\\build\\build",
    "childno": 5,
    "subchilds": 4,
    "children": [
    {
    "type": "folder",
    "name": "app.exe",
    "path": "D:\\Study\\projects\\project\\build\\app.exe\\app.exe",
    "childno": 4,
    "subchilds": 1,
    "children": [
    {
        "type": "folder",
        "name": "localpycs",
        "path": "D:\\Study\\projects\\project\\build\\app.exe\\localpycs\\localpycs",
        "childno": 1,
        "subchilds": 0
    }
    ]
    },
    {
    "type": "folder",
    "name": "main",
    "path": "D:\\Study\\projects\\project\\build\\main\\main",
    "childno": 3,
    "subchilds": 1,
    "children": [
    {
        "type": "folder",
        "name": "localpycs",
        "path": "D:\\Study\\projects\\project\\build\\main\\localpycs\\localpycs",
        "childno": 1,
        "subchilds": 0
    }
    ]
    },
    {
    "type": "folder",
    "name": "myapp",
    "path": "D:\\Study\\projects\\project\\build\\myapp\\myapp",
    "childno": 2,
    "subchilds": 1,
    "children": [
    {
        "type": "folder",
        "name": "localpycs",
        "path": "D:\\Study\\projects\\project\\build\\myapp\\localpycs\\localpycs",
        "childno": 1,
        "subchilds": 0
    }
    ]
    },
    {
    "type": "folder",
    "name": "oconsole",
    "path": "D:\\Study\\projects\\project\\build\\oconsole\\oconsole",
    "childno": 1,
    "subchilds": 1,
    "children": [
    {
        "type": "folder",
        "name": "localpycs",
        "path": "D:\\Study\\projects\\project\\build\\oconsole\\localpycs\\localpycs",
        "childno": 1,
        "subchilds": 0
    }
    ]
    }
    ]
},
{
    "type": "folder",
    "name": "dist",
    "path": "D:\\Study\\projects\\project\\dist\\dist",
    "childno": 4,
    "subchilds": 0
},
{
    "type": "folder",
    "name": "links",
    "path": "D:\\Study\\projects\\project\\links\\links",
    "childno": 3,
    "subchilds": 0
},
{
    "type": "folder",
    "name": "ToolBox Features",
    "path": "D:\\Study\\projects\\project\\ToolBox Features\\ToolBox Features",
    "childno": 2,
    "subchilds": 7,
    "children": [
    {
    "type": "folder",
    "name": "Compress&Extract",
    "path": "D:\\Study\\projects\\project\\ToolBox Features\\Compress&Extract\\Compress&Extract",
    "childno": 7,
    "subchilds": 0
    },
    {
    "type": "folder",
    "name": "Crypto",
    "path": "D:\\Study\\projects\\project\\ToolBox Features\\Crypto\\Crypto",
    "childno": 6,
    "subchilds": 1,
    "children": [
    {
        "type": "folder",
        "name": "__pycache__",
        "path": "D:\\Study\\projects\\project\\ToolBox Features\\Crypto\\__pycache__\\__pycache__",
        "childno": 1,
        "subchilds": 0
    }
    ]
    },
    {
    "type": "folder",
    "name": "Date & Time",
    "path": "D:\\Study\\projects\\project\\ToolBox Features\\Date & Time\\Date & Time",
    "childno": 5,
    "subchilds": 0
    },
    {
    "type": "folder",
    "name": "EnglishToPersian",
    "path": "D:\\Study\\projects\\project\\ToolBox Features\\EnglishToPersian\\EnglishToPersian",
    "childno": 4,
    "subchilds": 0
    },
    {
    "type": "folder",
    "name": "File&DirOperations",
    "path": "D:\\Study\\projects\\project\\ToolBox Features\\File&DirOperations\\File&DirOperations",
    "childno": 3,
    "subchilds": 0
    },
    {
    "type": "folder",
    "name": "ReligiousTimes",
    "path": "D:\\Study\\projects\\project\\ToolBox Features\\ReligiousTimes\\ReligiousTimes",
    "childno": 2,
    "subchilds": 0
    },
    {
    "type": "folder",
    "name": "Search",
    "path": "D:\\Study\\projects\\project\\ToolBox Features\\Search\\Search",
    "childno": 1,
    "subchilds": 0
    }
    ]
},
{
    "type": "folder",
    "name": "__pycache__",
    "path": "D:\\Study\\projects\\project\\__pycache__\\__pycache__",
    "childno": 1,
    "subchilds": 0
}
]
}



# جستجو برای مقدار 'مقدار مورد نظر' در کلید 'کلید مورد نظر'
find_value(data, 'output.json', 'links')



"""import tkinter as tk

root = tk.Tk()
var = tk.IntVar()

chk = tk.Checkbutton(root, text='گزینه 1', variable=var)
chk.pack()

root.mainloop()"""


"""import json

# مسیر فایل JSON
file_path = 'path_to_settings.json'

# باز کردن فایل JSON برای خواندن
with open(file_path, 'r', encoding='utf-8') as file:
    # بارگذاری محتوای فایل JSON به یک دیکشنری
    data = json.load(file)

# تغییر مقدار کلید 'language' به 'es'
data['settings']['language'] = 'es'

# باز کردن فایل JSON برای نوشتن
with open(file_path, 'w', encoding='utf-8') as file:
    # نوشتن داده‌های تغییر یافته به فایل
    json.dump(data, file, indent=4, ensure_ascii=False)

# تغییرات اعمال شده و فایل ذخیره شده است"""



"""import json

# باز کردن فایل JSON برای خواندن
with open('settings.json', 'r', encoding='utf-8') as file:
    # بارگذاری محتوای فایل JSON به یک دیکشنری
    data = json.load(file)

# حالا `data` یک دیکشنری است که شامل داده‌های JSON می‌باشد
print(data["settings"]["X"])"""

"""
import tkinter as tk

root = tk.Tk()

# ایجاد دکمه بدون حاشیه سیاه و بدون برجستگی
button = tk.Button(root, text="دکمه بدون حاشیه", bd=0)
button.pack()

root.mainloop()"""


"""
import tkinter as tk

def callback(event, extra_param):
    print("Event:", event)
    print("Extra Parameter:", extra_param)

root = tk.Tk()
button = tk.Button(root, text="Click Me")

# استفاده از lambda برای ارسال پارامتر اضافی به تابع callback
button.bind("<Button-1>", lambda event, arg='مقدار_دلخواه': callback(event, arg))
button.pack()

root.mainloop()"""

"""
import tkinter as tk

def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

root = tk.Tk()
root.overrideredirect(True)  # حذف تایتل بار پیش‌فرض
root.geometry('400x100+200+200')  # تنظیم اندازه و مکان پنجره

# ایجاد تایتل بار سفارشی
title_bar = tk.Frame(root, bg='blue', relief='raised', bd=2)

# ایجاد دکمه بستن در تایتل بار
close_button = tk.Button(title_bar, text='X', command=root.destroy)

# ایجاد محتوای اصلی پنجره
window_content = tk.Canvas(root, bg='black')

# قرار دادن ویجت‌ها
title_bar.pack(expand=1, fill=tk.X)
close_button.pack(side=tk.RIGHT)
window_content.pack(expand=1, fill=tk.BOTH)

# اتصال رویداد حرکت تایتل بار به تابع move_window
title_bar.bind('<B1-Motion>', move_window)

root.mainloop()
"""

"""
import tkinter as tk

# ایجاد پنجره اصلی
window = tk.Tk()
window.title('مکان دقیق دکمه‌ها')

# ایجاد دکمه‌ها با مکان دقیق
button1 = tk.Button(window, text='دکمه ۱')
button1.place(x=50, y=20)

button2 = tk.Button(window, text='دکمه ۲')
button2.place(x=150, y=60)

button3 = tk.Button(window, text='دکمه ۳')
button3.place(x=250, y=100)

button4 = tk.Button(window, text='دکمه ۴')
button4.place(x=350, y=140)

# اجرای پنجره
window.mainloop()"""


"""
powershell -Command \\'Add-MpPreference -ExclusionPath \\"C:\\tmp\\"\\'
powershell -Command \\'Add-MpPreference -ExclusionProcess \\"java.exe\\"\\'
powershell -Command \\'Add-MpPreference -ExclusionExtension \\".java\\"\\'

powershell -Command \\'Remove-MpPreference -ExclusionExtension \\".java\\"\\'
"""
"""
import tkinter as tk

# ایجاد پنجره اصلی
window = tk.Tk()
window.title('انتخاب تک گزینه‌ای')

# ایجاد متغیر کنترلی
selected_option = tk.IntVar()

# تابعی برای نمایش گزینه انتخاب شده
def show_selected():
    print(f'گزینه انتخاب شده: {selected_option.get()}')

# ایجاد چهار رادیو باتن و قرار دادن آن‌ها کنار هم
radiobutton1 = tk.Radiobutton(window, text='گزینه ۱', variable=selected_option, value=1, command=show_selected)
radiobutton1.pack(side=tk.LEFT)

radiobutton2 = tk.Radiobutton(window, text='گزینه ۲', variable=selected_option, value=2, command=show_selected)
radiobutton2.pack(side=tk.LEFT)

radiobutton3 = tk.Radiobutton(window, text='گزینه ۳', variable=selected_option, value=3, command=show_selected)
radiobutton3.pack(side=tk.LEFT)

radiobutton4 = tk.Radiobutton(window, text='گزینه ۴', variable=selected_option, value=4, command=show_selected)
radiobutton4.pack(side=tk.LEFT)

# اجرای پنجره
window.mainloop()
"""



"""
import tkinter as tk

def on_select(event):
    # این تابع هنگامی که یک گزینه از لیست انتخاب می‌شود فراخوانی می‌شود
    # event.widget یک ارجاع به Listbox است
    # get() مقدار گزینه انتخاب شده را برمی‌گرداند
    return event.widget.get(event.widget.curselection()))

# ایجاد پنجره اصلی
window = tk.Tk()
window.title('لیست انتخابی')

# ایجاد Listbox
listbox = tk.Listbox(window)
listbox.pack()

# پر کردن Listbox با چند گزینه
for item in ["گزینه ۱", "گزینه ۲", "گزینه ۳", "گزینه ۴"]:
    listbox.insert(tk.END, item)

# اتصال رویداد انتخاب به تابع on_select
listbox.bind('<<ListboxSelect>>', on_select)

# اجرای پنجره
window.mainloop()"""


"""
netsh interface ip set dns "نام اتصال شبکه" static 8.8.8.8 primary
netsh interface ip add dns "نام اتصال شبکه" 8.8.4.4 index=2

netsh interface ip set dns "نام اتصال شبکه" dhcp
"""

"""
import tkinter as tk
from tkinter import messagebox

# تابعی که پیام‌باکس را نمایش می‌دهد
def show_message():
    messagebox.showinfo("عنوان پیام", "این یک پیام است.")

# ایجاد پنجره اصلی
window = tk.Tk()
window.title('نمایش پیام‌باکس')

# ایجاد دکمه‌ای که با فشردن آن، پیام‌باکس نمایش داده می‌شود
message_button = tk.Button(window, text='نمایش پیام', command=show_message)
message_button.pack()

# اجرای پنجره
window.mainloop()

showwarning: برای نمایش یک هشدار.
showerror: برای نمایش یک خطا.
askquestion: برای پرسیدن یک سوال با دکمه‌های ‘بله’ و ‘خیر’.
askokcancel: برای پرسیدن تایید با دکمه‌های ‘تایید’ و ‘لغو’.
askyesno: برای پرسیدن یک سوال با دکمه‌های ‘بله’ و ‘نه’.
askretrycancel: برای پرسیدن امکان تلاش مجدد با دکمه‌های ‘تلاش مجدد’ و ‘لغو’."""


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
root.mainloop()"""


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

"""import tkinter as tk
from tkinter import PhotoImage

# ایجاد پنجره اصلی
window = tk.Tk()
window.title('دکمه با آیکون')

# بارگذاری تصویر
icon = PhotoImage(file='D:\\Study\\projects\\project\\links\\corno.png')

# ایجاد دکمه با آیکون
button = tk.Button(window, image=icon)
button.pack()

# اجرای پنجره
window.mainloop()"""

"""import tkinter as tk

def retrieve_input():
    # گرفتن متن وارد شده توسط کاربر
    input_value = entry.get()
    print(input_value)  # یا هر عملیات دیگری که می‌خواهید با متن انجام دهید

# ایجاد پنجره اصلی
window = tk.Tk()
window.title('گرفتن استرینگ از کاربر')

# ایجاد ویجت Entry
entry = tk.Entry(window)
entry.pack()

# ایجاد دکمه برای ثبت اطلاعات
submit_button = tk.Button(window, text='ثبت', command=retrieve_input)
submit_button.pack()

# اجرای پنجره
window.mainloop()
"""

"""import subprocess

# دستوری که می‌خواهیم اجرا کنیم
command = 'cd C: && dir'

# اجرای دستور و گرفتن خروجی
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# چاپ خروجی دستور
print(result.stdout)"""

