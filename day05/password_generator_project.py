import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassord Generator!")

number_letters = int(input("How many letters would you like in your password?\n "))

nb_numbers = int(input("How many numbers would like in your password?\n "))

numbers_symbols = int(input("How many symbols would like in your password?\n"))

password_list = []

for c in range(1, number_letters + 1):
    password_list.append(random.choice(letters))

for c in range(1, nb_numbers + 1):
    password_list += random.choice(numbers)

for c in range(1, numbers_symbols +1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for c in password_list:
    password += c

print(f"\033[93mYour password is: {password}")

