print("             Assalomun aleykum bu mening birinchi loyiham! \n")
print("         Bu loyiha kichik bir restoran uchun hisob kitob dasturi.\n")

hisob = 0
print("Mijoz nimalarni oldi?>>> \n\n Menyudan mos  raqamni tanlang>>>\n\n Choy -            1. - 2000 so'm \n Non -             2. - 2000 so'm \n So'msa -          3. - 5000 so'm \n Palov -           4. - 15000 so'm \n Shashlik -        5. - 10000 so'm \n Ko'fe -           6. - 2500 so'm \n  Perashka -       7. - 1000 so'm \n Pelmen -          8. - 7000 so'm \n Qovurma lag'mon - 9. - 8000 so'm \n Ko'ka - ko'la -   10. - 8000 so'm  ")

c = True
while c:
  if hisob == 0:
    n = int(input("\n Mijoz nima buyurdi?>>  "))

    if n == 1:
      print(" Choy:  2000 so'm")
      hisob += 2000
      print(" HOZIRCHA  HISOB: =  ", hisob ,"  so'm ")

      d = input(" \n Agar shu bn tugagan bo'lsa =  ni bosing   tugamagan bo'lsa   +  ni bosib davom eting. >>  ")
      if d.lower() == '=':
        c = False
      elif d.lower() == "+":
        c = True


    if n == 2:
      print(" Non:  2000 so'm")
      hisob += 2000
      print(" HOZIRCHA  HISOB: =  ", hisob,  "  so'm ")

      d = input(" \n Agar shu bn tugagan bo'lsa =  ni bosing   tugamagan bo'lsa   +  ni bosib davom eting. >>  ")
      if d.lower() == '=':
        c = False
      elif d.lower() == "+":
        c = True


    if n == 3:
      print(" So'msa:  5000 so'm")
      hisob += 3000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")

      d = input(" \n Agar shu bn tugagan bo'lsa =  ni bosing   tugamagan bo'lsa   +  ni bosib davom eting. >>  ")
      if d.lower() == '=':
        c = False
      elif d.lower() == "+":
        c = True



    if n == 4:
      print(" Palov:  15000 so'm")
      hisob += 15000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")


      d = input(" \n Agar shu bn tugagan bo'lsa =  ni bosing   tugamagan bo'lsa   +  ni bosib davom eting. >>  ")
      if d.lower() == '=':
        c = False
      elif d.lower()=="+":
        c = True



    if n == 5:
      print("Shashlik:  10000 so'm")
      hisob += 10000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")


      d = input(" \n Agar shu bn tugagan bo'lsa =  ni bosing   tugamagan bo'lsa   +  ni bosib davom eting. >>  ")
      if d.lower() == '=':
        c = False
      elif d.lower()=="+":
        c = True


    if n == 6:
      print(" Ko'fe:  2500 so'm")
      hisob += 2500
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")


      d = input(" \n Agar shu bn tugagan bo'lsa =  ni bosing   tugamagan bo'lsa   +  ni bosib davom eting. >>  ")
      if d.lower() == '=':
        c = False
      elif d.lower()=="+":
        c = True



    if n == 7:
      print(" Perashka:  1000 so'm")
      hisob += 1000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")

      d = input(" \n Agar shu bn tugagan bo'lsa =  ni bosing   tugamagan bo'lsa   +  ni bosib davom eting. >>  ")
      if d.lower() == '=':
        c = False
      elif d.lower() == "+":
        c = True



    if n == 8:
      print(" Pelman:  2000 so'm")
      hisob += 2000

      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")



      d = input(" \n Agar shu bn tugagan bo'lsa =  ni bosing   tugamagan bo'lsa   +  ni bosib davom eting. >>  ")
      if d.lower() == '=':
        c = False
      elif d.lower()=="+":
        c = True


    if n == 9:
      print(" Qovurma lag'mon:  2000 so'm")
      hisob += 2000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")


      d = input(" \n Agar shu bn tugagan bo'lsa =  ni bosing   tugamagan bo'lsa   +  ni bosib davom eting. >>  ")
      if d.lower() == '=':
        c = False
      elif d.lower()=="+":
        c = True



    if n == 10 :
      print("Ko'ka - ko'la:  8000 so'm")
      hisob += 8000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")

      d = input(" \n Agar shu bn tugagan bo'lsa =  ni bosing   tugamagan bo'lsa   +  ni bosib davom eting. >>  ")
      if d.lower() == '=':
        c = False
      elif d.lower()=="+":
        c = True


#====================================================
  elif hisob > 0:
    n = int(input("\nMijoz yana nima buyurdi?>>  "))

    if n == 1:
      print(" Choy:  2000 so'm")
      hisob += 2000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")

      d = input(" \n Agar shu bn tugagan bo'lsa =  ni bosing   tugamagan bo'lsa   +  ni bosib davom eting. >>  ")
      if d.lower() == '=':
        c = False
      elif d.lower()=="+":
        c = True

    if n == 2:
      print(" Non:  2000 so'm")
      hisob += 2000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")

      d = input(" \n Agar shu bn tugagan bo'lsa =  ni bosing   tugamagan bo'lsa    +  ni yozing.  ")
      if d.lower() == '=':
        c = False
      elif d.lower() == "+":
        c = True


    if n == 3:
      print(" So'msa:  5000 so'm")
      hisob += 3000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")

      d = input(" \n Agar shu bn tugagan bo'lsa  =  ni bosing   tugamagan bo'lsa    +  ni yozing.  ")
      if d.lower() == '=':
        c = False
      elif d.lower() == "+":
        c = True

    if n == 4:
      print(" Palov:  15000 so'm")
      hisob += 15000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")
      d = input(" \n Agar shu bn tugagan bo'lsa  =  ni bosing   tugamagan bo'lsa    +  ni yozing.  ")
      if d.lower() == '=':
        c = False
      elif d.lower() == "+":
        c = True


    if n == 5:
      print("Shashlik:  10000 so'm")
      hisob += 10000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")

      d = input(" \n Agar shu bn tugagan bo'lsa  =  ni bosing   tugamagan bo'lsa    +  ni yozing.  ")
      if d.lower() == '=':
        c = False
      elif d.lower() == "+":
        c = True

    if n == 6:
      print(" Ko'fe:  2500 so'm")
      hisob += 2500
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")

      d = input(" \n Agar shu bn tugagan bo'lsa  =  ni bosing   tugamagan bo'lsa    +  ni yozing.  ")
      if d.lower() == '=':
        c = False
      elif d.lower() == "+":
        c = True


    if n == 7:
      print(" Perashka:  1000 so'm")
      hisob += 1000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")

      d = input(" \n Agar shu bn tugagan bo'lsa  =  ni bosing   tugamagan bo'lsa    +  ni yozing.  ")
      if d.lower() == '=':
        c = False
      elif d.lower()=="+":
        c = True

    if n == 8:
      print(" Pelman:  12000 so'm")
      hisob += 2000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")

      d = input(" \n Agar shu bn tugagan bo'lsa  =  ni bosing   tugamagan bo'lsa    +  ni yozing.  ")
      if d.lower() == '=':
        c = False
      elif d.lower()=="+":
        c = True


    if n == 9:
      print(" Qovurma lag'mon:  8000 so'm")
      hisob += 2000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")
      d = input(" \n Agar shu bn tugagan bo'lsa  =  ni bosing   tugamagan bo'lsa    +  ni yozing.  ")
      if d.lower() == '=':
         c = False
      elif d.lower() == "+":
          c = True


    if n == 10:
      print("Ko'ka - ko'la:  8000 so'm")
      hisob += 8000
      print(" HOZIRCHA  HISOB: =  ", hisob, "  so'm ")

      d = input(" \n Agar shu bn tugagan bo'lsa  =  ni bosing   tugamagan bo'lsa    +  ni yozing.  ")
      if d.lower() == '=':
        c = False
      elif d.lower() == "+":
        c = True


print("\n\nJAMI  HISOB: ", hisob, "  so'm ")

print("\n\n\n by: RUZIMOV_Javlonbek")

input()
