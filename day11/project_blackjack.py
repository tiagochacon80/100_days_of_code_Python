import random


def deal_card():
    '''fonction pour retourner une carte aléatoire'''

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


'''Distribuez à l'utilisateur et à l'ordinateur 2 cartes chacun en utilisant deal_card() et append()'''
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


'''Créez une fonction appelée calculate_score() qui prend une liste de cartes en entrée
#et renvoie le score.'''
def calculater_score(cards):

    '''À l'intérieur de calculate_score() vérifie s'il y a un blackjack (une main avec seulement 2 cartes :
    as + 10) et renvoie 0 au lieu du score réel. 0 représentera un blackjack dans notre jeu.'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0


    return sum(cards)


