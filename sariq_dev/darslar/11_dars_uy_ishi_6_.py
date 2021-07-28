foydalanuvchilar = ['java', 'javlonbek', 'adham', "bo'rya",'sasha']

login = input(" Yangi login kiriting. >>>>  ")

c= True
while login.lower() in foydalanuvchilar:
  print("\nBu login band , yangi lgin tanlang ! ")
  login = input(" Yangi login kiriting. >>>>  ")

else:
  print(f"\n Xush kelibsiz ! {login} ")

print("\n\n\n by: Ruzmov_Javlonbek")

input()
