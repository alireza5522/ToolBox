import tkinter as tk
from tkinter import Toplevel
import threading
import time

x0,y0 = 10,10
W1,H1 = 50,200
X1,Y1= 10,10
running = False
start_time = None
timer = 0
time_text = None

def start_move(event):
    global x, y
    x = event.x
    y = event.y

def stop_move(event):
    global x, y
    global x0, y0
    global X, Y
    #root.winfo_screenwidth()
    if root.winfo_x() <= 30:
        x0=0
    elif root.winfo_x() >= root.winfo_screenwidth()-30-W:
        x0=root.winfo_screenwidth()-W

    if root.winfo_y() <= 30:
        y0=0
    X,Y = x0,y0
    root.geometry(f"+{x0}+{y0}")
    x = None
    y = None

def on_move(event):
    global x, y
    global x0, y0
    deltax = event.x - x
    deltay = event.y - y
    x0 = root.winfo_x() + deltax
    y0 = root.winfo_y() + deltay
    root.geometry(f"+{x0}+{y0}")

def open_new_window():
    global W,H,X,Y
    global W1,H1,X1,Y1
    new_window = Toplevel(root)
    #new_window.overrideredirect(True)
    #new_window.resizable(True, True)
    new_window.wm_attributes("-toolwindow", "true")
    W1,H1 = 50,200
    X1,Y1= X+W,Y+(H//2)-(H1//2)
    if Y1 < 0:
        Y1 = 0
    
    if (Y1+H1) > new_window.winfo_screenheight():
        Y1 = new_window.winfo_screenheight()-H1

    if X >= new_window.winfo_screenwidth()/2:
        X1,Y1= (X-W1),Y+(H//2)-(H1//2)
    else:
        X1,Y1= X+W,Y+(H//2)-(H1//2)

    new_window.geometry(f"{W1}x{H1}+{X1}+{Y1}")
    openbutton = tk.Button(new_window, 
                       text=txt, 
                       command=cornometerwindow,
                       width=10,
                       height=10,
                       relief='flat', 
                       highlightthickness=0, 
                       activebackground="lightgray", 
                       activeforeground="black",
                       bg="lightgray",
                       fg="black")
    openbutton.pack(side=tk.BOTTOM, fill=tk.X)


def cornometerwindow():
    global running,start_time,timer
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
        global time_text
        timer = 0
        time_text.configure(text='0.00')

    global W,H,X,Y
    global W1,H1,X1,Y1
    cornometer = Toplevel(root)
    #cornometer.overrideredirect(True)
    #cornometer.resizable(True, True)
    cornometer.wm_attributes("-toolwindow", "true")
    Wc,Hc = 500,200
    Xc,Yc= X+W,Y+(H//2)-(H1//2)
    if Yc < 0:
        Yc = 0
    
    if (Yc+H1) > cornometer.winfo_screenheight():
        Yc = cornometer.winfo_screenheight()-H1

    if X >= cornometer.winfo_screenwidth()/2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W1,Y+(H//2)-(Hc//2)

    global time_text

    # نمایش زمان
    time_text = tk.Label(cornometer, text='0.00', font=('Helvetica', 48))
    time_text.pack()

    # دکمه‌های کنترل
    start_button = tk.Button(cornometer, text='شروع',command=start)
    start_button.pack(fill='x')

    stop_button = tk.Button(cornometer, text='توقف',command=stop)
    stop_button.pack(fill='x')

    reset_button = tk.Button(cornometer, text='ریست',command=reset)
    reset_button.pack(fill='x')
    
    cornometer.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

root = tk.Tk()
W,H,X,Y=20,78,100,100
root.geometry(f"{W}x{H}+{X}+{Y}") #20x78
root.overrideredirect(True)
#root.resizable(False, False)
root.title("^^")
root.wm_attributes("-toolwindow", "true")
if X >= (root.winfo_screenwidth()/2):
    txt = "<<"
else:
    txt = ">>"

openbutton = tk.Button(root, 
                       text=txt, 
                       command=open_new_window,
                       width=2,
                       height=4,
                       relief='flat', 
                       highlightthickness=0, 
                       activebackground="lightgray", 
                       activeforeground="black",
                       bg="lightgray",
                       fg="black")
openbutton.pack(side=tk.BOTTOM, fill=tk.X)

move_button = tk.Button(root, 
                        text="", 
                        width=2, 
                        height=1,
                        relief='flat', 
                        highlightthickness=0, 
                        activebackground="white", 
                        activeforeground="black", 
                        bg="white", 
                        fg="black")
move_button.pack(side=tk.BOTTOM, fill=tk.X)
move_button.bind('<ButtonPress-1>', start_move)
move_button.bind('<ButtonRelease-1>', stop_move)
move_button.bind('<B1-Motion>', on_move)

root.mainloop()
