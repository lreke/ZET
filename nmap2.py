
import os

# Gerekli paketi yükle
os.system("pkg install nmap -y")
os.system("clear")

def menu():
    print("""
    ----------------------------
            NMAP MENU
    ----------------------------
    
    0 - Basit Nmap Taraması
    1 - Servis ve Sürüm Bilgisi (-sC -sV)

    ----------------------------
    """)


menu()


ip = input("Lütfen IP adresini giriniz: ").strip()
islem_no = input("Lütfen işlem numarasını giriniz (0 veya 1): ").strip()


if islem_no == "0":
    os.system("nmap " + ip)
elif islem_no == "1":
    os.system("nmap -sC -sV " + ip)
else:
    print("Geçersiz işlem numarası girdiniz.")

