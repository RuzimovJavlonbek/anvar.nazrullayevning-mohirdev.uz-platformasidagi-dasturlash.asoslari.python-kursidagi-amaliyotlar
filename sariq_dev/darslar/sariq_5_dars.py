#Dastur haqida qisqacha  ma'lumot
print("""Bu dastur  matn va unicod  xususyatlarini  o'rganish uchun 5 dars vaqti mashq uchun  yozildi.
Muallif: Ruzimov_J
Sana: 18_06_2021
Vaqt: 11:39 \n""")
# Asosiy  ko'dlar
ism = input("Ismingizni kiriting: ")
familya = input("Familyangizni kiriting: ")

ism_sharif = f"{familya}  {ism}"

ism_sharif_katta = ism_sharif.upper()  # Gapdagi hamma so'zni  Hamma harfni katta qilib beradi
ism_sharif_katta2 = ism_sharif.lower()  # Gapdagi  hamma so'zni hamma harfini kichik qilib beradi
ism_sharif_katta3 = ism_sharif.title()  # Gapdagi hamma so'zni 1-harfini katta qilib beradi
ism_sharif_katta4 = ism_sharif.capitalize()  # Gapdagi faqat 1- so'zni birinchi harfini katta qilib beradi

ism_sharif_katta_qushimcha = f"Assalomu aleykum  {ism_sharif_katta}"
ism_sharif_katta_qushimcha2 = f"Assalomu aleykum  {ism_sharif_katta2}"
ism_sharif_katta_qushimcha3 = f"Assalomu aleykum  {ism_sharif_katta3}"
ism_sharif_katta_qushimcha4 = f"Assalomu aleykum  {ism_sharif_katta4}"

print(ism_sharif_katta_qushimcha)
print(ism_sharif_katta_qushimcha2)
print(ism_sharif_katta_qushimcha3)
print(ism_sharif_katta_qushimcha4)

# strip ko'dlari
print("Assalomu aleykum bu strip " + ism.strip() )
# strip() - bu so'zni ikki tarafidan ochiq  joyni olib tashlab eradi
# lstrip() - matn boshidan bo'shliqni o'chirish   va  rstrip()- matn ohiridan bo'shliqni o'chirish  turlari  bor

input()
