import random

def print_tabla(tabla):
    for row in tabla:
        print(" | ".join(row))
        print("---------")


def verif_castigator(tabla):
    for i in range(3):
        # Verifica daca randurile sunt identice si folosite
        if tabla[i][0] == tabla[i][1] == tabla[i][2] != " ":
            return tabla[i][0]
        # Verifica daca coloanele sunt identice si folosite
        if tabla[0][i] == tabla[1][i] == tabla[2][i] != " ":
            return tabla[0][i]
    # Verifica daca diagonalele sunt identice si folosite
    if tabla[0][0] == tabla[1][1] == tabla[2][2] != " ":
        return tabla[0][0]
    if tabla[0][2] == tabla[1][1] == tabla[2][0] != " ":
        return tabla[0][2]
    return None


def xsi0():
    tabla = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    jucator_curent = "X"

    while True:
        print_tabla(tabla)

        while True:
            try:
                row = int(input("Alege randul (1,2,3): "))
                col = int(input("Alege coloana (1,2,3): "))

                if not (0 < row <= 3) or not (0 < col <= 3):
                    print("Ai ales randul sau coloana gresit. Te rog alege din nou randul si coloana")
                    continue

                if tabla[row-1][col-1] != " ":
                    print("Deja exista o valoare in aceasta casuta. Te rog alege din nou randul si coloana")
                    continue

                break
            except ValueError:
                print("Poti introduce doar numere la randuri si coloane. Te rog incearca din nou")

        tabla[row-1][col-1] = jucator_curent

        winner = verif_castigator(tabla)
        if winner:
            print_tabla(tabla)
            print("Jucatorul", winner, "castiga!")
            break

        # Schimb jucatori
        jucator_curent = "O" if jucator_curent == "X" else "X"

        # VerificamEgalitate
        if all(tabla[i][j] != " " for i in range(3) for j in range(3)):
            print_tabla(tabla)
            print("Este egalitate")
            break


def calc_hand(hand):
    total_value = 0
    num_aces = 0

    # Calculeaza valoarea fiecarei carte
    for card in hand:
        if card.isdigit():
            total_value += int(card)
        elif card in ["J", "Q", "K"]:
            total_value += 10
        elif card == "A":
            total_value += 11
            num_aces += 1

    # Ajustare valoare asi
    while total_value > 21 and num_aces > 0:
        total_value -= 10
        num_aces -= 1

    return total_value

def deal_card():
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    # Returnam un card random din lista
    return random.choice(cards)

def gameover():
    joci_iar_sau_nu = input("Vrei sa joci iar? (Da/Nu): ").lower()
    if joci_iar_sau_nu == "da":
        return 1
    elif joci_iar_sau_nu== "nu":
        return 2

        return None

def blackjack():
    print("Bine ati venit la Blackjack!")

    # Initializare hand la jucator si dealer
    hand_jucator = []
    dealer_hand = []


    bani = 20
    castiguri = 0
    pierderi = 0
    egalitati = 0

    # Main game loop
    while True:
        print("Banii tai: ", bani)
        if bani < 5:
            print("Ai ramas fara bani. La revedere!")
            break

        # Dam doua carti random la jucator si dealer
        hand_jucator.append(deal_card())
        dealer_hand.append(deal_card())
        hand_jucator.append(deal_card())
        dealer_hand.append(deal_card())

        # Se muta pe True cand e gata jocul
        game_over = False


        while not game_over:

            print("Mana ta:", hand_jucator, "Valoare totala:", calc_hand(hand_jucator))

            # Arata doar prima carte a dealerului
            print("Mana dealer:", [dealer_hand[0], "???"])


            if calc_hand(hand_jucator) == 21:
                print("Blackjack! Ai castigat!")
                bani += 5
                castiguri += 1
                game_over = True
                break


            alegere = input("Ce alegi? (Hit/Stand): ").lower()

            if alegere == "hit":

                hand_jucator.append(deal_card())


                if calc_hand(hand_jucator) > 21:
                    print("Bust! Ai pierdut!")
                    bani -= 5
                    pierderi += 1
                    game_over = True
            elif alegere == "stand":

                while calc_hand(dealer_hand) < 17:
                    dealer_hand.append(deal_card())


                print("Mana dealer:", dealer_hand, "Valoare totala:", calc_hand(dealer_hand))


                if calc_hand(dealer_hand) > 21:
                    print("Dealer bust! Ai castigat!")
                    bani += 2
                    castiguri += 1
                elif calc_hand(dealer_hand) > calc_hand(hand_jucator):
                    print("Dealer castiga!")
                    bani -= 5
                    pierderi += 1
                elif calc_hand(dealer_hand) < calc_hand(hand_jucator):
                    print("Ai castigat!")
                    bani += 2
                    castiguri += 1
                else:
                    print("Egalitate!")
                    bani -=3
                    egalitati +=1

                game_over = True

        if game_over:

            jociar=gameover()
            if jociar==1:
                # Resetare maini pentru urmatorul joc
                hand_jucator = []
                dealer_hand = []
            elif jociar==2:
                print("La revedere!")
                break
            else:
                while jociar!=1 and jociar!=2:
                    jociar = gameover()
                    if jociar == 1:
                        hand_jucator = []
                        dealer_hand = []
                    elif jociar == 2:
                        print("La revedere!")
                        break
                if jociar == 1:
                    # Resetare maini pentru urmatorul joc
                    hand_jucator = []
                    dealer_hand = []
                elif jociar == 2:
                    print("La revedere!")
                    break            
    print("Castiguri:", castiguri)
    print("Pierderi:", pierderi)
    print("Egalitati:", egalitati)

def joc_pahare():
    print("Ghiceste unde se afla piatra: 1, 2, sau 3")
    print("Scrie exit pentru a iesi din joc.")

    bani = 20
    castiguri = 0
    pierderi = 0

    while True:
        if bani < 5:
            print("Nu mai ai bani, la revedere!")
            print("castiguri: ", castiguri)
            print("pierderi: ", pierderi)
            break

        pahare = [' ', ' ', ' ']
        undei_piatra = random.randint(1, 3)
        pahare[undei_piatra - 1] = 'O'

        while True:
            pariu = input("Alegerea ta: ")
            if pariu.lower() == "exit":
                print("La revedere!")
                break
            elif pariu in ["1", "2", "3"]:
                break
            else:
                print("Alegere invalida. Te rog alege din nou.")

        if pariu.lower() == "exit":
            break

        print("Ai ales", pariu)
        print("Uite unde se afla:")
        print("  |  ".join(pahare))

        bani -= 5

        if pariu == str(undei_piatra):
            print("GG! Ai gasit piatra")
            bani += 8
            castiguri += 1
        else:
            print("Nu ai gasit piatra, mult noroc data viitoare")
            pierderi += 1

        print("Banii tai: $", bani)
        print("castiguri: ", castiguri)
        print("pierderi: ", pierderi)
        print("-----------------------------")

        jociar = gameover()
        if jociar == 2:
            print("La revedere!")
            break
        else:
            while jociar != 1 and jociar != 2:
                jociar = gameover()
                if jociar == 2:
                    print("La revedere!")
                    break
            if jociar == 2:
                break

def arunc_zar():
    return random.randint(1, 6)

def joc_zar():
    joc_iar_sau_nu_joc_iar = True

    while joc_iar_sau_nu_joc_iar:
        scor_juc1 = 0
        scor_juc2 = 0
        runde = 5

        while runde > 0:
            print(f"\nRound {6 - runde}:")


            input("Jucator 1, apasa enter sa arunci zarurile...")
            zar1 = arunc_zar()
            zar2 = arunc_zar()
            total = zar1 + zar2
            print(f"Jucator 1 a obtinut {zar1} si {zar2}. Total: {total}")
            if total % 2 == 0:
                print("Par! Jucator 1 castiga 10 puncte.")
                scor_juc1 += 10
            else:
                print("Impar! Jucator 1 pierde 5 puncte.")
                scor_juc1 -= 5


            input("Jucator 2, apasa enter sa arunci zarurile...")
            zar1 = arunc_zar()
            zar2 = arunc_zar()
            total = zar1 + zar2
            print(f"Jucator 2 a obtinut {zar1} si {zar2}. Total: {total}")
            if total % 2 == 0:
                print("Par! Jucator 2 castiga 10 puncte.")
                scor_juc2 += 10
            else:
                print("Impar! Jucator 2 pierde 5 puncte.")
                scor_juc2 -= 5

            runde -= 1

            if runde > 0:
                jociarzar = gameover()
                if jociarzar == 2:
                    print("La revedere!")
                    break
                else:
                    while jociarzar != 1 and jociarzar != 2:
                        jociarzar = gameover()
                        if jociarzar == 2:
                            print("La revedere!")
                            break
                    if jociarzar == 2:
                        break

        # Check for a tie and play additional runde if necessary
        while scor_juc1 == scor_juc2:
            print("\nEgalitate! Rundele decisive urmeaza...")
            input("Apasa enter sa arunci zarurile, jucator 1...")
            zar1 = arunc_zar()
            zar2 = arunc_zar()
            total = zar1 + zar2
            print(f"Jucator 1 a obtinut {zar1} si {zar2}. Total: {total}")
            if total % 2 == 0:
                print("Par! Jucator 1 castiga 10 puncte.")
                scor_juc1 += 10
            else:
                print("Impar! Jucator 1 pierde 5 puncte.")
                scor_juc1 -= 5

            input("Apasa enter sa arunci zarurile, jucator 2...")
            zar1 = arunc_zar()
            zar2 = arunc_zar()
            total = zar1 + zar2
            print(f"Jucator 2 a obtinut {zar1} si {zar2}. Total: {total}")
            if total % 2 == 0:
                print("Par! Jucator 2 castiga 10 puncte.")
                scor_juc2 += 10
            else:
                print("Impar! Jucator 2 pierde 5 puncte.")
                scor_juc2 -= 5

        print("\nJocul s-a terminat!")
        print("Scor jucator 1:", scor_juc1)
        print("Scor jucator 2:", scor_juc2)
        print("Jucatorul", "1 castiga!" if scor_juc1 > scor_juc2 else "2 castiga!")

        jociarzar = gameover()
        if jociarzar == 2:
            print("La revedere!")
            joc_iar_sau_nu_joc_iar = False
            break
        else:
            while jociarzar != 1 and jociarzar != 2:
                jociarzar = gameover()
                if jociarzar == 2:
                    joc_iar_sau_nu_joc_iar = False
                    print("La revedere!")
                    break
            if jociarzar == 2:
                joc_iar_sau_nu_joc_iar = False
                break




while True:
    print("Alege jocul dorit:")
    print("1. X si 0")
    print("2. Blackjack")
    print("3. Ghiceste unde se afla piatra")
    print("4. Joc zar 1v1")
    print("5. Iesi din meniu")

    alegere = input("Alege jocul dorit (1-4): ")

    if alegere == "1":
        xsi0()
    elif alegere == "2":
        blackjack()
    elif alegere == "3":
        joc_pahare()
    elif alegere == "4":
        joc_zar()
    elif alegere == "5":
        print("Sa aveti o zi buna!")
        break
    else:
        print("Optiunea nu exista. Te rog alege din nou.")

    print("----------------------------------")