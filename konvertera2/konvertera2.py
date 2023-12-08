vowels = 'AOUÅÄÖIY'

def konvertera_ord(word):
    converted = word.upper()
    for char in vowels:
        converted = converted.replace(char, "E")
    return converted

word = input("Skriv in ett ord du vill konvertera: ")
resultat = konvertera_ord(word)
print(f"Här är resultatet: {resultat}")

