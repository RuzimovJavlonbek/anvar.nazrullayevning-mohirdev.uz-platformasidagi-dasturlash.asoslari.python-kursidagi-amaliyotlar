from math import*
a = float(input(" Biror butun son kiriting >>> "))

while ceil(a) > a:
  a = float(input(" Siz butun son kiritmadingiz! \n Iltimos qayta biror bir butun son kiriting >>> "))

print(" Raxmat sonni  to'g'ri kiritdingiz. ")

a = int(a)
for i in range(2, 11):
  if a%i==0:
    print( a , " soni " , i ," ga  qoldiqsiz bo'linadi. " )

input()
