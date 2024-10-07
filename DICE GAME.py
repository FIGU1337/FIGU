
# Pythons inbyggda modul för att generera slumpmässiga tal och göra andra slumpmässiga operationer.
import random

# Funktion för att visa tärningen baserat på det slumpmässiga talet. Visas med så kallat "ASCII-konst".
def print_dice(number):
    dice_faces = {
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
    for line in dice_faces[number]:
        print(line)

# Huvudprogrammet
while True:
    # Frågar spelaren hur många rundor de vill spela.
    rounds = input("Hur många rundor vill du spela? (ange ett heltal): ")
    if not rounds.isdigit() or int(rounds) <= 0:
        print("Ange ett giltigt antal rundor större än 0.")
        continue

    rounds = int(rounds)
    player_score = 0  # Antal vunna rundor för spelaren.
    bot_score = 0  # Antal vunna rundor för boten.
    total_player_points = 0  # Summerad poäng för alla tärningskast för spelaren.
    total_bot_points = 0  # Summerad poäng för alla tärningskast för boten.

    # Kör spelet i det angivna antalet rundor.
    for round_number in range(1, rounds + 1):
        print(f"\nRunda {round_number} av {rounds}")
        
        # Spelaren rullar två tärningar.
        input("Tryck Enter för att rulla dina två tärningar...")
        player_roll_1 = random.randint(1, 6)
        player_roll_2 = random.randint(1, 6)
        player_total = player_roll_1 + player_roll_2
        print(f"Du fick {player_roll_1} och {player_roll_2}, totalt: {player_total}!")
        print_dice(player_roll_1)
        print_dice(player_roll_2)

        # Boten rullar två tärningar automatiskt.
        print("Boten rullar sina två tärningar...")
        bot_roll_1 = random.randint(1, 6)
        bot_roll_2 = random.randint(1, 6)
        bot_total = bot_roll_1 + bot_roll_2
        print(f"Boten fick {bot_roll_1} och {bot_roll_2}, totalt: {bot_total}!")
        print_dice(bot_roll_1)
        print_dice(bot_roll_2)

        # Uppdaterar totalpoäng för spelaren och boten.
        total_player_points += player_total
        total_bot_points += bot_total

        # Bestämmer vinnaren av omgången och uppdaterar antalet vunna rundor.
        if player_total > bot_total:
            print("Du vinner denna omgång!")
            player_score += 1
        elif player_total < bot_total:
            print("Boten vinner denna omgång!")
            bot_score += 1
        else:
            print("Det är oavgjort!")

    # Visar slutresultatet efter alla rundor.
    print("\nSlutresultat:")
    print(f"Du: {player_score} vunna rundor")
    print(f"Bot: {bot_score} vunna rundor")

    # Jämför vem som vann totalt och visar med hur många rundor.
    if player_score > bot_score:
        print(f"Du är den totala vinnaren med {player_score - bot_score} rundor!")
    elif player_score < bot_score:
        print(f"Boten är den totala vinnaren med {bot_score - player_score} rundor!")
    else:
        print("Spelet slutade oavgjort!")

    # Beräknar och visar snittpoängen per runda för spelaren och boten.
    avg_player_points = total_player_points / rounds
    avg_bot_points = total_bot_points / rounds

    print("\nSnittpoäng per runda:")
    print(f"Din snittpoäng: {avg_player_points:.2f}")
    print(f"Botens snittpoäng: {avg_bot_points:.2f}")

    # Frågar om spelaren vill spela igen.
    play_again = input("\nVill du spela igen? (ja/nej): ").lower()
    if play_again != "ja":
        print("Tack för att du spelade!")
        break  # Avslutar loopen om svaret inte är 'ja'.
