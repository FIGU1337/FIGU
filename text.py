import random

def spela_gissatalet(bra_gissningar_i_rad=0):
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
    
    return bra_gissningar_i_rad

# Exempel på hur man kan köra spelet
bra_gissningar_i_rad = 0
while True:
    bra_gissningar_i_rad = spela_gissatalet(bra_gissningar_i_rad)
    spela_igen = input("Vill du spela igen? (ja/nej): ").lower()
    if spela_igen != 'ja':
        break
