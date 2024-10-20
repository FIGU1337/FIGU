"""PSEUDOKOD

STARTA PROGRAM

IMPORTERA random

DEFINIERA lista med ord och betydelser

ASCIIgrafik för gubben

FUNKTIONSDEFINTION slumpaOrd:
    SLUMPA ett index
    RETURNA ord och betydelse

FUNKTIONSDEFINITION spelaomgang:
    SLUMPA ord och betydelse
    INITIERA gissade bokstäver och antal försök
    MEDAN försök > 0 OCH '' finns i gissade bokstäver:
        PRINTA försök kvar och felaktiga gissningar
        BE om gissning
        OM gissningen är giltig:
           OM rätt gissning:
                UPPDATERA gissade bokstäver
            ANNARS:
                MINSKA försök
        PRINTA aktuella gissade bokstäver
    PRINTA resultat

FUNKTIONSDEFINITION huvud_program:
    MEDAN SANT:
        KÖR spela_omgang
        BE om att spela igen
        OM inte "ja": AVSLUTA

STARTA huvud_program"""

import random 

#Färdig ordlista och betydelser.
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

#ASCII-grafik för gubben med 6 steg (huvud, kropp, två armar, två ben).
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

#Funktion för att slumpa ett ord och dess betydelse.
def slumpaOrd():
    slumpIndex = random.randint(0, len(ordlista) - 1)
    return ordlista[slumpIndex], betydelse[slumpIndex]

#Funktion för att visa gubben baserat på antal misslyckade försök.
def visa_gubben(forsok):
    print(gubben[6 - forsok])

#Funktion för att spela en omgång.
def spela_omgang():
    valt_ord, vald_beskrivning = slumpaOrd()
    valt_ord = valt_ord.lower() #Gör ordet till små bokstäver.
    gissad_bokstav = ['_' for _ in valt_ord]
    attempts = 6 #Antal tillåtna gissningar.
    gissat_fel = [] #Lista för felaktiga gissningar.

    print("\nVälkommen till Hänga gubben!")
    print(" ".join(gissad_bokstav))

    while attempts > 0 and '_' in gissad_bokstav:
        #Visa återstående försök och felaktiga gissningar.
        print(f"\nDu har {attempts} försök kvar.")
        print("Felaktiga gissningar: ", " ".join(gissat_fel))
        visa_gubben(attempts) #Visa gubben i ASCII-konst baserat på antalet försök.

        #Spelaren gissar en bokstav.
        gissning = input("Gissa en bokstav: ").lower()

        #Felkontroll för inmatning.
        if not gissning.isalpha() or len(gissning) != 1:
            print("Ogiltigt val! Du måste gissa på en enda bokstav.")
            continue

        if gissning in gissat_fel or gissning in gissad_bokstav:
            print(f"Du har redan gissat '{gissning}'!")
            continue

        #Kontrollera om gissningen är korrekt.
        if gissning in valt_ord:
            for i, letter in enumerate(valt_ord):
                if letter == gissning:
                    gissad_bokstav[i] = gissning
            print("\nBra gissning!")
        else:
            attempts -= 1
            gissat_fel.append(gissning)
            print(f"\nFel gissning! '{gissning}' finns inte i ordet.")

        #Visa det nuvarande ordet.
        print(" ".join(gissad_bokstav))

    #Visa slutgiltiga versionen av gubben.
    visa_gubben(attempts)

    #Kontrollera om spelaren vann eller förlorade och skriv ut beskrivningen av ordet.
    if '_' not in gissad_bokstav:
        print(f"\nGrattis! Du gissade rätt och gubben lever vidare :). Ordet var '{valt_ord}' ({vald_beskrivning}).")
    else:
        print(f"\nTyvärr! Du har förlorat och gubben är hängd :(. Ordet var '{valt_ord}' ({vald_beskrivning}).")

#Huvudprogrammet.
def huvud_program():
    while True:
        spela_omgang()
        spela_igen = input("\nVill du spela igen? (ja/nej): ").lower()
        if spela_igen != 'ja':
            print("Tack för att du spelade!")
            break

#Starta huvudprogrammet.
huvud_program()
