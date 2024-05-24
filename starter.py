import json
import sys
import os
import subprocess

def cmd(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result

try:
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
except:
    ...

with open('settings.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

if data["settings"]["startup"] == True:
    x = cmd(f"{application_path}\\tree2json.bat")
    print(x)
else:
    ...
