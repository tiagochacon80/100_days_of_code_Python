from random import randint

#Function to check user's guess against actual answer.
def check_answer():

#Choosing a random number between 1 and 100.
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)


#Make function to set difficulty.

#Let the user guess a number.
guess_number = int(input("Make a guess: "))