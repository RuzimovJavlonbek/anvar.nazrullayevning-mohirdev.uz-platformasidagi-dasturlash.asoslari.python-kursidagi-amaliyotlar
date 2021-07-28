mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]

narhlar = [12000,18000,10900,22000,25000,36000,-25, 63.2]

narhlar.remove(-25)
narhlar.remove(63.2)
narhlar[0] = narhlar[0] + 1000

sonlar = ['bir', 'ikki uch', 3, 4, 5]

ismlar = []
ismlar.append('javlonbek')
ismlar.append('jaxongir')
ismlar.append('sarvar')
ismlar.append('lochin')
ismlar.append('sardor')
ismlar.append('jumong')
ismlar.append('dabdaba')

del ismlar[0]

mevalar[0] = 'anor'

mevalar [-1] = 'uzum'

mevalar.append('tarvuz')
mevalar.append('qovun')
mevalar.insert(0, 'banana')
mevalar.insert(3, 'annaanas')
del mevalar[-1]

ismlar.remove("lochin")
ismlar.remove("jumong")


print(len(mevalar))

print(mevalar)
print(narhlar)
print(sonlar)
print(ismlar)


print(mevalar[0].upper())
print(mevalar[2])

print(mevalar[-1].title())


print(sonlar[-1])


print(narhlar[0]+narhlar[1])

input()
