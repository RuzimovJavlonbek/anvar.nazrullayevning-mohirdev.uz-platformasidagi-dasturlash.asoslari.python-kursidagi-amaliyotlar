a = 5
print( a!=6)

ism = input("Ismingizni kiritng>\n>>")

if ism.lower() != 'ali' :
  print(f"Uzr {ism.capitalize()} biz Alini kutyabmiz! ")
else:
  print(" SAlom Ali.")

javob = float(input("\n\n\n 12*6 nechaga teng?"))

if javob !=72:
  print("JAvob xato. ")


yosh = int(input("\n\n\nYoshingiz nechida? >>> "))

if yosh >=18:
  print("Xush kelibsiz! ")
else:
  print("Kirish mumkin emas! ")




login = input("Yangi lgin tanlang:  ")

if len(login) <=5:
  print("Login 5 harfdan  ko'proq bo'lishi shart ")


x, y = 25, 50

print("x>y")  if x>y  else print("x<y")



input()
