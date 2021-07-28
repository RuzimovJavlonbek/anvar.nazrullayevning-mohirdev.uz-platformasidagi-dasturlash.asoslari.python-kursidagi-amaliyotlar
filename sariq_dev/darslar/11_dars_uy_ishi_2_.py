yosh = int(input("Yoshingiz nechida ? >>>>"))

if yosh < 4 or yosh >60:
  narh = 0
elif yosh <=18:
  narh = 10000
elif yosh >18:
  narh = 20000

print(f" Sizga kirish {narh} so'm.  ")
input()
