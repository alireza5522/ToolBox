import json
import sys
import os

with open('settings.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

if data["settings"]["startup"] == True:
    try:
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))
    except:
        pass
else:
    ...

print(application_path)
