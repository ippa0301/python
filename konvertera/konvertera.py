def konvertera_ord (input_string):
    converted=input_string[0].upper() + input_string[1:].lower() +"!"
    return converted

word = input("Skriv in ett ord du vill konvertera:  ")
konverterat_ord = konvertera_ord(word)
print(konverterat_ord)
