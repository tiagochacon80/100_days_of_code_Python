import random

coin = input('Do you chose "Heads" or "Tails" \n')
if coin == "Heads" or coin == "Tails":
    choise = random.randint(0, 1)
    if choise == 1:
        print(choise, "Heads")
    else:
        print(choise, "Tails")
else:
    print("Invalid, you need to enter the first capital letter, as in the example.")