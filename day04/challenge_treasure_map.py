row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
if position > "33":
    print("You can only use numbers in the range 11 to 33, example: 11, 12, 21, 32...")
else:
    horizonal = int(position[0])#Variable initialisé pour prendre la position inicial de la ligne horizontale
    vertical = int(position[1])#Variable initialisé pour prendre la position inicial de la colonne verticale

    map[vertical - 1][horizonal - 1] = "X" #Position ou le "X", sera mis, moins 1 (-1) sera le split.

    print(f"{row1}\n{row2}\n{row3}")

