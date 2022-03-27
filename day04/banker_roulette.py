from random import randint

names = input("Give me everybody's names, separated by a coma.\n")

names_separated = names.split(", ")

compriment = len(names_separated)

random_choises = randint(0, compriment - 1)

friend_chosen = names_separated[random_choises]

print(f"Who will pay the bill? {friend_chosen}")



