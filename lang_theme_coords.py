from tkinter import PhotoImage
class coordinates:
    Main_Window_H,Main_Window_W = (210,255) #40#55+10
    cornometer_button_x,cornometer_button_y = (15,45)
    startup_button_x,startup_button_y = (15,85)
    dns_button_x,dns_button_y = (15,125)
    antivirus_button_x,antivirus_button_y = (15,165)
    setting_button_x,setting_button_y = (15,205)
    Religiustimes_button_x,Religiustimes_button_y = (80,45)
    date_button_x,date_button_y = (80,85)
    btc_button_x,btc_button_y = (80,125)
    translate_button_x,translate_button_y = (80,165)
    qrcode_button_x,qrcode_button_y = (80,205)
    search_button_x,search_button_y = (145,45)

    cornometer_H,cornometer_W = (250,250)
    time_text_x,time_text_y = (100,30)
    start_button_x,start_button_y = (100,100)
    stop_button_x,stop_button_y = (100,125)
    reset_button_x,reset_button_y = (100,150)

    startup_W,startup_H = (250,250)
    startup_label1_x,startup_label1_y = (10,30)
    startup_entry1_x,startup_entry1_y = (10,50)
    startup_label2_x,startup_label2_y = (10,100)
    startup_entry2_x,startup_entry2_y = (10,125)
    startup_submit_x,startup_submit_y = (10,150)
    
    dns_W,dns_H = (250,250)
    dns_label1_x,dns_label1_y = (10,30)
    dns_entry1_x,dns_entry1_y = (10,50)
    dns_label2_x,dns_label2_y = (10,100)
    dns_entry2_x,dns_entry2_y = (10,125)
    dns_label3_x,dns_label3_y = (10,150)
    dns_entry3_x,dns_entry3_y = (10,175)
    dns_submit1_x,dns_submit1_y = (10,200)
    dns_submit2_x,dns_submit2_y = (10,225)

    antivirus_W,antivirus_H = (250,250)
    antivirus_label1_x,antivirus_label1_y = (10,30)
    antivirus_entry1_x,antivirus_entry1_y = (10,50)
    antivirus_label2_x,antivirus_label2_y = (10,100)
    antivirus_entry2_x,antivirus_entry2_y = (10,125)
    antivirus_button1_x,antivirus_button1_y = (10,150)
    antivirus_button2_x,antivirus_button2_y = (50,150)
    antivirus_button3_x,antivirus_button3_y = (100,150)
    antivirus_submit_x,antivirus_submit_y = (10,175)

    religius_W,religius_H = (250,250)
    Religiustimes_label1_x,Religiustimes_label1_y = (10,40)
    Religiustimes_entry1_x,Religiustimes_entry1_y = (10,70)
    Religiustimes_submit_x,Religiustimes_submit_y = (10,100)
    Religiustimes_label2_x,Religiustimes_label2_y = (10,130)

    date_W,date_H = (350,350)
    date_label1_x,date_label1_y = (-50,50)

    setting_W,setting_H = (350,350)
    settings_label1_x,settings_label1_y = (10,40)
    settings_button1_x,settings_button1_y = (10,60)
    settings_button2_x,settings_button2_y = (10,80)
    settings_label2_x,settings_label2_y = (10,100)
    settings_button3_x,settings_button3_y = (10,120)
    settings_button4_x,settings_button4_y = (10,140)
    settings_button5_x,settings_button5_y = (10,160)
    settings_button6_x,settings_button6_y = (10,180)
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
    "setting_icon": PhotoImage(file='.\\links\\settingdark.png'),
    "btc_icon": PhotoImage(file='.\\links\\btcdark.png'),
    "translate_icon": PhotoImage(file='.\\links\\translatedark.png'),
    "qrcode_icon": PhotoImage(file='.\\links\\qrcodedark.png'),
    "search_icon": PhotoImage(file='.\\links\\searchdark.png')
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
    "setting_icon": PhotoImage(file='.\\links\\setting.png'),
    "btc_icon": PhotoImage(file='.\\links\\btc.png'),
    "translate_icon": PhotoImage(file='.\\links\\translate.png'),
    "qrcode_icon": PhotoImage(file='.\\links\\qrcode.png'),
    "search_icon": PhotoImage(file='.\\links\\search.png')
}
en = {
    "cornometer_text_start": "start",
    "cornometer_text_stop": "stop",
    "cornometer_text_reset": "reset",
    "Done_Massage": "Done",
    "Box_Massage": "Complited",
    "address_ask": "give me address",
    "filename_ask": "give me file",
    "submit_text": "submit",
    "Dns_adaptor_ask": "add adaptor name",
    "dns1_ask": "add dns 1",
    "dns2_ask": "add dns 2",
    "Dns_desable": "desable dns",
    "ask_City_pr": "add city to persion",
    "cornometertool": "cornometer",
    "startuptool": "startup:add's an specified app to the startup",
    "dnstool": "dns:changes systems dns",
    "antitool": "add's a safe file/folder to anti virus",
    "religiustool": "give a religius times",
    "datetool": "date",
    "settingtool": "settings",
    "black": "darkmode",
    "white": "lightmode",
    "farsi": "persian",
    "english": "english",
    "startup": "add this program to startup",
    "startup_": "do not add this program to startup",
    "langlabel": "choose a languge",
    "themelabel": "choose a theme"
}
fa = {
    "cornometer_text_start": "شروع",
    "cornometer_text_stop": "پایان",
    "cornometer_text_reset": "دوباره",
    "Done_Massage": "تمام",
    "Box_Massage": "عملیات به پایان رسید",
    "address_ask": "ادرس فایل را وارد کنید",
    "filename_ask": "اسم فایل را وارد کنید",
    "submit_text": "ثبت",
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
    "themelabel": "تم برنامه انتخاب کنید"
}
