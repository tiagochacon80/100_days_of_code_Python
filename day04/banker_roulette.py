from random import randint

names = input("Give me everybody's names, separated by a coma.\n")
names_separated = names.split(', ')

compriment = len(names_separated)

random_choice = randint(0, compriment - 1)

friend_chosen = names_separated[random_choice]

print((f"Who will pay de the bill? {friend_chosen}"))


