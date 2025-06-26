import phonenumbers
from phonenumbers import geocoder, carrier

numara = input("Telefon numarasını uluslararası formatta gir (örn: +905xxxxxxxxx): ")
try:
    parsed_num = phonenumbers.parse(numara)
    ulke = geocoder.description_for_number(parsed_num, "tr")
    operator = carrier.name_for_number(parsed_num, "tr")
    print(f"Numara ülke: {ulke}")
    print(f"Operatör: {operator}")
except Exception as e:
    print("Geçersiz numara veya format hatası.")