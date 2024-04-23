import time
import threading
import tkinter as tk
from tkinter import Toplevel
from tkinter import PhotoImage
import subprocess
from tkinter import messagebox

root = tk.Tk()

x0,y0 = 10,10
W1,H1 = 50,200
X1,Y1= 10,10
running = False
start_time = None
timer = 0
time_text = None

class coordinates:
    Main_Window_H,Main_Window_W = (50,250)
    cornometer_button_x,cornometer_button_y = (0,25)
    startup_button_x,startup_button_y = (0,75)
    dns_button_x,dns_button_y = (0,125)
    antivirus_button_x,antivirus_button_y = (0,175)

    cornometer_H,cornometer_W = (500,200)
    time_text_x,time_text_y = (100,10)
    start_button_x,start_button_y = (100,100)
    stop_button_x,stop_button_y = (100,125)
    reset_button_x,reset_button_y = (100,150)

    startup_W,startup_H = (250,250)
    startup_label1_x,startup_label1_y = (10,20)
    startup_entry1_x,startup_entry1_y = (10,50)
    startup_label2_x,startup_label2_y = (10,100)
    startup_entry2_x,startup_entry2_y = (10,125)
    startup_submit_x,startup_submit_y = (10,150)
    
    dns_W,dns_H = (250,250)
    dns_label1_x,dns_label1_y = (10,20)
    dns_entry1_x,dns_entry1_y = (10,50)
    dns_label2_x,dns_label2_y = (10,100)
    dns_entry2_x,dns_entry2_y = (10,125)
    dns_label3_x,dns_label3_y = (10,100)
    dns_entry3_x,dns_entry3_y = (10,125)
    dns_submit1_x,dns_submit1_y = (10,150)
    dns_submit2_x,dns_submit2_y = (10,175)

    antivirus_W,antivirus_H = (250,250)
    antivirus_label1_x,antivirus_label1_y = (10,20)
    antivirus_entry1_x,antivirus_entry1_y = (10,50)
    antivirus_label2_x,antivirus_label2_y = (10,100)
    antivirus_entry2_x,antivirus_entry2_y = (10,125)
    antivirus_button1_x,antivirus_button1_y = (10,150)
    antivirus_button2_x,antivirus_button2_y = (50,150)
    antivirus_button3_x,antivirus_button3_y = (100,150)
    antivirus_submit_x,antivirus_submit_y = (10,175)



class theme:
    titlebar = "yellow"
    window_bg = "white"
    activebackground = "lightgray"
    activeforeground = "black"
    bg = "lightgray"
    fg = "black"
    entrybg = "white"
    cornometer_icon = PhotoImage(file='D:\\Study\\projects\\project\\links\\corno50.png')
    startup_icon = PhotoImage(file='D:\\Study\\projects\\project\\links\\startup.png')
    def __init__(self,titlebar,
                 window_bg,
                 activebackground,
                 activeforeground,
                 bg,
                 fg,
                 entrybg,
                 cornometer_icon,
                 startup_icon):
       self.titlebar = titlebar
       self.window_bg = window_bg
       self.activebackground = activebackground
       self.activeforeground = activeforeground
       self.bg = bg
       self.fg = fg
       self.entrybg = entrybg
       self.cornometer_icon = cornometer_icon
       self.startup_icon = startup_icon
dark=theme(
    titlebar = "#363A36",
    window_bg = "#191B19",
    activebackground = "#363A36",
    activeforeground = "#C0C4C4",
    bg = "#363A36",
    fg = "#C0C4C4",
    entrybg = "#363A36",
    cornometer_icon = PhotoImage(file='D:\\Study\\projects\\project\\links\\corno50.png'),
    startup_icon = PhotoImage(file='D:\\Study\\projects\\project\\links\\startup.png')
)
light=theme(
    titlebar = "#EEEEEE",
    window_bg = "#E0E0E0",
    activebackground = "lightgrey",
    activeforeground = "#363A36",
    bg = "lightgrey",
    fg = "#363A36",
    entrybg = "lightgrey",
    cornometer_icon = PhotoImage(file='D:\\Study\\projects\\project\\links\\corno50.png'),
    startup_icon = PhotoImage(file='D:\\Study\\projects\\project\\links\\startup.png')
)
main_theme = light

class languge:
    cornometer_text_start = "start"
    cornometer_text_stop = "stop"
    cornometer_text_reset = "reset"
    Done_Massage = "Done"
    Box_Massage = "Complited"
    address_ask = "give me address"
    filename_ask = "give me file"
    submit_text = "submit"
    Dns_adaptor_ask = "add adaptor name"
    dns1_ask = "add dns 1"
    dns2_ask = "add dns 2"
    Dns_desable = "desable dns"
    def __init__(self,cornometer_text_start,
                 cornometer_text_stop,
                 cornometer_text_reset,
                 Done_Massage,
                 Box_Massage,
                 address_ask,
                 filename_ask,
                 submit_text,
                 Dns_adaptor_ask,
                 dns1_ask,
                 dns2_ask,
                 Dns_desable):
        self.cornometer_text_start = cornometer_text_start
        self.cornometer_text_stop = cornometer_text_stop
        self.cornometer_text_reset = cornometer_text_reset
        self.Done_Massage = Done_Massage
        self.Box_Massage = Box_Massage
        self.address_ask = address_ask
        self.filename_ask = filename_ask
        self.submit_text = submit_text
        self.Dns_adaptor_ask = Dns_adaptor_ask
        self.dns1_ask = dns1_ask
        self.dns2_ask = dns2_ask
        self.Dns_desable = Dns_desable
en = languge(
    cornometer_text_start = "start",
    cornometer_text_stop = "stop",
    cornometer_text_reset = "reset",
    Done_Massage = "Done",
    Box_Massage = "Complited",
    address_ask = "give me address",
    filename_ask = "give me file",
    submit_text = "submit",
    Dns_adaptor_ask = "add adaptor name",
    dns1_ask = "add dns 1",
    dns2_ask = "add dns 2",
    Dns_desable = "desable dns"
)
fa = languge(
    cornometer_text_start = "شروع",
    cornometer_text_stop = "پایان",
    cornometer_text_reset = "دوباره",
    Done_Massage = "تمام",
    Box_Massage = "عملیات به پایان رسید",
    address_ask = "ادرس فایل را وارد کنید",
    filename_ask = "اسم فایل را وارد کنید",
    submit_text = "ثبت",
    Dns_adaptor_ask = "اسم اداپتور را اضافه کنید",
    dns1_ask = "دنس یک را وارد کنید",
    dns2_ask = "دنس دو را وارد کنید",
    Dns_desable = "خاموش کردن دنس"
)
main_languge = fa

class ToolTip(object):
    def __init__(self, widget, text='Tooltip'):
        self.widget = widget
        self.text = text
        self.widget.bind('<Enter>', self.enter)
        self.widget.bind('<Leave>', self.leave)
        self.tw = None

    def enter(self, event=None):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 50
        y += self.widget.winfo_rooty()
        # ایجاد پنجره تولتیپ
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, background='grey', relief='solid', borderwidth=1,
                         font=("arial", "8", "normal"))
        label.pack(ipadx=1)

    def leave(self, event=None):
        if self.tw:
            self.tw.destroy()
            self.tw = None

def cmd(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result

def start_move(event,root):
    global x, y
    x = event.x
    y = event.y

def stop_move(event,root):
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

def on_move(event,root):
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
    W1,H1 = coordinates.Main_Window_H,coordinates.Main_Window_W
    X1,Y1= X+W,Y+(H//2)-(H1//2)

    if X >= new_window.winfo_screenwidth()//2:
        X1,Y1= (X-W1-W),Y+(H//2)-(H1//2)
    else:
        X1,Y1= X+W,Y+(H//2)-(H1//2)

    if Y1 < 0:
        Y1 = 0
    
    if (Y1+H1) > new_window.winfo_screenheight():
        Y1 = new_window.winfo_screenheight()-H1

    move_button = tk.Button(new_window, 
                        text="", 
                        height=1,
                        bd=0,
                        activebackground=main_theme.titlebar,
                        bg=main_theme.titlebar)
    move_button.place(x=0,y=0,relwidth=1)
    move_button.bind('<ButtonPress-1>', lambda event,var=new_window: start_move(event,var))
    move_button.bind('<ButtonRelease-1>',lambda event,var=new_window: stop_move(event,var))
    move_button.bind('<B1-Motion>',lambda event,var=new_window: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=new_window.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    closeall_button = tk.Button(move_button, text='close all', command=root.destroy,bg="red")
    closeall_button.pack(side=tk.LEFT)

    new_window.configure(bg=main_theme.window_bg)

    global cornometer_icon,startup_icon

    cornometer = tk.Button(new_window, 
                       image=main_theme.cornometer_icon,
                       command=cornometerwindow,
                       relief='flat', 
                       highlightthickness=0,)
    cornometer.place(x=coordinates.cornometer_button_x,y=coordinates.cornometer_button_y)
    ToolTip(cornometer,"cornometer")

    startup = tk.Button(new_window, 
                       image=main_theme.startup_icon,
                       command=start_up,
                       relief='flat', 
                       highlightthickness=0,)
    startup.place(x=coordinates.startup_button_x,y=coordinates.startup_button_y)
    ToolTip(startup,"start up")

    Dns = tk.Button(new_window, 
                       image=main_theme.startup_icon,
                       command=DnsChange,
                       relief='flat', 
                       highlightthickness=0,)
    Dns.place(x=coordinates.dns_button_x,y=coordinates.dns_button_y)
    ToolTip(Dns,"change dns")

    SafeAntiVirusbutton = tk.Button(new_window, 
                       image=main_theme.startup_icon,
                       command=SafeAntiVirus,
                       relief='flat', 
                       highlightthickness=0,)
    SafeAntiVirusbutton.place(x=coordinates.antivirus_button_x,y=coordinates.antivirus_button_y)
    ToolTip(SafeAntiVirusbutton,"SafeAntiVirus")

    new_window.geometry(f"{W1}x{H1}+{X1}+{Y1}")


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
    cornometer.configure(bg=main_theme.window_bg)

    move_button = tk.Button(cornometer, 
                        text="", 
                        height=1,
                        bd=0,
                        activebackground=main_theme.titlebar,
                        bg=main_theme.titlebar)
    move_button.place(x=0,y=0,relwidth=1)
    move_button.bind('<ButtonPress-1>', lambda event,var=cornometer: start_move(event,var))
    move_button.bind('<ButtonRelease-1>',lambda event,var=cornometer: stop_move(event,var))
    move_button.bind('<B1-Motion>',lambda event,var=cornometer: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=cornometer.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    #cornometer.overrideredirect(True)
    #cornometer.resizable(True, True)
    cornometer.wm_attributes("-toolwindow", "true")
    Wc,Hc = coordinates.cornometer_H,coordinates.cornometer_W
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= cornometer.winfo_screenwidth()//2:
        Xc,Yc= (X-W-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0
    
    if (Yc+H1) > cornometer.winfo_screenheight():
        Yc = cornometer.winfo_screenheight()-H1

    global time_text

    # نمایش زمان
    time_text = tk.Label(cornometer, text='0.00', font=('Helvetica', 48),bg=main_theme.window_bg,fg=main_theme.fg)
    time_text.place(x=coordinates.time_text_x,y=coordinates.time_text_y)

    # دکمه‌های کنترل
    start_button = tk.Button(cornometer, text=main_languge.cornometer_text_start,command=start,bg=main_theme.bg,fg=main_theme.fg,activebackground=main_theme.activebackground,activeforeground=main_theme.activeforeground)
    start_button.place(x=coordinates.start_button_x,y=coordinates.start_button_y)

    stop_button = tk.Button(cornometer, text=main_languge.cornometer_text_stop,command=stop,bg=main_theme.bg,fg=main_theme.fg,activebackground=main_theme.activebackground,activeforeground=main_theme.activeforeground)
    stop_button.place(x=coordinates.stop_button_x,y=coordinates.stop_button_y)

    reset_button = tk.Button(cornometer, text=main_languge.cornometer_text_reset,command=reset,bg=main_theme.bg,fg=main_theme.fg,activebackground=main_theme.activebackground,activeforeground=main_theme.activeforeground)
    reset_button.place(x=coordinates.reset_button_x,y=coordinates.reset_button_y)
    
    cornometer.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

def start_up():

    def retrieve_input():
        spliit = []
        input_value1 = entry1.get()
        input_value2 = entry2.get()
        if "/" in input_value1:
            spliit = input_value1.split("/")
        else:
            spliit = input_value1.split("\\")

        path = ""
        for i in spliit:
            path += "".join(i)+"\\"
        path += input_value2

        result = cmd(f'reg add HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v {input_value2} /t REG_SZ /d \"{path}\"')
        messagebox.showinfo(main_languge.Done_Massage, main_languge.Box_Massage)


    global W,H,X,Y
    global W1,H1,X1,Y1
    startup = Toplevel(root)
    startup.configure(bg=main_theme.window_bg)

    move_button = tk.Button(startup, 
                        text="", 
                        height=1,
                        bd=0,
                        activebackground=main_theme.titlebar,
                        bg=main_theme.titlebar)
    move_button.place(x=0,y=0,relwidth=1)
    move_button.bind('<ButtonPress-1>', lambda event,var=startup: start_move(event,var))
    move_button.bind('<ButtonRelease-1>',lambda event,var=startup: stop_move(event,var))
    move_button.bind('<B1-Motion>',lambda event,var=startup: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=startup.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    #cornometer.overrideredirect(True)
    #cornometer.resizable(True, True)
    startup.wm_attributes("-toolwindow", "true")
    Wc,Hc = coordinates.startup_W,coordinates.startup_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= startup.winfo_screenwidth()//2:
        Xc,Yc= (X-W-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > startup.winfo_screenheight():
        Yc = startup.winfo_screenheight()-H1

    # نمایش زمان
    label1 = tk.Label(startup, text=main_languge.address_ask, font=('Helvetica', 10),bg=main_theme.window_bg,fg=main_theme.fg)
    label1.place(x=coordinates.startup_label1_x,y=coordinates.startup_label1_y)

    entry1 = tk.Entry(startup,bg=main_theme.entrybg)
    entry1.place(x=coordinates.startup_entry1_x,y=coordinates.startup_entry1_y)

    label2 = tk.Label(startup, text=main_languge.filename_ask, font=('Helvetica', 10),bg=main_theme.window_bg,fg=main_theme.fg)
    label2.place(x=coordinates.startup_label2_x,y=coordinates.startup_label2_y)

    entry2 = tk.Entry(startup,bg=main_theme.entrybg)
    entry2.place(x=coordinates.startup_entry2_x,y=coordinates.startup_entry2_y)

    submit_button = tk.Button(startup, text=main_languge.submit_text, command=retrieve_input,bg=main_theme.bg,fg=main_theme.fg,activebackground=main_theme.activebackground,activeforeground=main_theme.activeforeground)
    submit_button.place(x=coordinates.startup_submit_x,y=coordinates.startup_submit_y)

    startup.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

def DnsChange():

    def retrieve_input():
        input_value1 = entry1.get()
        input_value2 = entry2.get()
        input_value3 = entry3.get()
        
        cmd(f"netsh interface ip set dns \"{input_value1}\" static {input_value2} primary")
        cmd(f"netsh interface ip add dns \"{input_value1}\" {input_value3} index=2")

        messagebox.showinfo(main_languge.Done_Massage, main_languge.Box_Massage)
    def Desabling():
        input_value1 = entry1.get()
        cmd(f"netsh interface ip set dns \"{input_value1}\" dhcp")
        messagebox.showinfo(main_languge.Done_Massage, main_languge.Box_Massage)


    global W,H,X,Y
    global W1,H1,X1,Y1
    dnschange = Toplevel(root)
    dnschange.configure(bg=main_theme.window_bg)

    move_button = tk.Button(dnschange, 
                        text="", 
                        height=1,
                        bd=0,
                        activebackground=main_theme.titlebar,
                        bg=main_theme.titlebar)
    move_button.place(x=0,y=0,relwidth=1)
    move_button.bind('<ButtonPress-1>', lambda event,var=dnschange: start_move(event,var))
    move_button.bind('<ButtonRelease-1>',lambda event,var=dnschange: stop_move(event,var))
    move_button.bind('<B1-Motion>',lambda event,var=dnschange: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=dnschange.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    #cornometer.overrideredirect(True)
    #cornometer.resizable(True, True)
    dnschange.wm_attributes("-toolwindow", "true")
    Wc,Hc = coordinates.dns_W,coordinates.dns_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= dnschange.winfo_screenwidth()//2:
        Xc,Yc= (X-W-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > dnschange.winfo_screenheight():
        Yc = dnschange.winfo_screenheight()-H1

    # نمایش زمان
    label1 = tk.Label(dnschange, text=main_languge.Dns_adaptor_ask, font=('Helvetica', 10),bg=main_theme.window_bg,fg=main_theme.fg)
    label1.place(x=coordinates.dns_label1_x,y=coordinates.dns_label1_y)

    entry1 = tk.Entry(dnschange,bg=main_theme.entrybg)
    entry1.place(x=coordinates.dns_entry1_x,y=coordinates.dns_entry1_y)

    label2 = tk.Label(dnschange, text=main_languge.dns1_ask, font=('Helvetica', 10),bg=main_theme.window_bg,fg=main_theme.fg)
    label2.place(x=coordinates.dns_label2_x,y=coordinates.dns_label2_y)

    entry2 = tk.Entry(dnschange,bg=main_theme.entrybg)
    entry2.place(x=coordinates.dns_entry2_x,y=coordinates.dns_entry2_y)

    label3 = tk.Label(dnschange, text=main_languge.dns2_ask, font=('Helvetica', 10),bg=main_theme.window_bg,fg=main_theme.fg)
    label3.place(x=coordinates.dns_label3_x,y=coordinates.dns_label3_y)

    entry3 = tk.Entry(dnschange,bg=main_theme.entrybg)
    entry3.place(x=coordinates.dns_entry3_x,y=coordinates.dns_entry3_y)

    submit_button1 = tk.Button(dnschange, text=main_languge.submit_text, command=retrieve_input,bg=main_theme.bg,fg=main_theme.fg,activebackground=main_theme.activebackground,activeforeground=main_theme.activeforeground)
    submit_button1.place(x=coordinates.dns_submit1_x,y=coordinates.dns_submit1_y)
    submit_button2 = tk.Button(dnschange, text=main_languge.Dns_desable, command=Desabling,bg=main_theme.bg,fg=main_theme.fg,activebackground=main_theme.activebackground,activeforeground=main_theme.activeforeground)
    submit_button2.place(x=coordinates.dns_submit2_x,y=coordinates.dns_submit2_y)

    dnschange.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

def SafeAntiVirus():

    def retrieve_input():
        spliit = []
        input_value1 = entry1.get()
        input_value2 = entry2.get()
        if "/" in input_value1:
            spliit = input_value1.split("/")
        else:
            spliit = input_value1.split("\\")

        path = ""
        for i in spliit:
            path += "".join(i)+"\\"
        path += input_value2

        result = cmd(f'reg add HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v {input_value2} /t REG_SZ /d \"{path}\"')
        messagebox.showinfo(main_languge.Done_Massage, main_languge.Box_Massage)

    global W,H,X,Y
    global W1,H1,X1,Y1
    SafeAntiVirus = Toplevel(root)
    SafeAntiVirus.configure(bg=main_theme.window_bg)
    move_button = tk.Button(SafeAntiVirus, 
                        text="", 
                        height=1,
                        bd=0,
                        activebackground=main_theme.titlebar,
                        bg=main_theme.titlebar)
    move_button.place(x=0,y=0,relwidth=1)
    move_button.bind('<ButtonPress-1>', lambda event,var=SafeAntiVirus: start_move(event,var))
    move_button.bind('<ButtonRelease-1>',lambda event,var=SafeAntiVirus: stop_move(event,var))
    move_button.bind('<B1-Motion>',lambda event,var=SafeAntiVirus: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=SafeAntiVirus.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    #cornometer.overrideredirect(True)
    #cornometer.resizable(True, True)
    SafeAntiVirus.wm_attributes("-toolwindow", "true")
    Wc,Hc = coordinates.antivirus_W,coordinates.antivirus_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= SafeAntiVirus.winfo_screenwidth()//2:
        Xc,Yc= (X-W-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > SafeAntiVirus.winfo_screenheight():
        Yc = SafeAntiVirus.winfo_screenheight()-H1
    # نمایش زمان
    label1 = tk.Label(SafeAntiVirus, text=main_languge.address_ask, font=('Helvetica', 10),bg=main_theme.window_bg,fg=main_theme.fg)
    label1.place(x=coordinates.antivirus_label1_x,y=coordinates.antivirus_label1_y)

    entry1 = tk.Entry(SafeAntiVirus,bg=main_theme.entrybg)
    entry1.place(x=coordinates.antivirus_entry1_x,y=coordinates.antivirus_entry1_y)

    label2 = tk.Label(SafeAntiVirus, text=main_languge.filename_ask, font=('Helvetica', 10),bg=main_theme.window_bg,fg=main_theme.fg)
    label2.place(x=coordinates.antivirus_label2_x,y=coordinates.antivirus_label2_y)

    entry2 = tk.Entry(SafeAntiVirus,bg=main_theme.entrybg)
    entry2.place(x=coordinates.antivirus_entry2_x,y=coordinates.antivirus_entry2_y)
    
    # ایجاد متغیر کنترل
    selected_option = tk.IntVar()
        # ایجاد چهار رادیو باتن
    button1 = tk.Radiobutton(SafeAntiVirus, text='File', variable=selected_option, value=1, bg=main_theme.window_bg,fg=main_theme.fg,activebackground=main_theme.window_bg,activeforeground=main_theme.activeforeground)
    button1.place(x=coordinates.antivirus_button1_x,y=coordinates.antivirus_button1_y)

    button2 = tk.Radiobutton(SafeAntiVirus, text='Folder', variable=selected_option, value=2, bg=main_theme.window_bg,fg=main_theme.fg,activebackground=main_theme.window_bg,activeforeground=main_theme.activeforeground)
    button2.place(x=coordinates.antivirus_button2_x,y=coordinates.antivirus_button2_y)

    button3 = tk.Radiobutton(SafeAntiVirus, text='process', variable=selected_option, value=3, bg=main_theme.window_bg,fg=main_theme.fg,activebackground=main_theme.window_bg,activeforeground=main_theme.activeforeground)
    button3.place(x=coordinates.antivirus_button3_x,y=coordinates.antivirus_button3_y)

    submit_button1 = tk.Button(SafeAntiVirus, text=main_languge.submit_text, command=retrieve_input,bg=main_theme.bg,fg=main_theme.fg,activebackground=main_theme.activebackground,activeforeground=main_theme.activeforeground)
    submit_button1.place(x=coordinates.antivirus_submit_x,y=coordinates.antivirus_submit_y)

    SafeAntiVirus.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")


W,H,X,Y=20,78,100,100
root.geometry(f"{W}x{H}+{X}+{Y}") #20x78
#root.overrideredirect(True)
#root.resizable(False, False)

root.title("^^")
root.wm_attributes("-toolwindow", "true")
if X >= (root.winfo_screenwidth()//2):
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
                       activebackground=main_theme.activebackground, 
                       activeforeground=main_theme.activeforeground,
                       bg=main_theme.bg,
                       fg=main_theme.fg)
openbutton.pack(side=tk.BOTTOM, fill=tk.X)

move_button = tk.Button(root, 
                        text="",
                        height=1,
                        bd=0,
                        activebackground=main_theme.titlebar,
                        bg=main_theme.titlebar)
move_button.pack(side=tk.BOTTOM, fill=tk.X)
move_button.bind('<ButtonPress-1>', lambda event,var=root: start_move(event,var))
move_button.bind('<ButtonRelease-1>',lambda event,var=root: stop_move(event,var))
move_button.bind('<B1-Motion>',lambda event,var=root: on_move(event,var))
root.mainloop()
