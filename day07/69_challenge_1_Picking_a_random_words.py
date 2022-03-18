import random

from hangman_words import word_list

chosen_word = random.choice(word_list)

print(f"The word is {chosen_word}")

lives = 6

from hangman_art import logo
print(logo)

display = ["_" for letter in chosen_word]

print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")

    if guess in chosen_word:
        position = 0
        for letter in chosen_word:
            if guess == letter:
                display[position] = letter
            position += 1
    else:
        lives -= 1
        print(f"Wrong! {lives} lives left")
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"The word is {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won")


    from hangman_art import stages
    print(stages[lives])
