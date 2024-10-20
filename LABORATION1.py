#Detta program låter spelaren spela två olika spel och interagera med en huvudmeny.
#Syftet med att erbjuda användaren en enkel spelupplevelse där de kan välja mellan att visa skaparna, spela ett tärningspel elelr att gissa ett tal mellan 1 och 100.

#Importmoduler för hantering av slumpmässiga tal respektive tidshantering.import random
import random
import time

#Räkning för antal bra gissningar i rad, funktion för spelet "Gissa talet".
bra_gissningar_i_rad = 0

#Funktionen huvudmeny: print välkomstmeddelande
def visa_huvudmenyn():
    print("Välkommen till Huvudmenyn!\n") 

#Definierar menyval 1 "visa skaparna", print skaparna av programmet.
def visa_skaparna():
    print("\nProgrammet är skapat av:")
    print("1. Filip Gustafsson")
    print("2. Maid Keranovic")
    print("3. Leo Ramirez")

#ASCII-konst som visar tärningar för Tärningsspelet.
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
    
    #Funktion som väljer rätt tärning baserat på slagen siffra 1-6.: Print
    for line in tärning_sidor[number]:
        print(line)

#Definerar valet "Tärningspelet"
def spela_tärningsspel():
    #Variabler för poängräkning av rundor.
    spelare_poäng_per_runda = []
    bot_poäng_per_runda = []

    while True:

        #Funktion input av antal rundor spelaren väljer.
        rundor = input("Välkommen till Tärningsspelet! Hur många rundor vill du spela? (ange ett heltal): ")
        if not rundor.isdigit() or int(rundor) <= 0:  #Inputkontroll: är en siffra som väljs: större än 0.
            print("Ange ett giltigt antal rundor större än 0.")
            continue

        #Konverterar variabeln rundor från str till heltal (integer).
        rundor = int(rundor)

        #Funktioner för poänguträkning: Runda respektive total.
        spelare_score = 0
        bot_score = 0
        total_spelare_poäng = 0
        total_bot_poäng = 0

        #Forloopen som exekverar att spelet körs inom "range + 1" antal rundor.
        for rundor_number in range(1, rundor + 1):
            print(f"\nRunda {rundor_number} av {rundor}")

            """Inputfunktion för att kasta tärningen - tryck enter:
            randintmodul för beräkning av tärningskast:
            summering av poängen för kastet. Runda respektive poängtotal. 
            Tärningsansikten visas i ASCII-konst."""
            input("Tryck Enter för att rulla dina två tärningar...")
            spelare_roll_1 = random.randint(1, 6)
            spelare_roll_2 = random.randint(1, 6)
            spelare_total_runda = spelare_roll_1 + spelare_roll_2
            spelare_poäng_per_runda.append(spelare_total_runda)
            print(f"Du fick {spelare_roll_1} och {spelare_roll_2}, totalt: {spelare_total_runda}!")
            print_tärning(spelare_roll_1)
            print_tärning(spelare_roll_2)

            """Funktion för botens kast - print visar det är botens tur:
            Timemodul för en mindre fördröjning på botens kast:
            randintmodul för beräkning av tärningskast:
            summering av poängen för kastet. Runda respektive poängtotal. 
            Tärningsansikten visas i ASCII-konst."""
            print("Boten rullar sina två tärningar...")
            time.sleep(2)
            bot_roll_1 = random.randint(1, 6)
            bot_roll_2 = random.randint(1, 6)
            bot_total_runda = bot_roll_1 + bot_roll_2
            bot_poäng_per_runda.append(bot_total_runda)
            print(f"Boten fick {bot_roll_1} och {bot_roll_2}, totalt: {bot_total_runda}!")
            print_tärning(bot_roll_1)
            print_tärning(bot_roll_2)

            # Totalpoäng för spelet: Spelare respektive bot.
            total_spelare_poäng += spelare_total_runda
            total_bot_poäng += bot_total_runda

            #Beräkning av poäng per runda. if Spelare elif bot vinner: else oavgjort.
            if spelare_total_runda > bot_total_runda:
                print("Du vinner denna omgång!")
                spelare_score += 1
            elif spelare_total_runda < bot_total_runda:
                print("Boten vinner denna omgång!")
                bot_score += 1
            else:
                print("Det är oavgjort!")
        #Printfunktioner för spelresultat/rundor: slutgiltig poäng spelomgång: antal vunna rundor.
        print("\nSlutresultat:")
        print(f"Du: {spelare_score} vunna rundor")
        print(f"Bot: {bot_score} vunna rundor")

        #Printfunktioner totalt spelresultat.
        if spelare_score > bot_score:
            print(f"Du är den totala vinnaren med {spelare_score - bot_score} rundor!")
        elif spelare_score < bot_score:
            print(f"Boten är den totala vinnaren med {bot_score - spelare_score} rundor!")
        else:
            print("Spelet slutade oavgjort!")

        #Variabler och Printfunktioner för spelarens respektive botens snittpoängen till en decimal.
        snitt_spelare_poäng = total_spelare_poäng / rundor
        snitt_bot_poäng = total_bot_poäng / rundor
        print("\nSnittpoäng per runda:")
        print(f"Din snittpoäng: {snitt_spelare_poäng:.1f}")
        print(f"Botens snittpoäng: {snitt_bot_poäng:.1f}")

        #Variabler uträkning av vilken runda som var spelaren sämsta respektive bästa.
        bästa_poäng = max(spelare_poäng_per_runda)
        bästa_runda = spelare_poäng_per_runda.index(bästa_poäng) + 1
        sämsta_poäng = min(spelare_poäng_per_runda)
        sämsta_runda = spelare_poäng_per_runda.index(sämsta_poäng) + 1
        # Variabler uträkning av vilken runda som var botens sämsta respektive bästa.
        bästa_poäng_bot = max(bot_poäng_per_runda)
        bästa_runda_bot = bot_poäng_per_runda.index(bästa_poäng_bot) + 1
        sämsta_poäng_bot = min(bot_poäng_per_runda)
        sämsta_runda_bot = bot_poäng_per_runda.index(sämsta_poäng_bot) + 1

        #Printfunktion som talar om resultatet av ovannämnda variabler.
        print(f"\nDin bästa runda var runda {bästa_runda} med {bästa_poäng} poäng.")
        print(f"Din sämsta runda var runda {sämsta_runda} med {sämsta_poäng} poäng.")
        print(f"Botens bästa runda var runda {bästa_runda_bot} med {bästa_poäng_bot} poäng.")
        print(f"Botens sämsta runda var runda {sämsta_runda_bot} med {sämsta_poäng_bot} poäng.")

        # Inputfunktion där spelaren för välja att spela igen eller att avsluta spelet.
        spela_igen = input("\nVill du spela igen? (ja/nej): ").lower()
        if spela_igen != "ja":
            print("Tack för att du spelade!")
            break
        
#Definerar funktionen från menyvalet "Gissa talet".
def spela_gissatalet():
    global bra_gissningar_i_rad #Modul som håller koll på hur många gånger spelaren gör en bra gissning (under 6 försök) i rad.
    target_number = random.randint(1, 100) #Används till att generera ett slumpat tal, för var omgång.
    antal_försök = 0
    tidigare_gissat = set() #Operation för att omgångsbaserat spara tidigare gissade tal. 
    
    #Whileloop som håller igång spelet tills spelaren har gissat rätt tal.
    while True:
        gissning = input("Välkommen till Gissa talet! Gissa ett tal mellan 1 och 100: ")
        if not gissning.isdigit(): #Kontroll för giltig inmatning: isdigit
            print("Vänligen ange ett giltigt tal!")
            continue

        gissning = int(gissning) #Gissning "isdigit" konverteras till en integer.
        
        #Sats för kontroll av gissning: undviker tidigare gissning.
        if gissning in tidigare_gissat:
            print(f"Du har redan gissat på det talet {gissning}, försök med ett annat tal!")
            continue

        tidigare_gissat.add(gissning) #Variabeln som ser till att "gissning" läggs i set (kontrollräkning).
        antal_försök += 1

        #Satser som kontrollerar om det gissade talet är för lågt, högt eller är rätt: Tillhörande printfunktioner.
        if gissning < target_number:
            print("För lågt!")
        elif gissning > target_number:
            print("För högt!")
        else: # Kontroll för om antal rätt gissningar håller sig inom satt variabel för att klassas som en "bra gissningsstrategi".
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
        
"""Det bör aldrig ta fler än 7 gissningar, även om vi jobbar från 1-200,
 då om vi halverar antal möjligheter nog antal gånger så bör vi komma fram till rätt svar på 7 gissningar. 
 Detta kallas i finare termer en binärsökning."""

#Whileloopen för huvudmenyn, den är igång tills att användaren väljer ett av alternativen (1-4). 
while True:
    visa_huvudmenyn()
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