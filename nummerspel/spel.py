



print("Välkommen! Innan vi börjar spelet, ange era spelar namn. Vad heter du spelare 1?")
player1=input()
print("Hej", (player1), ", vad heter du spelare 2?")
player2=input()
print("Hej", (player2), ", då börjar vi!")


def main():
     spelare = [player1, player2]
     starttal = 50
     while starttal > 0:
          for pp in spelare:
                print("totalt: ", starttal)
                while True:
                    player_choice = input(f"{pp} välj ett nummer att ta bort mellan 1-5: ")
                    if int(player_choice) > 5 or int(player_choice) < 1:
                        print("Felaktigt! Ange ett nummer mellan 1 och 5: ")
                    else:
                         break
                
                starttal -= int(player_choice)
                
                print (starttal)
                
                if starttal <= 0 and pp == player1:
                     print(pp, "har förlorat, ", player2, "har vunnit")
                elif starttal <= 0 and pp == player2:
                     print(pp, "har förlorat, ", player1, "har vunnit")
                break
main()