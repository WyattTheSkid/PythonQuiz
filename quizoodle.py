#Part I
name = ""
day = ""
month = ""
year = ""
usrage = 0
current_year = 2022
usrBornIn = 0
ffood = ""
fanimal = ""
tg1 = 0
tg2 = 0
tg3 = 0
tgall = 0
tgavg = 0
name = input("what is your name?: ")
print ("hello there,"+ " " + name + " " + "nice to meet you!")
day = input("what day is it?: ")
print ("so today is "+day+" cool.")
usrage = input("how old are you "+name+"?"+": ")
try:
    int(usrage)
    isvalidage = True
except ValueError:
    isvalidage = False
    print("that's not a number stupid.")
#print(isvalidage) #debug
if isvalidage == True:
   usrBornIn = (int(current_year)) - (int(usrage))
   print("so you were born in "+(str(usrBornIn))+" "+"or"+" "+(str(usrBornIn-1))+".")
   print("")
   ffood = input("hey "+name+", what's your favorite food"+"?"+": ")
   print("ah yes, "+ffood+" "+"that's one of my favorites as well!")
   fanimal = input("What about your favorite animal"+"?"+": ")
   if fanimal == "spiders":
      print("")
      print("                          ಠ_ಠ      ")
      print("")
      print("ok this conversation is over we can't be friends anymore.")
   else:
      print("I really like "+fanimal+"s "+"too they're really cute :)") 
      tg1 = input("so what was your first test grade"+"?"+": ")
      tg2 = input("and your second"+"?"+": ")
      tg3 = input("and lastly, what about your third"+"?"+": ")
      tgall = (int(tg1)+int(tg2)+int(tg3))
      tgavg = tgall/3
      print (int(tgavg))
      if tgavg < 50:
       print("only a "+tgavg+"? thats not great...")
      elif tgavg > 70:
        print("heyyyy a "+(str(tgavg))+" thats not too shabby my friend.")
      else:
         print("hmmph. a"+(str(tgavg))+"it is what it is.")
elif isvalidage == False:
       print("we'll try this again another time...")

