#Ett program som tillåter spelaren att spela två olika spel.
#Detta program låter spelaren spela två olika spel och interagera med en huvudmeny.
#Syftet med att erbjuda användaren en enkel spelupplevelse där de kan välja mellan att visa skaparna, spela ett tärningspel elelr att gissa ett tal mellan 1 och 100.

#Används för att generera slumpmässiga tal och ett för att skapa tidsfördröjningar längre ner i koden.
import random
import time


bra_gissningar_i_rad = 0 #Används för att hålla koll på antal bra gissningar i rad, i spelet "Gissa telet".

def visa_hemskärm():
    print("Välkommen till Huvudmenyn!\n") #Visar huvudmenyn för att ge användaren följande valmöjligheter.

def visa_skaparna(): #Visar användaren vilka som ligger bakom grogrammet
    print("\nProgrammet är skapat av:")
    print("1. Filip Gustafsson")
    print("2. Maid Keranovic")
    print("3. Sahar Muradi")
    print("4. Leo Ramirez")

#ASCII-konst som visar ger spelaren en känsla av att kasta faktiska tärningar och får då en bättre spelupplevelse.
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

def spela_tärningsspel():
      
    spelare_poäng_per_runda = [] #
    bot_poäng_per_runda = [] #
    
    while True:
        rundor = input("Välkommen till Tärningsspelet! Hur många rundor vill du spela? (ange ett heltal): ")
        if not rundor.isdigit() or int(rundor) <= 0:
            print("Ange ett giltigt antal rundor större än 0.")
            continue

        rundor = int(rundor)
        spelare_score = 0 #
        bot_score = 0 #
        total_spelare_poäng = 0 #
        total_bot_poäng = 0 #

        for rundor_number in range(1, rundor + 1):
            print(f"\nRunda {rundor_number} av {rundor}")
            
            #
            input("Tryck Enter för att rulla dina två tärningar...")
            spelare_roll_1 = random.randint(1, 6)
            spelare_roll_2 = random.randint(1, 6)
            spelare_total_runda = spelare_roll_1 + spelare_roll_2
            spelare_poäng_per_runda.append(spelare_total_runda)
            print(f"Du fick {spelare_roll_1} och {spelare_roll_2}, totalt: {spelare_total_runda}!")
            print_tärning(spelare_roll_1)
            print_tärning(spelare_roll_2)
            
            #
            print("Boten rullar sina två tärningar...")
            time.sleep(2) #
            bot_roll_1 = random.randint(1, 6)
            bot_roll_2 = random.randint(1, 6)
            bot_total_runda = bot_roll_1 + bot_roll_2
            bot_poäng_per_runda.append(bot_total_runda)
            print(f"Boten fick {bot_roll_1} och {bot_roll_2}, totalt: {bot_total_runda}!")
            print_tärning(bot_roll_1)
            print_tärning(bot_roll_2)

            total_spelare_poäng += spelare_total_runda
            total_bot_poäng += bot_total_runda   

            if spelare_total_runda > bot_total_runda:
                print("Du vinner denna omgång!")
                spelare_score += 1
            elif spelare_total_runda < bot_total_runda:
                print("Boten vinner denna omgång!")
                bot_score += 1
            else:
                print("Det är oavgjort!")

        print("\nSlutresultat:")
        print(f"Du: {spelare_score} vunna rundor")
        print(f"Bot: {bot_score} vunna rundor")

        if spelare_score > bot_score:
            print(f"Du är den totala vinnaren med {spelare_score - bot_score} rundor!")
        elif spelare_score < bot_score:
            print(f"Boten är den totala vinnaren med {bot_score - spelare_score} rundor!")
        else:
            print("Spelet slutade oavgjort!")

        snitt_spelare_poäng = total_spelare_poäng / rundor
        snitt_bot_poäng = total_bot_poäng / rundor

        print("\nSnittpoäng per runda:")
        print(f"Din snittpoäng: {snitt_spelare_poäng:.1f}")
        print(f"Botens snittpoäng: {snitt_bot_poäng:.1f}")
        
        #
        bästa_poäng = max(spelare_poäng_per_runda)
        bästa_runda = spelare_poäng_per_runda.index(bästa_poäng) + 1

        sämsta_poäng = min(spelare_poäng_per_runda)
        sämsta_runda = spelare_poäng_per_runda.index(sämsta_poäng) + 1
        
        bästa_poäng_bot = max(bot_poäng_per_runda)
        bästa_runda_bot = bot_poäng_per_runda.index(bästa_poäng_bot) + 1

        sämsta_poäng_bot = min(bot_poäng_per_runda)
        sämsta_runda_bot = bot_poäng_per_runda.index(sämsta_poäng_bot) + 1

        #
        print(f"\nDin bästa runda var runda {bästa_runda} med {bästa_poäng} poäng.")
        print(f"Din sämsta runda var runda {sämsta_runda} med {sämsta_poäng} poäng.")
        
        print(f"Botens bästa runda var runda {bästa_runda_bot} med {bästa_poäng_bot} poäng.")
        print(f"Botens sämsta runda var runda {sämsta_runda_bot} med {sämsta_poäng_bot} poäng.")

        spela_igen = input("\nVill du spela igen? (ja/nej): ").lower()
        if spela_igen != "ja":
            print("Tack för att du spelade!")
            break

def spela_gissatalet():
    global bra_gissningar_i_rad #
    target_number = random.randint(1, 100)
    antal_försök = 0

    while True:
        gissning = input("Välkommen till Gissa talet! Gissa ett tal mellan 1 och 100: ")
        if not gissning.isdigit():
            print("Vänligen ange ett giltigt tal!")
            continue

        gissning = int(gissning)
        antal_försök += 1

        if gissning < target_number:
            print("För lågt!")
        elif gissning > target_number:
            print("För högt!")
        else:
            print(f"Grattis! Du gissade rätt efter {antal_försök} försök.")
            if antal_försök <= 7:
                print("Bra jobbat!")
                bra_gissningar_i_rad += 1
            else:
                print("Så många försök borde det inte ta, försök igen.")
                bra_gissningar_i_rad = 0

            if bra_gissningar_i_rad >= 3:
                print("Du använder bevisligen en bra gissningsstrategi!")

            break

#
while True:
    visa_hemskärm()
    print("1: Visa skaparna")
    print("2: Spela Tärningsspelet")
    print("3: Spela Gissa talet")
    print("4: Avsluta")

    val = input("Välj ett alternativ (1-4): ")

    if val == '1':
        visa_skaparna()
    elif val == '2':
        spela_tärningsspel()
    elif val == '3':
        spela_gissatalet()
    elif val == '4':
        print("Avslutar spelet...")
        break
    else:
        print("Ogiltigt val, försök igen.")