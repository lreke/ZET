
import os

dogru_sifre = "zetronciern"

# Şifre kontrolü
girilen_sifre = input("🔐 Lütfen şifreyi girin: ").strip()

if girilen_sifre != dogru_sifre:
    print("❌ Hatalı şifre! Erişim reddedildi.")
    exit()

def figlet():
    os.system("apt-get install figlet")
    os.system("clear")
    os.system("figlet zetron")

figlet()


def menu():
    print("""
    ----------------------------
            ZETRON MENU
    ----------------------------
    
    0 - NMAP
          
    1 - ŞİFRE KRİPTOLAMA

    2 - PFOZ
    
    3 - ZENIP
    ----------------------------
    """)


menu()

islem_no = input("Lütfen işlem numarasını giriniz (0 veya 1): ").strip()


if islem_no == "0":
    os.system("python nmap2.py")
elif islem_no == "1":
    os.system("python KRIPTOLAMA.py")
elif islem_no == "2":
    os.system("python pfoz.py")
elif islem_no == "3":
    os.system("python zenıp.py")
else:
    print("Geçersiz işlem numarası girdiniz.")