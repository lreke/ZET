import socket
import requests
import os
import time



os.system("pip install requests")
os.system("clear")


def tekli_ip_bul():
    site = input("\nSite adresi girin (örnek: google.com): ").strip()
    try:
        ip = socket.gethostbyname(site)
        print(f"{site} adresinin IP'si: {ip}\n")
    except socket.gaierror:
        print("Hata: Site bulunamadı veya geçersiz.\n")

def ip_konum_bilgisi():
    site = input("\nKonum bilgisi alınacak siteyi girin (örnek: google.com): ").strip()
    try:
        ip = socket.gethostbyname(site)
        print(f"{site} IP: {ip}")
        
        # IP konum bilgisi çekiliyor
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()

        if data["status"] == "success":
            print(f"""
📍 Ülke: {data['country']}
🏙️  Şehir: {data['city']}
🌐  ISP (Sağlayıcı): {data['isp']}
🏢  Kuruluş: {data['org']}
🧭  Bölge: {data['regionName']}
🕒  Saat Dilimi: {data['timezone']}
📮  Posta Kodu: {data['zip']}
            """)
        else:
            print("Konum bilgisi alınamadı.")
    except socket.gaierror:
        print("Hata: Geçersiz site adresi.\n")
    except Exception as e:
        print(f"Hata oluştu: {e}")

def cikis():
    print("\nÇıkılıyor...")
    time.sleep(1)
    exit()

def menu():
    while True:
        print("""
==============================
     🔎 IP BULMA MENÜSÜ      
==============================
[1] Tek Site IP Bul
[2] IP Konum Bilgisi Getir
[3] Çıkış
==============================
        """)

        secim = input("Seçiminizi yapın (1-3): ").strip()

        if secim == "1":
            tekli_ip_bul()
        elif secim == "2":
            ip_konum_bilgisi()
        elif secim == "3":
            cikis()
        else:
            print("Geçersiz seçim! Lütfen 1-3 arasında bir değer girin.\n")

menu()