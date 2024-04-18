import tkinter as tk
import time
from main import *

# تابع به‌روزرسانی زمان کرنومتر
def update_time():
    if running:
        global timer
        global time_text
        # محاسبه زمان گذشته
        timer = time.time() - start_time
        # نمایش زمان
        time_text.configure(text=f'{timer:.2f}')
        # به‌روزرسانی هر 10 میلی‌ثانیه
        cornometer.after(10, update_time)

# تابع شروع کرنومتر
def start():
    global running, start_time
    if not running:
        running = True
        start_time = time.time()
        update_time()

# تابع توقف کرنومتر
def stop():
    global running
    running = False

# تابع ریست کرنومتر
def reset():
    global timer
    global cornometer
    timer = 0
    cornometer.configure(text='0.00')

"""# ایجاد پنجره اصلی
window = tk.Tk()
window.title('کرنومتر')"""

# متغیرهای جهانی
running = False
start_time = None
timer = 0

# نمایش زمان
"""time_text = tk.Label(window, text='0.00', font=('Helvetica', 48))
time_text.pack()

# دکمه‌های کنترل
start_button = tk.Button(window, text='شروع', command=start)
start_button.pack(fill='x')

stop_button = tk.Button(window, text='توقف', command=stop)
stop_button.pack(fill='x')

reset_button = tk.Button(window, text='ریست', command=reset)
reset_button.pack(fill='x')"""

# اجرای پنجره
#window.mainloop()
