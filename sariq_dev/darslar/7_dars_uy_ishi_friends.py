dust = []

dust.append("Bobur")
dust.append("Sarvar")
dust.append("Javlonbek")
dust.append("Umidjon")
print(dust)

dust.remove("Javlonbek")
print(dust)

dust.insert(0, "Oxunjon")
dust.insert(-1, "Sardor")
print(dust)


yangi_mehmonlar = []
print(yangi_mehmonlar)

keldi1 =dust.pop(0)
keldi2 =dust.pop(1)
keldi3 =dust.pop(2)

yangi_mehmonlar.append(keldi1)
yangi_mehmonlar.append(keldi2)
yangi_mehmonlar.append(keldi3)
print(yangi_mehmonlar)
print(dust)

input()
