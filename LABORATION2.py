#Import random-modulen som genererar slumpmässiga tal för valet av slumpord.
import random

#Den färdiga ordlistan från uppgiften med tillhörande betydelser.
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

#ASCII-grafik för den hängda gubben i 6 steg.
gubben = [
    """
      -----
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]

#Definition av slumpord: val av ord: returnanrop för betydelse av samma värde.
def slumpaOrd():
    slumpIndex = random.randint(0, len(ordlista) - 1)
    return ordlista[slumpIndex], betydelse[slumpIndex]

#Definition av "visa_gubben": print ASCII baserat på "antal misslyckade försök".
def visa_gubben(forsok):
    print(gubben[6 - forsok])

"""Definierar spelomgång: "slumpaOrd" ordval+beskrivning:
Valt ord defineras i lowercase: "gissad_bokstav" för bokstäver i valt ord"""
def spela_omgang():
    valt_ord, vald_beskrivning = slumpaOrd()
    valt_ord = valt_ord.lower()
    gissad_bokstav = ['_' for _ in valt_ord]
    attempts = 6                                #Antal tillåtna gissningar.
    gissat_fel = []                             #Lista för felaktiga gissningar.


    print("\nVälkommen till Hänga gubben!")
    print(" ".join(gissad_bokstav))

#Funktioner för återstående försök: fler än 0: antal försök kvar: tidigare gissningar.
    while attempts > 0 and '_' in gissad_bokstav:
        print(f"\nDu har {attempts} försök kvar.")
        print("Felaktiga gissningar: ", " ".join(gissat_fel))
        visa_gubben(attempts) #Visa gubben baserat på antalet försök.

        #Inputfunktion för bokstavsgissning.
        gissning = input("Gissa en bokstav: ").lower()

        #Felkontroll av inmatning av bokstavsgissning: felaktigt tecken och antal tecken.
        if not gissning.isalpha() or len(gissning) != 1:
            print("Ogiltigt val! Du måste gissa på en enda bokstav.")
            continue
        if gissning in gissat_fel or gissning in gissad_bokstav:    #felkontroll: redan gissat tecken.
            print(f"Du har redan gissat '{gissning}'!")
            continue

        #Kontrollera om bokstavsgissningen var korrekt: ´else´ "fel gissning.": runda dragen.
        if gissning in valt_ord:
            for i, letter in enumerate(valt_ord):
                if letter == gissning:
                    gissad_bokstav[i] = gissning
            print("\nBra gissning!")
        else:
            attempts -= 1
            gissat_fel.append(gissning)
            print(f"\nFel gissning! '{gissning}' finns inte i ordet.")

        #printfunktion för gissad bokstav
        print(" ".join(gissad_bokstav))

    #Definiera hängda gubben efter antal (försök).
    visa_gubben(attempts)

    #Print om spelaren vann eller förlorade och skriv ut valda ordet eller/och beskrivningen av ordet.
    if '_' not in gissad_bokstav:
        print(f"\nGrattis! Du gissade rätt och gubben lever vidare :). Ordet var '{valt_ord}' ({vald_beskrivning}).")
    else:
        print(f"\nTyvärr! Du har förlorat och gubben är hängd :(. Ordet var '{valt_ord}' ({vald_beskrivning}).")

#Spelavslut
def huvud_program():
    while True:
        spela_omgang()
        spela_igen = input("\nVill du spela igen? (ja/nej): ").lower()
        if spela_igen != 'ja':
            print("Tack för att du spelade!")
            break #if "nej" stänger/break programmet.

#Starta huvudprogrammet på nytt if "ja".
huvud_program()
