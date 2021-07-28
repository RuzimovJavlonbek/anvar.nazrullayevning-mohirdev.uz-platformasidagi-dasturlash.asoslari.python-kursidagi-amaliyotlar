#ismlar = ["Javlonbek", 'Bobur', 'Jaxongir', 'Umidjon ', 'Oxun', 'Abduraxmon']
#sonlar = [9,45,780,32,1,0,78,]
#print(sonlar)
#print(sorted(sonlar,reverse = True))
#sonlar.reverse()
#print(sonlar)
#print(sorted(sonlar))
#print(ismlar)
#print(sorted(ismlar))
#print(ismlar)

'''
sonlar = list(range(0,10))
print(sonlar)
max_qiymat = max(sonlar)
min_qiymat= min(sonlar)
print(max_qiymat)
print(min_qiymat)
print(sum(sonlar))
'''
#===========================================================================
'''
narhlar = [12000,22500,23456,9800,5600,9934,32874]

print("\n", narhlar, "\n")

arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)

print (" Eng arzon narh " , arzon , " . Eng qimmati  " , qimmat ,".  Jami:  " , jami)

'''
#================================================================


# =============== Ro'yxatni  ko'pya qilish===============
'''
cars = ['bmw' , 'mercedes benz' , 'volvo' , 'gm' , 'tesla' , 'audi']

my_cars = list(cars)


my_cars.remove('bmw')

print(cars)

print(my_cars)

'''
#==============================Tupl =============================
'''
toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
toys = list(toys)
toys[0] = "salom"

toys = tuple(toys)

print(toys)
'''

sonlar_1 = list(range(1980,2001))
print(sonlar_1)

#for x in sonlar_1:
 # print(x)

#if 19978 in sonlar_1:
  #print("Siz shu yil tugilgansiz")
#else:
  #print("YIL  yo'q")

#eng_arzon = min(sonlar_1)
#Eeng_qimmat = max(sonlar_1)


#print("\n\n\n" , eng_arzon, " , " , eng_qimmat)

my_son  = sonlar_1[11:]
print(my_son)


input()
