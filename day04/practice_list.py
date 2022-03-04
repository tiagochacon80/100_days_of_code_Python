#Quand nous voulons imprimer un item de la liste
names = ["Tiago", "Rafael", "Andreza", "Alexia", "Joshua", "Agrio", "Cristina", "Socorro", "Zito"]
print(names[7])

#Quand nous voulons identifier le dernier item de la liste
people = len(names) #Prendre la compriment de la liste, dans ce cas 9
print(names[people - 1]) #nous renvoie la dernière position de la liste

#Une liste dans l'autre liste
fruits = ["Morango", "Nectarina", "Marça", "Uva", "Pessego", "Pera", "Tomate"]#Liste 0
vegetables = ["Espinafri", "kale", "Celery", "Potatoes", "alface"]#Liste 1

dirty_dozen = [fruits, vegetables]#Nous avons mis deux liste dans une liste
print(dirty_dozen)
print(dirty_dozen[1][3])#Nous renvoie le string dans la liste 1, position 3 - "Potatoes"


