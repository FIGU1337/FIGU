
#Pythons inbyggda modul för att generera slumpmässiga tal.
import random
import time  # Importerar time-modulen för att använda sleep.

def visa_hemskärm():
    print("Välkommen ")

#Funktion för att visa tärningen baserat på det slumpmässiga talet. Visas med så kallat "ASCII-konst". 
def print_tärning(number):
    tärning_sidor = {
        1: ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
        3: ("┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
        5: ("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"),
        6: ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")
    }
    for line in tärning_sidor[number]:
        print(line)

#Huvudprogrammet
while True:
    #Frågar spelaren hur många rundor de vill spela.
    rundor = input("Hur många rundor vill du spela? (ange ett heltal): ")
    if not rundor.isdigit() or int(rundor) <= 0:
        print("Ange ett giltigt antal rundor större än 0.")
        continue

    rundor = int(rundor)
    spelare_score = 0  #Antal vunna rundor för spelaren.
    bot_score = 0  #Antal vunna rundor för boten.
    total_spelare_poäng = 0  #Summerad poäng för alla tärningskast för spelaren.
    total_bot_poäng = 0  #Summerad poäng för alla tärningskast för boten.

    #Kör spelet i det angivna antalet rundor.
    for rundor_number in range(1, rundor + 1):
        print(f"\nRunda {rundor_number} av {rundor}")
        
        #Spelaren rullar två tärningar.
        input("Tryck Enter för att rulla dina två tärningar...")
        spelare_roll_1 = random.randint(1, 6)
        spelare_roll_2 = random.randint(1, 6)
        spelare_total = spelare_roll_1 + spelare_roll_2
        print(f"Du fick {spelare_roll_1} och {spelare_roll_2}, totalt: {spelare_total}!")
        print_tärning(spelare_roll_1)
        print_tärning(spelare_roll_2)

        #Boten rullar två tärningar automatiskt.
        print("Boten rullar sina två tärningar...")
        time.sleep(1)
        bot_roll_1 = random.randint(1, 6)
        bot_roll_2 = random.randint(1, 6)
        bot_total = bot_roll_1 + bot_roll_2
        print(f"Boten fick {bot_roll_1} och {bot_roll_2}, totalt: {bot_total}!")
        print_tärning(bot_roll_1)
        print_tärning(bot_roll_2)

        #Uppdaterar totalpoäng för spelaren och boten.
        total_spelare_poäng += spelare_total
        total_bot_poäng += bot_total

        #Bestämmer vinnaren av omgången och uppdaterar antalet vunna rundor.
        if spelare_total > bot_total:
            print("Du vinner denna omgång!")
            spelare_score += 1
        elif spelare_total < bot_total:
            print("Boten vinner denna omgång!")
            bot_score += 1
        else:
            print("Det är oavgjort!")

    #Visar slutresultatet efter alla rundor.
    print("\nSlutresultat:")
    print(f"Du: {spelare_score} vunna rundor")
    print(f"Bot: {bot_score} vunna rundor")

    #Jämför vem som vann totalt och visar med hur många rundor.
    if spelare_score > bot_score:
        print(f"Du är den totala vinnaren med {spelare_score - bot_score} rundor!")
    elif spelare_score < bot_score:
        print(f"Boten är den totala vinnaren med {bot_score - spelare_score} rundor!")
    else:
        print("Spelet slutade oavgjort!")

    #Beräknar och visar snittpoängen per runda för spelaren och boten.
    snitt_spelare_poäng = total_spelare_poäng / rundor
    snitt_bot_poäng = total_bot_poäng / rundor

    print("\nSnittpoäng per runda:")
    print(f"Din snittpoäng: {snitt_spelare_poäng:.2f}")
    print(f"Botens snittpoäng: {snitt_bot_poäng:.2f}")

    #Frågar om spelaren vill spela igen.
    play_again = input("\nVill du spela igen? (ja/nej): ").lower()
    if play_again != "ja":
        print("Tack för att du spelade!")
        break  #Avslutar loopen om svaret inte är 'ja'.
