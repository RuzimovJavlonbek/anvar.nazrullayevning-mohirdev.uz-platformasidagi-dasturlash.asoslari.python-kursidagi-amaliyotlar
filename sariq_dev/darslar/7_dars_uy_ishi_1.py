ismlar = ["Abror", "Botir" , " Javlonbek", "Mahmud"]
print(ismlar)

print("\n\nSalom " , ismlar[0] ," bugun choyhona bormi.? \n", ismlar[3] , " choyhonaga boramizmi ? ")
# Sonlar degan ruyxat

sonlar  = [ 89 , -5, 2.1 , -6.4 ]

print(sonlar)
print(sum(sonlar))

c = sonlar[0] + sonlar[1]

print(c)

sonlar[2] = 1000

print(sonlar)

a = sonlar[2]
sonlar[2] = sonlar[0]
sonlar[0] = a

print(sonlar)

del sonlar[0]

print(sonlar , " ,  " , sonlar[0])







input()