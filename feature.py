"""import requests

def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print("عکس با موفقیت دانلود شد.")
    else:
        print("خطا در دانلود عکس: ", response.status_code)

def getqrcode():
    text = input("")

    URL = "https://qr-code.ir/api/qr-code/?d=" + text

    download_image(URL,text+".png")


getqrcode()"""

import subprocess
import sys
import os
import json

try:
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
except:
    pass

drive = application_path[0]

filename = "localpycs"
searchpath = "D:\\Study\\projects"
path = application_path+"\\output.json"

if searchpath[0].lower() == drive.lower():
    command = f"cd {searchpath} && {application_path}\\tree2json.bat => {application_path}\\output.json"
else:
    command = f"{searchpath[0]}: && cd {searchpath}:// && {application_path}\\tree2json.bat => {application_path}\\output.json"

result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

main_string = str(data)
search_string = filename

start = 0
poslist = []
while start < len(main_string):
    position = main_string.find(filename, start)
    if position != -1:
        poslist.append(position)
        start = position + 1
    else:
        break

# position = main_string.find(search_string)
# position += len(search_string)+4

endpos_list = []
for i in poslist:
    i += len(filename)+4
    end_pos = main_string[i:i+512]
    endposition = end_pos.find(",")
    if main_string[i:i+endposition].find("path") != -1:
        print(main_string[i:i+endposition])
    


# print(main_string[position:position+endposition])
             




