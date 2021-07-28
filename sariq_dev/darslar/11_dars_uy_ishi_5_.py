mahsulotlar = ['non', 'shakar', 'qand', 'olma', 'gugurt','pechenya', 'shapka', 'papka', 'shim', "ko'ylak", 'malibu2']

savat = []
bor_mahsulotlar = []
mavjud_emas = []

n = int(input("Tahminan  nechta mahsulot harid qilmoqchisiz? >>>> "))
while n < 5:
  n = int(input(" \nMahsulotlar soni 5 dankam bo'lmasin. \n Qayta kiriting. Tahminan  nechta mahsulot harid qilmoqchisiz? >>>> "))

for i in range(n):
  b = savat.append(input(f"{i+1} - mahsulotni kiriting. "))

if savat:
  for savatdagi in savat:
    if savatdagi in mahsulotlar:
      print(f" {savatdagi} do'konimizda bor. ")
      bor_mahsulotlar.append(savatdagi)
    else:
      print(f" {savatdagi} do'konimizda yo'q. ")
      mavjud_emas.append(savatdagi)
      
if len(mavjud_emas) ==0:
  print(" \nSiz so'ragan barcha mahsulot do'konimizda bor. ")
else:
  print("\n Quydagi mahsulotlar do'konimizda yo'q: ")
  for yuqlari in mavjud_emas:
    print(yuqlari)



input()
