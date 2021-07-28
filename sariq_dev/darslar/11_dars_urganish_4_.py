narh = 15000
salat = True
choy = False

if salat and choy:
  narh +=10000
elif salat or choy:
  narh += 5000
print("Natija: ",narh)

input()
