#denna uppgidt ska man öva variabler, vilkor och loopar
import random
import os
os.system("cls" if os.name == "nt" else "clear")

print ("\n----------------------------------------")
print (".:gissatalet:.\n\n")

print ("gissa ett tal mellan 1 och 10 och pröva lyckan, du får 3st försök!\n")
slumptal = random.randrange (1, 10)
#print (slumptal)
i = 0
hittat = False
#loop
while i < 3:
    gissatal =input("mata in tal: " )

    if slumptal == int(gissatal) :
        hittat = True
        print("\n rätt svar! \n")
        break

    i += 1

    if hittat :
        print ("\n Bra jobbat, du har vunnit en fot-massage")
    else:
        print ("\n fel! du suger")

    print("\n------------------------------------------------")
