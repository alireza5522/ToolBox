import requests

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


getqrcode()



