import hashlib
import base64
import os

def menu():
    os.system("clear")
    print("""
    ============================
       ŞİFRE KRİPTOLAMA ARACI
    ============================
    1 - SHA256 ile şifrele
    2 - MD5 ile şifrele
    3 - Base64 ile şifrele
    0 - Çıkış
    """)

def sha256_encrypt(text):
    return hashlib.sha256(text.encode()).hexdigest()

def md5_encrypt(text):
    return hashlib.md5(text.encode()).hexdigest()

def base64_encrypt(text):
    return base64.b64encode(text.encode()).decode()

while True:
    menu()
    secim = input("Seçiminizi girin: ")

    if secim == "0":
        print("Çıkılıyor...")
        break

    sifre = input("Şifre girin: ")

    if secim == "1":
        print("\nSHA256:", sha256_encrypt(sifre))
    elif secim == "2":
        print("\nMD5:", md5_encrypt(sifre))
    elif secim == "3":
        print("\nBase64:", base64_encrypt(sifre))
    else:
        print("\nGeçersiz seçim.")

    input("\nDevam etmek için Enter'a bas...")
