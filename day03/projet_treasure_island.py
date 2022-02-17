print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

road = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if road == "left":
    lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or type "swim" to swim accros. \n').lower()
    if lake == "wait":
        door = input("You arrive at the island. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if door == "yellow":
            print("You Win!")
        elif door == "red":
            print("Burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Your chose a door that doesn't exist. Game Over.")
    else:
        print("Attacked by an angry trout. Game Over.")
else:
    print("Fall into a hole")
