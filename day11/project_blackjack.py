import random
from art import logo

clearConsole = lambda: print('\n' * 50)

def deal_card():
    '''fonction pour retourner une carte aléatoire'''

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

'''Créez une fonction appelée calculate_score() qui prend une liste de cartes en entrée
#et renvoie le score.'''
def calculater_score(cards):

    '''À l'intérieur de calculate_score() vérifie s'il y a un blackjack (une main avec seulement 2 cartes :
    as + 10) et renvoie 0 au lieu du score réel. 0 représentera un blackjack dans notre jeu.'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    '''À l'intérieur de calculate_score(), vérifiez s'il y a un 11 (as). Si le score est déjà supérieur à 21, 
    supprimez le 11 et remplacez-le par un 1. Vous devrez peut-être rechercher append() et remove().'''
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

'''Créez une fonction appelée compare() et transmettez le user_score et le computer_score. Si l'ordinateur et 
l'utilisateur ont tous les deux le même score, alors c'est un match nul. Si l'ordinateur a un blackjack (0), alors 
l'utilisateur perd. Si l'utilisateur a un blackjack (0), alors l'utilisateur gagne. Si le user_score est supérieur à 21,
l'utilisateur perd. Si le computer_score est supérieur à 21, l'ordinateur perd. Si rien de ce qui précède, 
le joueur avec le score le plus élevé gagne.'''
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    print(logo)

    '''Distribuez à l'utilisateur et à l'ordinateur 2 cartes chacun en utilisant deal_card() et append()'''
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    '''The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated 
    until the game ends.'''
    while not is_game_over:
        '''Appelez calculate_score(). Si l'ordinateur ou l'utilisateur a un blackjack (0) 
        ou si le score de l'utilisateur est supérieur à 21, alors le jeu se termine.'''
        user_score = calculater_score(user_cards)
        computer_score = calculater_score(computer_cards)
        print(f" Your cards: {user_cards}, current scores: {user_score}")
        print(f" Computer's first card: {computer_cards[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            '''Si le jeu n'est pas terminé, demandez à l'utilisateur s'il veut piocher une autre carte. Si oui, 
            utilisez la fonction deal_card() pour ajouter une autre carte à la liste user_cards. Si non, alors le jeu est 
            terminé.'''
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    '''Une fois que l'utilisateur a terminé, il est temps de laisser l'ordinateur jouer.
     L'ordinateur doit continuer à tirer des cartes tant qu'il a un score inférieur à 17.'''
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculater_score(computer_cards)

    print(f" Yout final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play_again == "y":
    while play_again:
        clearConsole()
        play_game()














