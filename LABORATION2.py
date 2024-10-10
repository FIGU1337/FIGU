#Ett program där användaren spelar spelet "Hänga Gubben".

import random #Importerar random-modulen som genererar slumpmässiga tal.

#Färdig ordlista och betydelser
ordlista = ["Vispgrädde", "Ukulele", "Innebandyspelare", "Flaggstång", "Yxa", "Havsfiske", "Prisma",
            "Landsbygd", "Generositet", "Lyckosam", "Perrong", "Samarbeta", "Välartad"]
betydelse = ["Uppvispad grädde",
             "Ett fyrsträngat instrument med ursprung i Portugal",
             "En person som spelar sporten innebandy",
             "En mast man hissar upp en flagga på",
             "Verktyg för att hugga ved",
             "Fiske till havs",
             "Ett transparent optiskt element som bryter ljuset vid plana ytor",
             "Geografiskt område med lantlig bebyggelse",
             "En personlig egenskap där man vill dela med sig av det man har",
             "Att man ofta, eller för stunden har tur",
             "Den upphöjda yta som passagerare väntar på eller stiger på/av ett spårfordon",
             "Att arbeta tillsammans mot ett gemensamt mål",
             "Att någon är väluppfostrad, skötsam, eller lovande"]

#ASCII-grafik för gubben med 6 steg (huvud, kropp, två armar, två ben)
gubben = [
    """
      -----
      |   |
          |
          |
          |
          |
    =========
    """,  #0 missar (tom gubbe)
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,  #1 miss (huvud)
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,  #2 missar (kropp)
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,  #3 missar (en arm)
    """
      -----
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,  #4 missar (två armar)
    """
      -----
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,  #5 missar (ett ben)
    """
      -----
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """   #6 missar (två ben, hela gubben är ritad)
]

#Funktion för att slumpa ett ord och dess betydelse
def slumpaOrd():
    slumpIndex = random.randint(0, len(ordlista) - 1)
    return ordlista[slumpIndex], betydelse[slumpIndex]

#Testa funktionen slumpaOrd
testOrd, testBetydelse = slumpaOrd()
print("Test av funktionen slumpaOrd:")
print(f"Ord: {testOrd}")
print(f"Betydelse: {testBetydelse}\n")

#Funktion för att visa gubben baserat på antal misslyckade försök
def visa_gubben(forsok):
    print(gubben[6 - forsok])

#Funktion för att spela en omgång
def spela_omgang():
    chosen_word, chosen_description = slumpaOrd()
    chosen_word = chosen_word.lower()  #Gör ordet till små bokstäver
    guessed_letters = ['_' for _ in chosen_word]
    attempts = 6  #Antal tillåtna gissningar
    guessed_wrong = []  #Lista för felaktiga gissningar

    print("\nVälkommen till Hänga gubben!")
    print(" ".join(guessed_letters))

    while attempts > 0 and '_' in guessed_letters:
        #Visa återstående försök och felaktiga gissningar
        print(f"\nDu har {attempts} försök kvar.")
        print("Felaktiga gissningar: ", " ".join(guessed_wrong))
        visa_gubben(attempts)  #Visa gubben baserat på antalet försök

        #Spelaren gissar en bokstav
        guess = input("Gissa en bokstav: ").lower()

        #Felkontroll för inmatning
        if not guess.isalpha() or len(guess) != 1:
            print("Ogiltigt val! Du måste gissa på en enda bokstav.")
            continue

        if guess in guessed_wrong or guess in guessed_letters:
            print(f"Du har redan gissat '{guess}'!")
            continue

        #Kontrollera om gissningen är korrekt
        if guess in chosen_word:
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    guessed_letters[i] = guess
            print("\nBra gissning!")
        else:
            attempts -= 1
            guessed_wrong.append(guess)
            print(f"\nFel gissning! '{guess}' finns inte i ordet.")

        #Visa det nuvarande ordet
        print(" ".join(guessed_letters))

    # Visa slutgiltiga versionen av gubben
    visa_gubben(attempts)

    #Kontrollera om spelaren vann eller förlorade och skriv ut beskrivningen av ordet
    if '_' not in guessed_letters:
        print(f"\nGrattis! Du gissade rätt och gubben lever vidare :). Ordet var '{chosen_word}' ({chosen_description}).")
    else:
        print(f"\nTyvärr, du har förlorat och gubben är hängd :(. Ordet var '{chosen_word}' ({chosen_description}).")

#Huvudprogrammet
def huvud_program():
    while True:
        spela_omgang()
        spela_igen = input("\nVill du spela igen? (ja/nej): ").lower()
        if spela_igen != 'ja':
            print("Tack för att du spelade!")
            break

#Starta huvudprogrammet
huvud_program()
