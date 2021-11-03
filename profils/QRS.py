import qrcode
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

def get_img(CIN):
    BASE_DIR = Path(__file__).resolve().parent.parent
    print(BASE_DIR)
    
    print("i m here !!!!")
    img = qrcode.make(f"https://4a54-102-157-48-231.ngrok.io/profile/{CIN}/")
    print("1")
    img.save(BASE_DIR / 'QR_imgs' / f"{CIN}.jpg")
    print("2")
    
    print(f"QR Code saved in ./qrs/{CIN}.jpg")
    
    return str(BASE_DIR / 'QR_imgs' / f"{CIN}.jpg")

