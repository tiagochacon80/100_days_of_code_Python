import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"The word is {chosen_word}")

display = ["_" for letter in chosen_word]

print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    position = 0
    for letter in chosen_word:
        if guess == letter:
            display[position] = letter
        position += 1

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You won")








