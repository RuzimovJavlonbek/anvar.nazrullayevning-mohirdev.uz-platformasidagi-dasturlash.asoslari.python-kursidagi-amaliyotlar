ism = input("Isnigiz kim? >> ")
login = input("Loginingizni kiriting? >> ")

if login.title() == 'Admin':
  print(" Xush kelibsiz {}  {} . \n Foydalanuvchilar ro'yhatini ko'rasizmi? ".format(login,ism))
else:
  print(" Xush kelibsiz {} .".format(ism))

input()


