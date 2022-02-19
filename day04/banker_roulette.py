import random

names_string = input("Give me everybody's names, separated by a coma. \n")

names = names_string.split(", ")

numbers_names = len(names)#len() nous donne le compriment/quantité des noms dans notre liste name[]

number_chosen = random.randint(0, numbers_names-1)#Après trouvé la quantité avec len() nous allons diminuer de -1 pour trouver le dernier élément de la liste

chosen = names[number_chosen]

print(chosen)
