menu = ['osh' , 'qazonkabob', 'shashlik' , 'norin','somsa']
buyurtmalar = ['osh' , 'somsa', 'manti' , 'shashlik']

if buyurtmalar:
  for taom in buyurtmalar:
    if taom in menu:
      print(f" Menuda {taom} bor. ")
    else:
      print(f"Kechirasiz , menuda  {taom} yo'q.")

else:
  print("Savatchangiz bo'sh.  ")

input()
