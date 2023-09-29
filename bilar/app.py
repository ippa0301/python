import bil 

looping = True 

volvo_svart = bil.Bil("Volvo", "Svart", 3)
fiat_vit = bil.Bil("Fiat", "vit", 10)
bugatti_rosa = bil.Bil("Bugatti", "rosa", 1)

billista = [volvo_svart, fiat_vit, bugatti_rosa]


#print (f"första bilen i liste ={billista[2].fabrikat}")

while looping: 
    print(".....................................................")
    print("\n\t -:BilAutomat:- ")

    i=0


    for bil in billista:
        print(f"{i+1} : {bil.fabrikat} : {bil.color} : Antal={bil.lager}")
        i +=1

    bil_nr =input("\n Mata in siffra för vald bil: ")
    bil_nr_int = int(bil_nr)

    lager_int = billista[bil_nr_int-1].getLager()
    lager_string = str(lager_int)

    if lager_int > 0:
        print(f"\n En {billista[bil_nr_int-1].fabrikat} kommer här! ")

        nytt_lagersaldo_int = lager_int - 1
        nytt_lagersaldo_str = int(nytt_lagersaldo_int)

        billista[bil_nr_int-1].setLager(nytt_lagersaldo_int)

    go = input("Vill du avsluta programmet? j/n")

    if (go == "j"):
        break