
import requests

url = input("Fayl havolasini kiriting: ")

ruxsat = [".mp3", ".mp4", ".pdf", ".png", ".jpg", ".jpeg", ".webp"]

fayl_nomi = url.split("/")[-1].split("?")[0]
kengaytma = "." + fayl_nomi.split(".")[-1].lower()

if kengaytma not in ruxsat:
    print("Xatolik: Bu fayl formati qo'llab-quvvatlanmaydi!")
    print("Ruxsat etilgan formatlar: mp3, mp4, pdf, png, jpg, jpeg, webp")

else:
    print("Fayl turi:", kengaytma[1:].upper())
    print("Yuklab olinmoqda...")

    try:
        response = requests.get(url, timeout=30)

        if response.status_code == 200:
            with open("downloads/" + fayl_nomi, "wb") as fayl:
                fayl.write(response.content)

            print("Fayl muvaffaqiyatli yuklandi!")
            print("Saqlangan fayl: downloads/" + fayl_nomi)

        else:
            print("Faylni yuklab bo'lmadi!")
            print("URL manzilni tekshiring yoki fayl mavjud emas.")

    except requests.exceptions.RequestException:
        print("Faylni yuklab bo'lmadi!")
        print("URL manzilni tekshiring yoki fayl mavjud emas.")
