from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """Checks answer against guess. Return the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"Congratulation! You have a good answer {answer}!")

#Make function to set difficulty.
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Tape only 'easy' or 'hard'.")
        game()

def game():
    #Choosing a random number between 1 and 100.
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Correct answer {answer}")

    turns = set_difficulty()
    #Repeat the guessing functionality if they get it wrong.
    guess_number = 0
    while guess_number != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        #Track the number of turns and rescue by 1 if they get it wrong.
        guess_number = int(input("Make a guess: "))
        turns = check_answer(guess_number, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return

game()


