mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat = []

for n in range(5):
  savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
  for mahsulot in savat:
    if mahsulot in mahsulotlar:
      print(f"Do'konimizda {mahsulot} bor")
    else:
      print(f"Do'konimizda {mahsulot} yo'q")

else:
  print("Savatingiz bo'sh")
input()
