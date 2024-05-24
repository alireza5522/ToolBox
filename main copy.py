import time
import threading
import tkinter as tk
from tkinter import Toplevel
import subprocess
from tkinter import messagebox
import requests
import json
import sys
import os
from tkinter import simpledialog
from zipfile import ZipFile

try:
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
except:
    pass
drive = application_path[0]

root = tk.Tk()

defult_title = True
password = "hi"
x0,y0 = 10,10
W1,H1 = 50,200
X1,Y1= 10,10
running = False
start_time = None
timer = 0
time_text = None
startup = False

from lang_theme_coords import coordinates
from lang_theme_coords import dark,light
main_theme = dark
from lang_theme_coords import en,fa
main_languge = en

def encrypt(text):
    # output = ""
    # for c in text:
    #     output = output +(chr(ord(c)+4))
    # return output

    output = ""
    for c in text:
        if int(ord(c))%2:
            sign = -1
        else:
            sign = 1

        output = output +(chr(ord(c)+sign))
    return output

def decrypt(text):
    # output = ""
    # for c in text:
    #     output = output +(chr(ord(c)-4))
    # return output

    output = ""
    for c in text:
        if int(ord(c))%2:
            sign = 1
        else:
            sign = -1
        output = output +(chr(ord(c)-sign))
    return output

class ToolTip(object):
    def __init__(self, widget, text='Tooltip'):
        self.widget = widget
        self.text = text
        self.widget.bind('<Enter>', self.enter)
        self.widget.bind('<Leave>', self.leave)
        self.tw = None

    def enter(self, event=None):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 55
        y += self.widget.winfo_rooty() + (15/2)
        # ایجاد پنجره تولتیپ
        self.tw = tk.Toplevel(self.widget)
        self.tw.attributes('-topmost', True)
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

def stop_move(event,roots):
    global x, y
    global x0, y0
    global X, Y
    global root,openbutton
    #root.winfo_screenwidth()
    if roots.winfo_x() <= 30:
        x0=0
    elif roots.winfo_x() >= roots.winfo_screenwidth()-30-W:
        x0=roots.winfo_screenwidth()-W

    if roots.winfo_y() <= 30:
        y0=0
    X,Y = x0,y0
    roots.geometry(f"+{x0}+{y0}")
    x = None
    y = None
    if roots == root:
        writesettings("X",X,1)
        writesettings("Y",Y,2)
        if X >= (root.winfo_screenwidth()//2):
            openbutton.configure(text="<<")
        else:
            openbutton.configure(text=">>")
        
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
    new_window.overrideredirect(defult_title)
    #new_window.resizable(True, True)
    new_window.wm_attributes("-toolwindow", "true")
    new_window.attributes('-topmost', True)
    W1,H1 = coordinates.Main_Window_H,coordinates.Main_Window_W
    X1,Y1= X+W,Y+(H//2)-(H1//2)

    if X >= new_window.winfo_screenwidth()//2:
        X1,Y1= (X-W1),Y+(H//2)-(H1//2)
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
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=new_window: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=new_window: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=new_window: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=new_window.destroy,bg=main_theme["closebg"], fg=main_theme["closefg"], height=1,width=2)
    close_button.pack(side=tk.RIGHT)
    closeall_button = tk.Button(move_button, text='close all', command=root.destroy,bg=main_theme["closebg"], fg=main_theme["closefg"])
    closeall_button.pack(side=tk.LEFT)
    setting = tk.Button(move_button, 
                       image=main_theme["setting_icon"],
                       command=settings,
                       relief='flat', 
                       highlightthickness=0,
                       bd=0,
                       bg=main_theme["titlebar"],
                       fg=main_theme["titlebar"],
                       activebackground=main_theme["titlebar"],
                       activeforeground=main_theme["titlebar"])
    setting.pack(side=tk.LEFT)

    new_window.configure(bg=main_theme["window_bg"])

    global cornometer_icon,startup_icon

    cornometer = tk.Button(new_window, 
                       image=main_theme["cornometer_icon"],
                       command=cornometerwindow,
                       relief='flat', 
                       bd=0,
                       highlightthickness=0,)
    cornometer.place(x=coordinates.cornometer_button_x,y=coordinates.cornometer_button_y)
    ToolTip(cornometer,main_languge["cornometertool"])

    startup = tk.Button(new_window, 
                       image=main_theme["startup_icon"],
                       command=start_up,
                       relief='flat', 
                       bd=0,
                       highlightthickness=0,)
    startup.place(x=coordinates.startup_button_x,y=coordinates.startup_button_y)
    ToolTip(startup,main_languge["startuptool"])

    Dns = tk.Button(new_window, 
                       image=main_theme["dns_icon"],
                       command=DnsChange,
                       relief='flat', 
                       bd=0,
                       highlightthickness=0,)
    Dns.place(x=coordinates.dns_button_x,y=coordinates.dns_button_y)
    ToolTip(Dns,main_languge["dnstool"])

    SafeAntiVirusbutton = tk.Button(new_window, 
                       image=main_theme["antivirus_icon"],
                       command=SafeAntiVirus,
                       relief='flat',
                       bd=0,
                       highlightthickness=0,)
    SafeAntiVirusbutton.place(x=coordinates.antivirus_button_x,y=coordinates.antivirus_button_y)
    ToolTip(SafeAntiVirusbutton,main_languge["antitool"])

    Religiustimes = tk.Button(new_window, 
                       image=main_theme["religius_icon"],
                       command=Religius_times,
                       relief='flat', 
                       highlightthickness=0,
                       bd=0,)
    Religiustimes.place(x=coordinates.Religiustimes_button_x,y=coordinates.Religiustimes_button_y)
    ToolTip(Religiustimes,main_languge["religiustool"])
    
    date = tk.Button(new_window, 
                       image=main_theme["date_icon"],
                       command=date_time,
                       relief='flat', 
                       highlightthickness=0,
                       bd=0,)
    date.place(x=coordinates.date_button_x,y=coordinates.date_button_y)
    ToolTip(date,main_languge["datetool"])

    btc = tk.Button(new_window, 
                       image=main_theme["btc_icon"],
                       command=btc_call,
                       relief='flat', 
                       highlightthickness=0,
                       bd=0,)
    btc.place(x=coordinates.btc_button_x,y=coordinates.btc_button_y)
    ToolTip(btc,main_languge["btctool"])
    
    translate = tk.Button(new_window, 
                       image=main_theme["translate_icon"],
                       command=Translate,
                       relief='flat', 
                       highlightthickness=0,
                       bd=0,)
    translate.place(x=coordinates.translate_button_x,y=coordinates.translate_button_y)
    ToolTip(translate,main_languge["trtool"])

    qrcode = tk.Button(new_window, 
                       image=main_theme["qrcode_icon"],
                       command=QRcode,
                       relief='flat', 
                       highlightthickness=0,
                       bd=0,)
    qrcode.place(x=coordinates.qrcode_button_x,y=coordinates.qrcode_button_y)
    ToolTip(qrcode,main_languge["qrtool"])

    search = tk.Button(new_window, 
                       image=main_theme["search_icon"],
                       command=Search,
                       relief='flat', 
                       highlightthickness=0,
                       bd=0,)
    search.place(x=coordinates.search_button_x,y=coordinates.search_button_y)
    ToolTip(search,main_languge["srtool"])

    wether = tk.Button(new_window, 
                       image=main_theme["wether_icon"],
                       command=Wether,
                       relief='flat', 
                       highlightthickness=0,
                       bd=0,)
    wether.place(x=coordinates.wether_button_x,y=coordinates.wether_button_y)
    ToolTip(wether,main_languge["settingtool"])

    todolist = tk.Button(new_window, 
                       image=main_theme["todolist_icon"],
                       command=Todolist,
                       relief='flat', 
                       highlightthickness=0,
                       bd=0,)
    todolist.place(x=coordinates.todolist_button_x,y=coordinates.todolist_button_y)
    ToolTip(todolist,main_languge["todolisttool"])

    password = tk.Button(new_window, 
                       image=main_theme["pass_icon"],
                       command=Password,
                       relief='flat', 
                       highlightthickness=0,
                       bd=0,)
    password.place(x=coordinates.password_button_x,y=coordinates.password_button_y)
    ToolTip(password,main_languge["settingtool"])

    backup = tk.Button(new_window, 
                       image=main_theme["backup_icon"],
                       command=Backup,
                       relief='flat', 
                       highlightthickness=0,
                       bd=0,)
    backup.place(x=coordinates.backup_button_x,y=coordinates.backup_button_y)
    ToolTip(backup,main_languge["settingtool"])

    dollar = tk.Button(new_window, 
                       image=main_theme["dollar_icon"],
                       command=Dollar,
                       relief='flat', 
                       highlightthickness=0,
                       bd=0,)
    dollar.place(x=coordinates.dollar_button_x,y=coordinates.dollar_button_y)
    ToolTip(dollar,main_languge["settingtool"])

    new_window.geometry(f"{W1}x{H1}+{X1}+{Y1}")

def cornometerwindow():
    global running,start_time,timer
    def update_time():
        if running:
            global timer
            global time_text
            timer = time.time() - start_time
            time_text.configure(text=f'{timer:.2f}')
            cornometer.after(10, update_time)

    def start():
        global running, start_time
        if not running:
            running = True
            start_time = time.time()
            update_time()

    def stop():
        global running
        running = False

    def reset():
        global timer
        global time_text
        timer = 0
        time_text.configure(text='0.00')

    global W,H,X,Y
    global W1,H1,X1,Y1
    cornometer = Toplevel(root)
    cornometer.configure(bg=main_theme["window_bg"])

    move_button = tk.Button(cornometer, 
                        text=main_languge["Cornometer"], 
                        anchor="w",
                        height=1,
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=cornometer: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=cornometer: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=cornometer: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=cornometer.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    cornometer.overrideredirect(defult_title)
    #cornometer.resizable(True, True)
    cornometer.wm_attributes("-toolwindow", "true")
    cornometer.attributes('-topmost', True)
    Wc,Hc = coordinates.cornometer_H,coordinates.cornometer_W
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= cornometer.winfo_screenwidth()//2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X1+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0
    
    if (Yc+H1) > cornometer.winfo_screenheight():
        Yc = cornometer.winfo_screenheight()-H1

    global time_text
    print(Wc,Hc,Xc,Yc)
    print("----------------")


    time_text = tk.Label(cornometer, text='0.00', font=('Helvetica', 48),bg=main_theme["window_bg"],fg=main_theme["fg"])
    time_text.place(x=coordinates.time_text_x,y=coordinates.time_text_y,anchor="center")

    start_button = tk.Button(cornometer, text=main_languge["cornometer_text_start"],command=start,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    start_button.place(x=coordinates.start_button_x,y=coordinates.start_button_y,width=150,anchor="center")

    stop_button = tk.Button(cornometer, text=main_languge["cornometer_text_stop"],command=stop,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    stop_button.place(x=coordinates.stop_button_x,y=coordinates.stop_button_y,width=150,anchor="center")

    reset_button = tk.Button(cornometer, text=main_languge["cornometer_text_reset"],command=reset,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    reset_button.place(x=coordinates.reset_button_x,y=coordinates.reset_button_y,width=150,anchor="center")
    
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
        messagebox.showinfo(main_languge["Done_Massage"], main_languge["Box_Massage"])

    def delete_inp():
        input_value2 = entry2.get()
        result = cmd(f'REG DELETE "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /v "{input_value2}" /f')
        messagebox.showinfo(main_languge["Done_Massage"], main_languge["Box_Massage"])

    global W,H,X,Y
    global W1,H1,X1,Y1
    startup = Toplevel(root)
    startup.configure(bg=main_theme["window_bg"])

    move_button = tk.Button(startup, 
                        text=main_languge["Startup"],
                        anchor="w", 
                        height=1,
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=startup: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=startup: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=startup: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=startup.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    startup.overrideredirect(defult_title)
    #cornometer.resizable(True, True)
    startup.wm_attributes("-toolwindow", "true")
    startup.attributes('-topmost', True)
    Wc,Hc = coordinates.startup_W,coordinates.startup_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= startup.winfo_screenwidth()//2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > startup.winfo_screenheight():
        Yc = startup.winfo_screenheight()-H1

    label1 = tk.Label(startup, text=main_languge["address_ask"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label1.place(x=coordinates.startup_label1_x,y=coordinates.startup_label1_y,anchor="center")

    entry1 = tk.Entry(startup,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry1.place(x=coordinates.startup_entry1_x,y=coordinates.startup_entry1_y,width=150)

    label2 = tk.Label(startup, text=main_languge["filename_ask"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label2.place(x=coordinates.startup_label2_x,y=coordinates.startup_label2_y,anchor="center")

    entry2 = tk.Entry(startup,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry2.place(x=coordinates.startup_entry2_x,y=coordinates.startup_entry2_y,width=150)

    submit_button = tk.Button(startup, text=main_languge["submit_text"], command=retrieve_input,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    submit_button.place(x=coordinates.startup_submit_x,y=coordinates.startup_submit_y,anchor="center")
    
    delete_button = tk.Button(startup, text=main_languge["delete_text"], command=delete_inp,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    delete_button.place(x=coordinates.startup_delete_x,y=coordinates.startup_delete_y,anchor="center")


    startup.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

def DnsChange():

    def retrieve_input():
        input_value1 = entry1.get()
        input_value2 = entry2.get()
        input_value3 = entry3.get()
        
        cmd(f"netsh interface ip set dns \"{input_value1}\" static {input_value2} primary")
        cmd(f"netsh interface ip add dns \"{input_value1}\" {input_value3} index=2")

        messagebox.showinfo(main_languge["Done_Massage"], main_languge["Box_Massage"])
    def Desabling():
        input_value1 = entry1.get()
        cmd(f"netsh interface ip set dns \"{input_value1}\" dhcp")
        messagebox.showinfo(main_languge["Done_Massage"], main_languge["Box_Massage"])


    global W,H,X,Y
    global W1,H1,X1,Y1
    dnschange = Toplevel(root)
    dnschange.configure(bg=main_theme["window_bg"])

    move_button = tk.Button(dnschange, 
                        text=main_languge["DNS"],
                        anchor="w", 
                        height=1,
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=dnschange: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=dnschange: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=dnschange: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=dnschange.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    dnschange.overrideredirect(defult_title)
    #cornometer.resizable(True, True)
    dnschange.wm_attributes("-toolwindow", "true")
    dnschange.attributes('-topmost', True)
    Wc,Hc = coordinates.dns_W,coordinates.dns_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= dnschange.winfo_screenwidth()//2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > dnschange.winfo_screenheight():
        Yc = dnschange.winfo_screenheight()-H1

    # نمایش زمان
    label1 = tk.Label(dnschange, text=main_languge["Dns_adaptor_ask"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label1.place(x=coordinates.dns_label1_x,y=coordinates.dns_label1_y,anchor="center")

    entry1 = tk.Entry(dnschange,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry1.place(x=coordinates.dns_entry1_x,y=coordinates.dns_entry1_y,anchor="center")

    label2 = tk.Label(dnschange, text=main_languge["dns1_ask"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label2.place(x=coordinates.dns_label2_x,y=coordinates.dns_label2_y,anchor="center")

    entry2 = tk.Entry(dnschange,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry2.place(x=coordinates.dns_entry2_x,y=coordinates.dns_entry2_y,anchor="center")

    label3 = tk.Label(dnschange, text=main_languge["dns2_ask"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label3.place(x=coordinates.dns_label3_x,y=coordinates.dns_label3_y,anchor="center")

    entry3 = tk.Entry(dnschange,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry3.place(x=coordinates.dns_entry3_x,y=coordinates.dns_entry3_y,anchor="center")

    submit_button1 = tk.Button(dnschange, text=main_languge["submit_dns"], command=retrieve_input,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    submit_button1.place(x=coordinates.dns_submit1_x,y=coordinates.dns_submit1_y,anchor="center")
    delete_button2 = tk.Button(dnschange, text=main_languge["Dns_desable"], command=Desabling,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    delete_button2.place(x=coordinates.dns_submit2_x,y=coordinates.dns_submit2_y,anchor="center")

    dnschange.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

def SafeAntiVirus():

    def retrieve_input():
        spliit = []
        input_value1 = entry1.get()
        if "/" in input_value1:
            spliit = input_value1.split("/")
        else:
            spliit = input_value1.split("\\")

        path = ""
        for i in spliit:
            path += "".join(i)+"\\"

        result = cmd(f'powershell -inputformat none -outputformat none -NonInteractive -Command \"Add-MpPreference -ExclusionPath \'{input_value1}\'\"')
        messagebox.showinfo(main_languge["Done_Massage"], main_languge["Box_Massage"])

    global W,H,X,Y
    global W1,H1,X1,Y1
    SafeAntiVirus = Toplevel(root)
    SafeAntiVirus.configure(bg=main_theme["window_bg"])
    move_button = tk.Button(SafeAntiVirus, 
                        text=main_languge["anti"], 
                        anchor="w",
                        height=1,
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=SafeAntiVirus: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=SafeAntiVirus: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=SafeAntiVirus: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=SafeAntiVirus.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    SafeAntiVirus.overrideredirect(defult_title)
    #cornometer.resizable(True, True)
    SafeAntiVirus.wm_attributes("-toolwindow", "true")
    SafeAntiVirus.attributes('-topmost', True)
    Wc,Hc = coordinates.antivirus_W,coordinates.antivirus_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= SafeAntiVirus.winfo_screenwidth()//2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > SafeAntiVirus.winfo_screenheight():
        Yc = SafeAntiVirus.winfo_screenheight()-H1

    label1 = tk.Label(SafeAntiVirus, text=main_languge["address_ask"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label1.place(x=coordinates.antivirus_label1_x,y=coordinates.antivirus_label1_y,anchor="center")

    entry1 = tk.Entry(SafeAntiVirus,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry1.place(x=coordinates.antivirus_entry1_x,y=coordinates.antivirus_entry1_y,anchor="center")

    submit_button1 = tk.Button(SafeAntiVirus, text=main_languge["submit_dns"], command=retrieve_input,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    submit_button1.place(x=coordinates.antivirus_button1_x,y=coordinates.antivirus_button1_y,anchor="center")

    SafeAntiVirus.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

def Religius_times():

    def giveinfo():
        city = entry1.get()

        URL = "https://api.keybit.ir/owghat/?city=" + city

        response = requests.get(URL)
        data = json.loads(response.text)

        morning_call_to_prayer = data['result']['azan_sobh']
        sunrise = data['result']['tolu_aftab']
        noon_call_to_prayer = data['result']['azan_zohr']
        sunset = data['result']['ghorub_aftab']
        evening_call_to_prayer = data['result']['azan_maghreb']
        midnight = data['result']['nimeshab']
        month = data['result']['month']
        day = data['result']['day']
        date = f"1403/{month}/{day}"

        label2.configure(text=f"اذان صبح: {morning_call_to_prayer}\nطلوع آفتاب: {sunrise}\nاذان ظهر: {noon_call_to_prayer}\nغروب آفتاب: {sunset}\nاذان مغرب: {evening_call_to_prayer}\nنیمه شب: {midnight}\nتاریخ: {date}")



    global W,H,X,Y
    global W1,H1,X1,Y1
    Religiustimes = Toplevel(root)
    Religiustimes.configure(bg=main_theme["window_bg"])
    move_button = tk.Button(Religiustimes, 
                        text=main_languge["reli"],
                        anchor="w",
                        height=1,
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=Religiustimes: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=Religiustimes: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=Religiustimes: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=Religiustimes.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    Religiustimes.overrideredirect(defult_title)
    #cornometer.resizable(True, True)
    Religiustimes.wm_attributes("-toolwindow", "true")
    Religiustimes.attributes('-topmost', True)
    Wc,Hc = coordinates.religius_W,coordinates.religius_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= Religiustimes.winfo_screenwidth()//2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > Religiustimes.winfo_screenheight():
        Yc = Religiustimes.winfo_screenheight()-H1

    label1 = tk.Label(Religiustimes, text=main_languge["ask_City_pr"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label1.place(x=coordinates.Religiustimes_label1_x,y=coordinates.Religiustimes_label1_y,anchor="center")
    
    entry1 = tk.Entry(Religiustimes,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry1.place(x=coordinates.Religiustimes_entry1_x,y=coordinates.Religiustimes_entry1_y,anchor="center")
    
    submit_button1 = tk.Button(Religiustimes, text=main_languge["submit_dns"], command=giveinfo,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    submit_button1.place(x=coordinates.Religiustimes_submit_x,y=coordinates.Religiustimes_submit_y,anchor="center")

    label2 = tk.Label(Religiustimes, text="", font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label2.place(x=coordinates.Religiustimes_label2_x,y=coordinates.Religiustimes_label2_y,anchor="center")


    
    Religiustimes.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

def date_time():


    URL = "https://api.keybit.ir/time"

    response = requests.get(URL)
    data = json.loads(response.text)


    time = data["time24"]["full"]["en"]
    hour, minute, second = map(int, time.split(':'))
    hour = hour - 1 if hour > 0 else 23
    date_fa = data["date"]["full"]["official"]["usual"]["en"]
    date_en = data["date"]["other"]["gregorian"]["usual"]["en"]
    data_ar = data["date"]["other"]["ghamari"]["usual"]["en"]
    year_name = data["date"]["year"]['name']
    year_animal = data["date"]["year"]["animal"]
    year_leapyear = data["date"]["year"]["leapyear"]
    month_name = data["date"]["month"]["name"]
    month_asterism =  data["date"]["month"]["asterism"]
    day_event_local = data["date"]["day"]["events"]["local"]
    day_event_holy = data["date"]["day"]["events"]["holy"]
    day_event_global = data["date"]["day"]["events"]["global"]

    text = f"""
    Time: {hour}:{minute}:{second}
    Date (Farsi): {date_fa}
    Date (English): {date_en}
    Date (Arabic): {data_ar}
    Year Name: {year_name}
    Year Animal: {year_animal}
    Is Leap Year: {year_leapyear}
    Month Name: {month_name}
    Month Asterism: {month_asterism}
    Local Events: {day_event_local if day_event_local else '-'}
    Holy Events: {day_event_holy if day_event_holy else '-'}
    Global Events: {day_event_global if day_event_global else '-'}
    """
    messagebox.showinfo("date", text)

def settings():
    global startup
    def theme_change():
        if main_theme == dark:
            writesettings("dark_mode",False,3)
        else:
            writesettings("dark_mode",True,3)
        messagebox.showinfo(main_languge["Done_Massage"], main_languge["Box_Massage"])

    def lang_change():
        if main_languge == en:
            writesettings("language","fa",4)
        else:
            writesettings("language","en",4)
        messagebox.showinfo(main_languge["Done_Massage"], main_languge["Box_Massage"])

    def startup_change():
        global startup
        if startup == True:
            writesettings("startup",False,5)
        else:
            writesettings("startup",True,5)
        messagebox.showinfo(main_languge["Done_Massage"], main_languge["Box_Massage"])

    def passchange():
        global password
        print(password)
        result = simpledialog.askstring("ورودی کاربر", "لطفا یک رشته وارد کنید:")
        if result == password:
            newpass = simpledialog.askstring("ورودی کاربر", "لطفا یک رشته وارد کنید:")
            password = newpass
            writesettings("password",encrypt(newpass),6)

    global W,H,X,Y,password
    global W1,H1,X1,Y1
    setting = Toplevel(root)
    setting.configure(bg=main_theme["window_bg"])
    move_button = tk.Button(setting, 
                        text="", 
                        height=1,
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=setting: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=setting: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=setting: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=setting.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    setting.overrideredirect(defult_title)
    #cornometer.resizable(True, True)
    setting.wm_attributes("-toolwindow", "true")
    setting.attributes('-topmost', True)
    Wc,Hc = coordinates.setting_W,coordinates.setting_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= setting.winfo_screenwidth()//2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > setting.winfo_screenheight():
        Yc = setting.winfo_screenheight()-H1
    
    

    label1 = tk.Label(setting, text=main_languge["themelabel"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label1.place(x=coordinates.settings_label1_x,y=coordinates.settings_label1_y,anchor="center")

    themed = tk.Button(setting, text=main_languge["black"],command=theme_change, bg=main_theme["window_bg"],fg=main_theme["fg"],activebackground=main_theme["window_bg"],activeforeground=main_theme["activeforeground"])
    if main_theme == dark:
        themed.configure(text=main_languge["white"])
    else:
        themed.configure(text=main_languge["black"])
    themed.place(x=coordinates.settings_button1_x,y=coordinates.settings_button1_y,anchor="center")

    label2 = tk.Label(setting, text=main_languge["langlabel"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])

    label2.place(x=coordinates.settings_label2_x,y=coordinates.settings_label2_y,anchor="center")

    lang = tk.Button(setting, text=main_languge["english"],command=lang_change, bg=main_theme["window_bg"],fg=main_theme["fg"],activebackground=main_theme["window_bg"],activeforeground=main_theme["activeforeground"])
    if main_languge == en:
        lang.configure(text=main_languge["farsi"])
    else:
        lang.configure(text=main_languge["english"])
    lang.place(x=coordinates.settings_button3_x,y=coordinates.settings_button3_y,anchor="center")

    isstartup = tk.Button(setting, text=main_languge["startup"],command=startup_change, bg=main_theme["window_bg"],fg=main_theme["fg"],activebackground=main_theme["window_bg"],activeforeground=main_theme["activeforeground"])
    if startup == True:
        isstartup.configure(text=main_languge["startup_"])
    else:
        isstartup.configure(text=main_languge["startup"])
    isstartup.place(x=coordinates.settings_button5_x,y=coordinates.settings_button5_y,anchor="center")

    passw = tk.Button(setting, text=main_languge["changepass"],command=passchange, bg=main_theme["window_bg"],fg=main_theme["fg"],activebackground=main_theme["window_bg"],activeforeground=main_theme["activeforeground"])
    passw.place(x=coordinates.settings_button2_x,y=coordinates.settings_button2_y,anchor="center")
    
    setting.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")
 
def btc_call():

    def get_symbol_data():
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        symbol = entry1.get()
        parameters = {
            "symbol" : symbol
        }

        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': "72ebba38-31de-43ec-8424-c9cc1ed173ee"
        }

        response = requests.get(url, headers=headers, params=parameters)
        data = json.loads(response.text)

        if 'data' not in data or symbol not in data['data']:
            print("Invalid cryptocurrency symbol.")
            messagebox.showinfo(main_languge["Done_Massage"],"Invalid cryptocurrency symbol.")
            return None
        else:
            symbol_data = symbol,data

            if symbol_data is not None:
                symbol, data = symbol_data

                name = data['data'][symbol]['name']
                symbol_name = data['data'][symbol]['symbol']
                price = data['data'][symbol]['quote']['USD']['price']
                hourly_change = data['data'][symbol]['quote']['USD']['percent_change_1h']
                daily_change = data['data'][symbol]['quote']['USD']['percent_change_24h']
                weekly_change = data['data'][symbol]['quote']['USD']['percent_change_7d']
                volume = data['data'][symbol]['quote']['USD']['volume_24h']
                market_cap = data['data'][symbol]['quote']['USD']['market_cap']
                total_supply = data['data'][symbol]['total_supply']
                max_supply = data['data'][symbol]['max_supply']

                if max_supply is None:
                    max_supply = "Ulimited"

                txt = f"""
                {name} ({symbol_name})
                Price: ${price:,.3f} USD
                1hr Change: {hourly_change:.2f}%
                24hr Change: {daily_change:.2f}%
                7d Change: {weekly_change:.2f}%
                Volume: ${volume:,}")
                Market Cap: ${market_cap:,.2f}
                Total Supply: {total_supply:,}
                Max Supply: {max_supply:,}"""
                
                label2.configure(text=txt)

    global W,H,X,Y
    global W1,H1,X1,Y1
    btc = Toplevel(root)
    btc.configure(bg=main_theme["window_bg"])
    move_button = tk.Button(btc, 
                        text=main_languge["Curr"], 
                        height=1,
                        anchor="w",
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=btc: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=btc: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=btc: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=btc.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    btc.overrideredirect(defult_title)
    #cornometer.resizable(True, True)
    btc.wm_attributes("-toolwindow", "true")
    btc.attributes('-topmost', True)
    Wc,Hc = coordinates.btc_W,coordinates.btc_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= btc.winfo_screenwidth()//2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > btc.winfo_screenheight():
        Yc = btc.winfo_screenheight()-H1

    label1 = tk.Label(btc, text=main_languge["btclabel"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label1.place(x=coordinates.btc_label1_x,y=coordinates.btc_label1_y,anchor="center")
    
    entry1 = tk.Entry(btc,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry1.place(x=coordinates.btc_entry1_x,y=coordinates.btc_entry1_y,anchor="center")
    
    submit_button1 = tk.Button(btc, text=main_languge["submit_dns"], command=get_symbol_data,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    submit_button1.place(x=coordinates.btc_submit_x,y=coordinates.btc_submit_y,anchor="center")

    label2 = tk.Label(btc, text="", font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label2.place(x=coordinates.btc_label2_x,y=coordinates.btc_label2_y,anchor="center")

    btc.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")
   
def Translate():

    def EnglishToPersian():

        def copy():
            root.clipboard_clear()
            root.clipboard_append(response.text)

        text = entry1.get()
        URL = "https://api.codebazan.ir/replace/index.php?lang=tofa&text=" + text

        response = requests.get(URL)

        label2.configure(text=response.text)
        copy_button1 = tk.Button(translate, text=main_languge["copy"], command=copy,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
        copy_button1.place(x=coordinates.translate_submit2_x,y=coordinates.translate_submit2_y,anchor="center")

    
        

    global W,H,X,Y
    global W1,H1,X1,Y1
    translate = Toplevel(root)
    translate.configure(bg=main_theme["window_bg"])
    move_button = tk.Button(translate, 
                        text=main_languge["tr"],
                        anchor="w", 
                        height=1,
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=translate: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=translate: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=translate: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=translate.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    translate.overrideredirect(defult_title)
    #cornometer.resizable(True, True)
    translate.wm_attributes("-toolwindow", "true")
    translate.attributes('-topmost', True)
    Wc,Hc = coordinates.translate_W,coordinates.translate_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= translate.winfo_screenwidth()//2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > translate.winfo_screenheight():
        Yc = translate.winfo_screenheight()-H1

    label1 = tk.Label(translate, text=main_languge["sen"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label1.place(x=coordinates.translate_label1_x,y=coordinates.translate_label1_y,anchor="center")
    
    entry1 = tk.Entry(translate,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry1.place(x=coordinates.translate_entry1_x,y=coordinates.translate_entry1_y,anchor="center")
    
    submit_button1 = tk.Button(translate, text=main_languge["submit_dns"], command=EnglishToPersian,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    submit_button1.place(x=coordinates.translate_submit_x,y=coordinates.translate_submit_y,anchor="center")

    label2 = tk.Label(translate, text="", font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label2.place(x=coordinates.translate_label2_x,y=coordinates.translate_label2_y,anchor="center")
    
    
    
    translate.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

def QRcode():
    
    def download_image(image_url, save_path):
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            messagebox.showinfo(main_languge["Done_Massage"], main_languge["qrcodemassage"])
        else:
            messagebox.showinfo(main_languge["Done_Massage"], main_languge["qrcodemassageno"])

    def getqrcode():
        text = entry1.get()

        URL = "https://qr-code.ir/api/qr-code/?d=" + text

        name = ""
        for i in text:
            if i.isascii():
                if i.isdigit() or i.isalpha():
                    name += i

        download_image(URL,name+".png")

    global W,H,X,Y
    global W1,H1,X1,Y1
    qrcode = Toplevel(root)
    qrcode.configure(bg=main_theme["window_bg"])
    move_button = tk.Button(qrcode, 
                        text=main_languge["qr"],
                        anchor="w", 
                        height=1,
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=qrcode: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=qrcode: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=qrcode: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=qrcode.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    qrcode.overrideredirect(defult_title)
    #cornometer.resizable(True, True)
    qrcode.wm_attributes("-toolwindow", "true")
    qrcode.attributes('-topmost', True)
    Wc,Hc = coordinates.qrcode_W,coordinates.qrcode_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= qrcode.winfo_screenwidth()//2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > qrcode.winfo_screenheight():
        Yc = qrcode.winfo_screenheight()-H1

    label1 = tk.Label(qrcode, text=main_languge["qrcodelabel"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label1.place(x=coordinates.qrcode_label1_x,y=coordinates.qrcode_label1_y,anchor="center")
    
    entry1 = tk.Entry(qrcode,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry1.place(x=coordinates.qrcode_entry1_x,y=coordinates.qrcode_entry1_y,anchor="center")
    
    submit_button1 = tk.Button(qrcode, text=main_languge["submit_dns"], command=getqrcode,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    submit_button1.place(x=coordinates.qrcode_submit_x,y=coordinates.qrcode_submit_y,anchor="center")

    qrcode.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

def Search():
    def Serch():
        filename = entry1.get()
        searchpath = entry2.get()
        path = application_path+"\\output.json"

        if searchpath[0].lower() == drive.lower():
            command = f"cd {searchpath} && {application_path}\\tree2json.bat => {application_path}\\output.json"
        else:
            command = f"{searchpath[0]}: && cd {searchpath} && {application_path}\\tree2json.bat => {application_path}\\output.json"
        print(command)
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)

        main_string = str(data)

        start = 0
        poslist = []
        while start < len(main_string):
            position = main_string.find(filename, start)
            if position != -1:
                poslist.append(position)
                start = position + 1
            else:
                break
            
        finded = ""
        for i in poslist:
            i += len(filename)+4
            end_pos = main_string[i:i+512]
            endposition = end_pos.find(",")
            if main_string[i:i+endposition].find("path") != -1:
                # print(main_string[i:i+endposition])
                finded += main_string[i:i+endposition]
                finded += "\n"
        print(finded)

        messagebox.showinfo(main_languge["Done_Massage"],finded)

    global W,H,X,Y,application_path,drive
    global W1,H1,X1,Y1
    search = Toplevel(root)
    search.configure(bg=main_theme["window_bg"])
    move_button = tk.Button(search, 
                        text=main_languge["sr"],
                        anchor="w", 
                        height=1,
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=search: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=search: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=search: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=search.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    search.overrideredirect(defult_title)
    #cornometer.resizable(True, True)
    search.wm_attributes("-toolwindow", "true")
    search.attributes('-topmost', True)
    Wc,Hc = coordinates.search_W,coordinates.search_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= search.winfo_screenwidth()//2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > search.winfo_screenheight():
        Yc = search.winfo_screenheight()-H1

    label1 = tk.Label(search, text=main_languge["searchlabel"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label1.place(x=coordinates.search_label1_x,y=coordinates.search_label1_y,anchor="center")
    
    entry1 = tk.Entry(search,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry1.place(x=coordinates.search_entry1_x,y=coordinates.search_entry1_y,anchor="center")
    
    label2 = tk.Label(search, text=main_languge["searchdir"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label2.place(x=coordinates.search_label2_x,y=coordinates.search_label2_y,anchor="center")
    
    entry2 = tk.Entry(search,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry2.place(x=coordinates.search_entry2_x,y=coordinates.search_entry2_y,anchor="center")
    
    submit_button1 = tk.Button(search, text=main_languge["search"], command=Serch,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    submit_button1.place(x=coordinates.search_submit_x,y=coordinates.search_submit_y,anchor="center")

    search.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

def Wether():
    def getwether():
        city = entry1.get()

        URL = 'https://api.codebazan.ir/weather/?city=' + city

        response = requests.get(URL)
        data = json.loads(response.text)

        item = data['list'][0]

        temp = item['main']['temp']
        temp_min = item['main']['temp_min']
        temp_max = item['main']['temp_max']
        pressure = item['main']['pressure']
        humidity = item['main']['humidity']
        wind_speed = item['wind']['speed']
        wind_direction = item['wind']['deg']
        clouds = item['clouds']['all']
        pop = item['pop']
        weather_description = item['weather'][0]['description']

        label2.configure(text=f'Temperature: {temp}\nMin Temperature: {temp_min}\nMax Temperature: {temp_max}\nPressure: {pressure}\nHumidity: {humidity}%\nWind Speed: {wind_speed}\nWind Direction: {wind_direction}\nClouds: {clouds}\nPop: {pop}\nWeather Description: {weather_description}')


    global W,H,X,Y
    global W1,H1,X1,Y1
    wether = Toplevel(root)
    wether.configure(bg=main_theme["window_bg"])
    move_button = tk.Button(wether, 
                        text="", 
                        height=1,
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=wether: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=wether: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=wether: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=wether.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    wether.overrideredirect(defult_title)
    #cornometer.resizable(True, True)
    wether.wm_attributes("-toolwindow", "true")
    wether.attributes('-topmost', True)
    Wc,Hc = coordinates.wether_W,coordinates.wether_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= wether.winfo_screenwidth()//2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > wether.winfo_screenheight():
        Yc = wether.winfo_screenheight()-H1

    label1 = tk.Label(wether, text=main_languge["askfin"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label1.place(x=coordinates.wether_label1_x,y=coordinates.wether_label1_y,anchor="center")
    
    entry1 = tk.Entry(wether,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry1.place(x=coordinates.wether_entry1_x,y=coordinates.wether_entry1_y,anchor="center")
    
    submit_button1 = tk.Button(wether, text=main_languge["submit_dns"], command=getwether,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    submit_button1.place(x=coordinates.wether_submit_x,y=coordinates.wether_submit_y,anchor="center")

    label2 = tk.Label(wether, text="", font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label2.place(x=coordinates.wether_label2_x,y=coordinates.wether_label2_y,anchor="center")

    wether.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

def Todolist():

    def readfile():
        lines = []
        with open('file.txt', 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(line.strip())
        for task in lines:
            tasks_listbox.insert(tk.END, task)

    def add_task():
        task = entry1.get()
        with open('file.txt', 'a', encoding='utf-8') as file:
            file.write(task + '\n')
        if task != "":
            tasks_listbox.insert(tk.END, task)
            entry1.delete(0, tk.END)
    
    def remove_line_by_number(filename, line_number):
        # خواندن تمام خط‌ها و ذخیره آن‌ها به جز خطی که می‌خواهیم حذف کنیم
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(filename, 'w', encoding='utf-8') as file:
            for i, line in enumerate(lines):
                if i != line_number - 1:  # شماره خط‌ها از 0 شروع می‌شود
                    file.write(line)


    def delete_task():
        try:
            selected_task_index = tasks_listbox.curselection()[0]
            remove_line_by_number('file.txt', selected_task_index+1)
            tasks_listbox.delete(selected_task_index)
        except:
            pass

    global W,H,X,Y
    global W1,H1,X1,Y1
    todolist = Toplevel(root)
    todolist.configure(bg=main_theme["window_bg"])
    move_button = tk.Button(todolist, 
                        text=main_languge['Todo'],
                        anchor="w", 
                        height=1,
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=todolist: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=todolist: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=todolist: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=todolist.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    todolist.overrideredirect(defult_title)
    #cornometer.resizable(True, True)
    todolist.wm_attributes("-toolwindow", "true")
    todolist.attributes('-topmost', True)
    Wc,Hc = coordinates.todolist_W,coordinates.todolist_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= todolist.winfo_screenwidth()//2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > todolist.winfo_screenheight():
        Yc = todolist.winfo_screenheight()-H1
     

    entry1 = tk.Entry(todolist, width=50,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry1.place(x=coordinates.todolist_entry1_x,y=coordinates.todolist_entry1_y,anchor="center")

    add_task_button = tk.Button(todolist, text=main_languge["addtask"], command=add_task,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    add_task_button.place(x=coordinates.todolist_button1_x,y=coordinates.todolist_button1_y,anchor="center")

    tasks_listbox = tk.Listbox(todolist, width=50, height=10,bg=main_theme["entrybg"],fg=main_theme["fg"])
    tasks_listbox.place(x=coordinates.todolist_list_x,y=coordinates.todolist_list_y,anchor="center")
    readfile()

    delete_task_button = tk.Button(todolist, text=main_languge["deltask"], command=delete_task,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    delete_task_button.place(x=coordinates.todolist_button2_x,y=coordinates.todolist_button2_y,anchor="center")
    
    todolist.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

def Password():
    
    global password
    result = simpledialog.askstring("", main_languge["askpass"])
    if result != password:
        return

    def readfile():
        lines = []
        with open('data.sav', 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(decrypt(line.strip()))
        for task in lines:
            tasks_listbox.insert(tk.END, task)

    def add_task():
        task = entry1.get()
        
        with open('data.sav', 'a', encoding='utf-8') as file:
            file.write(encrypt(task) + '\n')
        if task != "":
            tasks_listbox.insert(tk.END, task)
            entry1.delete(0, tk.END)
    
    def remove_line_by_number(filename, line_number):
        # خواندن تمام خط‌ها و ذخیره آن‌ها به جز خطی که می‌خواهیم حذف کنیم
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(filename, 'w', encoding='utf-8') as file:
            for i, line in enumerate(lines):
                if i != line_number - 1:  # شماره خط‌ها از 0 شروع می‌شود
                    file.write(line)


    def delete_task():
        try:
            selected_task_index = tasks_listbox.curselection()[0]
            remove_line_by_number('data.sav', selected_task_index+1)
            tasks_listbox.delete(selected_task_index)
        except:
            pass

    global W,H,X,Y
    global W1,H1,X1,Y1
    passwords = Toplevel(root)
    passwords.configure(bg=main_theme["window_bg"])
    move_button = tk.Button(passwords, 
                        text="", 
                        height=1,
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=passwords: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=passwords: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=passwords: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=passwords.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    passwords.overrideredirect(defult_title)
    #cornometer.resizable(True, True)
    passwords.wm_attributes("-toolwindow", "true")
    passwords.attributes('-topmost', True)
    Wc,Hc = coordinates.todolist_W,coordinates.todolist_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= passwords.winfo_screenwidth()//2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > passwords.winfo_screenheight():
        Yc = passwords.winfo_screenheight()-H1
     

    entry1 = tk.Entry(passwords, width=50,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry1.place(x=coordinates.todolist_entry1_x,y=coordinates.todolist_entry1_y,anchor="center")

    add_task_button = tk.Button(passwords, text=main_languge["addpass"], command=add_task,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    add_task_button.place(x=coordinates.todolist_button1_x,y=coordinates.todolist_button1_y,anchor="center")

    tasks_listbox = tk.Listbox(passwords, width=25, height=10,bg=main_theme["entrybg"],fg=main_theme["fg"])
    tasks_listbox.place(x=90,y=210,anchor="center")
    tasks_listbox = tk.Listbox(passwords, width=25, height=10,bg=main_theme["entrybg"],fg=main_theme["fg"])
    tasks_listbox.place(x=270,y=210,anchor="center")
    readfile()

    delete_task_button = tk.Button(passwords, text=main_languge["delpass"], command=delete_task,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    delete_task_button.place(x=coordinates.todolist_button2_x,y=coordinates.todolist_button2_y,anchor="center")
    
    passwords.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

def Backup():
    
    def bu():
        directory_to_zip = entry1.get()
        output_zip_file = entry2.get()

        def zip_directory(directory_path, output_zip_path):
            with ZipFile(output_zip_path, 'w') as zipf:
                for root, _, files in os.walk(directory_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, directory_path)
                        zipf.write(file_path, arcname=arcname)

        n = directory_to_zip.split("\\")
        output_zip_file += "\\"+n[-1]+".zip"
        print(directory_to_zip,output_zip_file)
        zip_directory(directory_to_zip, output_zip_file)
        print(f"Directory '{directory_to_zip}' has been zipped to '{output_zip_file}'.")


    global W,H,X,Y
    global W1,H1,X1,Y1
    backup = Toplevel(root)
    backup.configure(bg=main_theme["window_bg"])
    move_button = tk.Button(backup, 
                        text="", 
                        height=1,
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
    move_button.place(x=0,y=0,relwidth=1)
    # move_button.bind('<ButtonPress-1>', lambda event,var=backup: start_move(event,var))
    # move_button.bind('<ButtonRelease-1>',lambda event,var=backup: stop_move(event,var))
    # move_button.bind('<B1-Motion>',lambda event,var=backup: on_move(event,var))
    close_button = tk.Button(move_button, text='X', command=backup.destroy,bg="#D1698B")
    close_button.pack(side=tk.RIGHT)
    backup.overrideredirect(defult_title)
    #cornometer.resizable(True, True)
    backup.wm_attributes("-toolwindow", "true")
    backup.attributes('-topmost', True)
    Wc,Hc = coordinates.backup_W,coordinates.backup_H
    Xc,Yc= X+W,Y+(H//2)-(H1//2)

    if X >= backup.winfo_screenwidth()//2:
        Xc,Yc= (X-W1-Wc),Y+(H//2)-(Hc//2)
    else:
        Xc,Yc= X+W+W1,Y+(H//2)-(Hc//2)

    if Yc < 0:
        Yc = 0

    if (Yc+H1) > backup.winfo_screenheight():
        Yc = backup.winfo_screenheight()-H1

    label1 = tk.Label(backup, text=main_languge["ask_City_pr"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label1.place(x=coordinates.backup_label1_x,y=coordinates.backup_label1_y,anchor="center")
    
    entry1 = tk.Entry(backup,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry1.place(x=coordinates.backup_entry1_x,y=coordinates.backup_entry1_y,anchor="center")
    
    label2 = tk.Label(backup, text=main_languge["ask_City_pr"], font=('Helvetica', 10),bg=main_theme["window_bg"],fg=main_theme["fg"])
    label2.place(x=coordinates.backup_label2_x,y=coordinates.backup_label2_y,anchor="center")
    
    entry2 = tk.Entry(backup,bg=main_theme["entrybg"],fg=main_theme["fg"])
    entry2.place(x=coordinates.backup_entry2_x,y=coordinates.backup_entry2_y,anchor="center")
    
    submit_button1 = tk.Button(backup, text=main_languge["submit_dns"], command=bu,bg=main_theme["bg"],fg=main_theme["fg"],activebackground=main_theme["activebackground"],activeforeground=main_theme["activeforeground"])
    submit_button1.place(x=coordinates.backup_submit_x,y=coordinates.backup_submit_y,anchor="center")

    backup.geometry(f"{Wc}x{Hc}+{Xc}+{Yc}")

def Dollar():
    
    def dollar_request():
        URL = "https://www.tgju.org/profile/price_dollar_rl"

        response = requests.get(URL)
        txt = response.text
        key = '<span class="price" data-col="info.last_trade.PDrCotVal">'
        position = (txt.find(key))+len(key)
        return(txt[position:position+7])

    txt = dollar_request()

    messagebox.showinfo(main_languge["Done_Massage"], f"{main_languge["dollarghymat"]}{txt}\n\n{main_languge["sorce"]}www.tgju.org")

def readsettings():
    global W,H,X,Y,main_languge,main_theme,startup,password
    with open('settings.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    X = data["settings"]["X"]
    Y = data["settings"]["Y"]

    if data["settings"]["dark_mode"] == True:
        main_theme = dark
    else:
        main_theme = light

    if data["settings"]["language"] == "en":
        main_languge = en
    else:
        main_languge = fa

    if data["settings"]["startup"] == True:
        startup = True
    else:
        startup = False

    password = decrypt(data["settings"]["password"])

def writesettings(key,val,index):
    file_path = 'settings.json'

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    data['settings'][key] = val

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=index, ensure_ascii=False)


W,H,X,Y=20,78,100,100

readsettings()

root.geometry(f"{W}x{H}+{X}+{Y}") #20x78
root.overrideredirect(defult_title)
#root.resizable(True, True)

root.title("^^")
root.wm_attributes("-toolwindow", "true")
root.attributes('-topmost', True)
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
                       activebackground=main_theme["activebackground"], 
                       activeforeground=main_theme["activeforeground"],
                       bg=main_theme["bg"],
                       fg=main_theme["fg"])
openbutton.pack(side=tk.BOTTOM, fill=tk.X)

move_button = tk.Button(root, 
                        text="",
                        height=1,
                        bd=0,
                        activebackground=main_theme["titlebar"],
                        bg=main_theme["titlebar"])
move_button.pack(side=tk.BOTTOM, fill=tk.X)
move_button.bind('<ButtonPress-1>', lambda event,var=root: start_move(event,var))
move_button.bind('<ButtonRelease-1>',lambda event,var=root: stop_move(event,var))
move_button.bind('<B1-Motion>',lambda event,var=root: on_move(event,var))
root.mainloop()
