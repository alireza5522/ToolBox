from tkinter import PhotoImage
class AS:
    Main_Window_H,Main_Window_W = (210,255) #40#55+10
    cornometer_button_x,cornometer_button_y = (15,45)
    startup_button_x,startup_button_y = (15,85)
    dns_button_x,dns_button_y = (15,125)
    antivirus_button_x,antivirus_button_y = (15,165)
    setting_button_x,setting_button_y = (145,205)
    Religiustimes_button_x,Religiustimes_button_y = (80,45)
    date_button_x,date_button_y = (80,85)
    btc_button_x,btc_button_y = (80,125)
    translate_button_x,translate_button_y = (80,165)
    qrcode_button_x,qrcode_button_y = (80,205)
    search_button_x,search_button_y = (145,45)
    wether_button_x,wether_button_y = (145,85)
    todolist_button_x,todolist_button_y = (15,205)
    password_button_x,password_button_y = (145,125)
    backup_button_x,backup_button_y = (145,165)
    dollar_button_x,dollar_button_y = (145,205)

    cornometer_H,cornometer_W = (210,255)
    time_text_x,time_text_y = (110,90)
    start_button_x,start_button_y = (30,140)
    stop_button_x,stop_button_y = (30,170)
    reset_button_x,reset_button_y = (30,200)

    startup_W,startup_H = (210,255)
    startup_label1_x,startup_label1_y = (105,60)
    startup_entry1_x,startup_entry1_y = (30,80)
    startup_label2_x,startup_label2_y = (105,120)
    startup_entry2_x,startup_entry2_y = (30,140)
    startup_submit_x,startup_submit_y = (105,185)
    startup_delete_x,startup_delete_y = (105,220)
    
    dns_W,dns_H = (250,255)
    dns_label1_x,dns_label1_y = (125,45)
    dns_entry1_x,dns_entry1_y = (125,70)
    dns_label2_x,dns_label2_y = (125,100)
    dns_entry2_x,dns_entry2_y = (125,125)
    dns_label3_x,dns_label3_y = (125,155)
    dns_entry3_x,dns_entry3_y = (125,175)
    dns_submit1_x,dns_submit1_y = (125,205)
    dns_submit2_x,dns_submit2_y = (125,235)

    antivirus_W,antivirus_H = (250,255)
    antivirus_label1_x,antivirus_label1_y = (125,70)
    antivirus_entry1_x,antivirus_entry1_y = (125,95)
    antivirus_label2_x,antivirus_label2_y = (125,125)
    antivirus_entry2_x,antivirus_entry2_y = (125,150)
    antivirus_button1_x,antivirus_button1_y = (125,200)

    religius_W,religius_H = (250,255)
    Religiustimes_label1_x,Religiustimes_label1_y = (125,40)
    Religiustimes_entry1_x,Religiustimes_entry1_y = (125,70)
    Religiustimes_submit_x,Religiustimes_submit_y = (125,100)
    Religiustimes_label2_x,Religiustimes_label2_y = (125,180)

    date_W,date_H = (300,300)
    date_label1_x,date_label1_y = (150,150)

    setting_W,setting_H = (255,255)
    settings_label1_x,settings_label1_y = (10,40)
    settings_button1_x,settings_button1_y = (10,60)
    settings_button2_x,settings_button2_y = (10,80)
    settings_label2_x,settings_label2_y = (10,100)
    settings_button3_x,settings_button3_y = (10,120)
    settings_button4_x,settings_button4_y = (10,140)
    settings_button5_x,settings_button5_y = (10,160)
    settings_button6_x,settings_button6_y = (10,180)

    btc_W,btc_H = (350,350)
    btc_label1_x,btc_label1_y = (175,40)
    btc_entry1_x,btc_entry1_y = (175,70)
    btc_submit_x,btc_submit_y = (175,100)
    btc_label2_x,btc_label2_y = (140,200)
    
    translate_W,translate_H = (250,255)
    translate_label1_x,translate_label1_y = (125,50)
    translate_entry1_x,translate_entry1_y = (125,75)
    translate_submit_x,translate_submit_y = (125,105)
    translate_label2_x,translate_label2_y = (125,150)
    translate_submit2_x,translate_submit2_y = (125,180)

    qrcode_W,qrcode_H = (250,255)
    qrcode_label1_x,qrcode_label1_y = (125,50)
    qrcode_entry1_x,qrcode_entry1_y = (125,75)
    qrcode_submit_x,qrcode_submit_y = (125,105)

    todolist_W,todolist_H = (350,350)
    todolist_entry1_x,todolist_entry1_y = (175,70)
    todolist_button1_x,todolist_button1_y = (175,105)
    todolist_list_x,todolist_list_y = (175,210)
    todolist_button2_x,todolist_button2_y = (175,320)

    search_W,search_H = (250,255)
    search_label1_x,search_label1_y = (125,50)
    search_entry1_x,search_entry1_y = (125,75)
    search_label2_x,search_label2_y = (125,105)
    search_entry2_x,search_entry2_y = (125,130)
    search_submit_x,search_submit_y = (125,170)
    search_label3_x,search_label3_y = (125,190)
    
    wether_W,wether_H = (250,320)
    wether_label1_x,wether_label1_y = (125,45)
    wether_entry1_x,wether_entry1_y = (125,70)
    wether_submit_x,wether_submit_y = (125,105)
    wether_label2_x,wether_label2_y = (125,210)

coordinates = AS()

dark = {
    "closebg": "#e04343",
    "closefg": "white",
    "titlebar": "#4B4F4B",
    "window_bg": "#191B19",
    "activebackground": "#363A36",
    "activeforeground": "#C0C4C4",
    "bg": "#363A36",
    "fg": "#C0C4C4",
    "entrybg": "#363A36",
    "cornometer_icon": PhotoImage(file='.\\links\\cornometerdark.png'),
    "startup_icon": PhotoImage(file='.\\links\\start_updark.png'),
    "dns_icon": PhotoImage(file='.\\links\\dnsdark.png'),
    "antivirus_icon": PhotoImage(file='.\\links\\antidark.png'),
    "religius_icon": PhotoImage(file='.\\links\\religiusdark.png'),
    "date_icon": PhotoImage(file='.\\links\\datedark.png'),
    "setting_icon": PhotoImage(file='.\\links\\ssd.png'),
    "btc_icon": PhotoImage(file='.\\links\\btcdark.png'),
    "translate_icon": PhotoImage(file='.\\links\\translatedark.png'),
    "qrcode_icon": PhotoImage(file='.\\links\\qrcodedark.png'),
    "search_icon": PhotoImage(file='.\\links\\searchdark.png'),
    "wether_icon": PhotoImage(file='.\\links\\wetherdark.png'),
    "todolist_icon": PhotoImage(file='.\\links\\todolistdark.png'),
    "pass_icon": PhotoImage(file='.\\links\\passdark.png'),
    "backup_icon": PhotoImage(file='.\\links\\backupdark.png'),
    "dollar_icon": PhotoImage(file='.\\links\\dollardark.png'),
}
light={
    "closebg": "#e04343",
    "closefg": "white",
    "titlebar": "#EEEEEE",
    "window_bg": "#E0E0E0",
    "activebackground": "lightgrey",
    "activeforeground": "#363A36",
    "bg": "lightgrey",
    "fg": "#363A36",
    "entrybg": "lightgrey",
    "cornometer_icon": PhotoImage(file='.\\links\\cornometer.png'),
    "startup_icon": PhotoImage(file='.\\links\\start_up.png'),
    "dns_icon": PhotoImage(file='.\\links\\dns.png'),
    "antivirus_icon": PhotoImage(file='.\\links\\anti.png'),
    "religius_icon": PhotoImage(file='.\\links\\religius.png'),
    "date_icon": PhotoImage(file='.\\links\\date.png'),
    "setting_icon": PhotoImage(file='.\\links\\ss.png'),
    "btc_icon": PhotoImage(file='.\\links\\btc.png'),
    "translate_icon": PhotoImage(file='.\\links\\translate.png'),
    "qrcode_icon": PhotoImage(file='.\\links\\qrcode.png'),
    "search_icon": PhotoImage(file='.\\links\\search.png'),
    "wether_icon": PhotoImage(file='.\\links\\wether.png'),
    "todolist_icon": PhotoImage(file='.\\links\\todolist.png'),
    "pass_icon": PhotoImage(file='.\\links\\pass.png'),
    "backup_icon": PhotoImage(file='.\\links\\backup.png'),
    "dollar_icon": PhotoImage(file='.\\links\\dollar.png'),
}
en = {
    "cornometer_text_start": "start",
    "cornometer_text_stop": "stop",
    "cornometer_text_reset": "reset",
    "Done_Massage": "Done",
    "Box_Massage": "this task completed successfully",
    "address_ask": "add the path of the folder",
    "filename_ask": "add the name of the file",
    "submit_text": "Add this app to start up",
    "Dns_adaptor_ask": "Adaptor name:",
    "dns1_ask": "DNS 1:",
    "dns2_ask": "DNS 2:",
    "Dns_desable": "Desable DNS",
    "ask_City_pr": "please add a city name in persian",
    "cornometertool": "Cornometer",
    "startuptool": "startup:add a specific app to the startup",
    "dnstool": "dns:changes systems dns",
    "antitool": "this adds a safe folder to antivirus",
    "religiustool": "gives religious times",
    "datetool": "date: gives date and events",
    "settingtool": "settings",
    "black": "Dark mode",
    "white": "Light mode",
    "farsi": "فارسی",
    "english": "English",
    "startup": "add this program to startup",
    "startup_": "do not add this program to startup",
    "langlabel": "choose a language",
    "themelabel": "choose a theme",
    "btclabel": "please add a symbol of currency:",
    "qrcodelabel": "add a text to convert into qr code",
    "qrcodemassageno": "failed to make the qr code",
    "qrcodemassage": "qr code has been made in the app folder",
    "todolisttool": "Todo List: you can add you list of tasks here",
    "dollarghymat": "The dollar price is: ",
    "sorce": "source: ",
    "searchdir": "choose a folder/drive to search",
    "search": "Search",
    "changepass": "Change password",
    "delete_text": "Delete this app from start up",
    "submit_dns": "Submit",
    "addtask": "Add task",
    "deltask": "Delete task",
    "sen": "enter the sentence",
    "copy": "Copy",
    "askfin": "add a city name to finglish",
}
fa = {
    "cornometer_text_start": "شروع",
    "cornometer_text_stop": "پایان",
    "cornometer_text_reset": "دوباره",
    "Done_Massage": "تمام",
    "Box_Massage": "عملیات با موفقیت به پایان رسید",
    "address_ask": "لطفا آدرس پوشه را وارد کنید",
    "filename_ask": "لطفا اسم برنامه را وارد کنید",
    "submit_text": "این برنامه را به استارت اپ اضافه کن",
    "Dns_adaptor_ask": "اسم اداپتور را اضافه کنید",
    "dns1_ask": "دنس یک را وارد کنید",
    "dns2_ask": "دنس دو را وارد کنید",
    "Dns_desable": "خاموش کردن دنس",
    "ask_City_pr": "نام یک شهر را به فارسی وارد کنید",
    "cornometertool": "کرنومتر",
    "startuptool": "استارت اپ",
    "dnstool": "دی ان اس",
    "antitool": "انتی ویروس",
    "religiustool": "اوقات شرعی",
    "datetool": "تاریخ",
    "settingtool": "تنظیمات",
    "black": "مود دارک",
    "white": "مود لایت",
    "farsi": "فارسی",
    "english": "اینگلیسی",
    "startup": "این برنامه را به استارت اپ اضافه کن",
    "startup_": "این برنامه را به استارت اپ اضافه نکن",
    "langlabel": "زبان برنامه را انتخاب کنید",
    "themelabel": "تم برنامه انتخاب کنید",
    "btclabel": "یک نماد از نرخ ارز را وارد کنید",
    "qrcodelabel": "جمله مورد نظر را اضافه کنید",
    "qrcodemassageno": "کد کیو ار شما دانلود نشد",
    "qrcodemassage": "کد کیو ار شما با موفقیت دانلود شد",
    "todolisttool": "لیست کارها",
    "dollarghymat": "قیمت دلار به ریال: ",
    "sorce": "منبع: ",
    "searchdir": "مسیر جستجو",
    "search": "جستجو",
    "changepass": "تغییر رمز",
    "delete_text": "این برنامه را از استارت اپ حذف کن",
    "submit_dns": "ثبت",
    "addtask": "اضافه کردن وضیفه",
    "deltask": "حذف وظیفه",
    "sen": "جمله را وارد کنید",
    "copy": "کپی",
    "askfin": "نام شهر را به فینگلیش وارد کنید",
}
