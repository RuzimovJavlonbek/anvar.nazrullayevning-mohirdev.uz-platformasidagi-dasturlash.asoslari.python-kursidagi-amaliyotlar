#=========================== 1- UY ISHI =============================================
'''
malum_davlat = ["O'zbekiston" , "Rossiya" , "Xitoy" ,"Norvegiya", "Amerika Qo'shmash Shtatlar", "Kanada" , "Buyuk Britanya" , "Afg'oniston"]
print(malum_davlat)

print(len(malum_davlat))
print(sorted(malum_davlat))
print(" \n\n", sorted(malum_davlat ,reverse=True))

print("\n\n\n" , malum_davlat)

malum_davlat.reverse()

print("\n\n",malum_davlat)

malum_davlat.sort()
print("\n\n\n",malum_davlat)

malum_davlat.reverse()
print(malum_davlat)
'''

#=========================== 2- UY ISHI =============================================
'''
juft_sonlar =list(range(120,12001 , 2))
print(sum(juft_sonlar))

eng_kichik = min(juft_sonlar)
eng_katta = max(juft_sonlar)
print(eng_katta , " \n" , eng_kichik)

print(" \nNatija: " , eng_katta - eng_kichik , "\n Elemntlar soni: =  " , len(juft_sonlar)//2)

print("\n\n",juft_sonlar[:21])
print("\n\n",juft_sonlar[2970:2991])
print("\n\n",juft_sonlar[-21:])

'''
#=========================== 3- UY ISHI Taomlar =============================================

taomlar = ["qovrilgan tuxum", "somsa", "gril", "shashlik", "fitchi"]

nonushta = taomlar[:]

del nonushta[2]
del nonushta[2]
nonushta.append("osh")
nonushta.append("tandir kabob")

print(taomlar)

print(" \n" , nonushta)

nonushta = tuple(nonushta)

nonushta[0] = "qaymoq va non"

input()
