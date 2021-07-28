mahsulotlar = ['non', 'shakar','qand','olma','gugurt','pechenya', 'shapka', 'papka', 'shim', "ko'ylak", 'malibu2']

savat = []

n = int(input("Tahminan  nechta mahsulot harid qilmoqchisiz? >>>> "))
while n<5:
  n = int(input(" \nMahsulotlar soni 5 dankam bo'lmasin. \n Qayta kiriting. Tahminan  nechta mahsulot harid qilmoqchisiz? >>>> "))

for i in range(n):
  b = savat.append(input(f"{i+1} - mahsulotni kiriting. "))

if savat:
  for savatdagi in savat:
    if savatdagi in mahsulotlar:
      print(f" {savatdagi} do'konimizda bor. ")
    else:
      print(f" {savatdagi} do'konimizda yo'q. ")

else:
  print("Savatingiz bo'sh.")

input()
