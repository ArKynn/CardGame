import random
global deck, deck_p, deck_ai
deck = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck_p = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck_ai = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
check = 1

def shuffle():
    random.shuffle(deck_p)
    random.shuffle(deck_ai)

def fish(deck_a, deck_b):
    global cards_ai, cards_p
    cards_p = [deck_a[-1], deck_a[-2]]
    cards_ai = [deck_b[-1], deck_b[-2]]
    print(f"\nPlayer Cards: {cards_p}\nAI Cards: {cards_ai}\n")
    return cards_p, cards_ai

def compare():
    sum_p = (int(deck.index(cards_p[0])) + 1) + (int(deck.index(cards_p[1])) + 1)
    sum_ai = (int(deck.index(cards_ai[0])) + 1) + (int(deck.index(cards_ai[1])) + 1)

    if sum_p > sum_ai:
        print("O player venceu!")
    elif sum_p < sum_ai:
        print ("O AI venceu!")
    else:
        print ("O jogo empatou!")

def discard():
    global check
    while check == 1:
        try:
            ans = input()
            if int(ans) > 0 and int(ans) < 3:
                if int(ans) == 1:
                    deck_p.append(deck_p.pop(0))
                    fish(deck_p, deck_ai)
                    check = 0
                elif int(ans) == 2:
                    deck_p.append(deck_p.pop(0))
                    deck_p.append(deck_p.pop(0))
                    fish(deck_p, deck_ai)
                    check = 0
            elif int(ans) == 0:
                check = 0
            else:
                raise ValueError
        except ValueError:
            print("Introduza um número entre 0 e 2")
    del ans
while check>=0:
    shuffle()
    fish(deck_p, deck_ai)

    print(f"Deseja descartar alguma das suas cartas?\n(Respostas possiveis: 0, 1 ou 2)\n")
    discard()
    compare()
    check = 2
    while check == 2:
        fin=input("\nDeseja jogar novamente?\n(Sim? : s / Não? : n\n")
        try:
            if fin == "s":
                check = 1
                del fin
            elif fin == "n":
                check = -2
            else:
                raise ValueError
        except ValueError:
            print("Resposta não válida")