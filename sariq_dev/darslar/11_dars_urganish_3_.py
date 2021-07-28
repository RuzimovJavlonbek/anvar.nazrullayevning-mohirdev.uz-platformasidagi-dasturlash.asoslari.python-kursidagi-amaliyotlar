kun = input("Bugun nima kun?>>>")
harorat = float(input("Havo harorati qanday?>>>"))
if (kun.lower() == "yakshanba" or kun.lower() == "shanba") and harorat >= 30:
  print("Cho'milgani ketdik? ")
elif (kun.lower() == "yakshanba" or kun.lower() == "shanba") and harorat < 30:
  print(" Uyda dam olamiz! ")
input()
