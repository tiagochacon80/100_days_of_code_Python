#Write a program that adds the digits in a 2 digit number. If you input was 35, then the output should be 3 + 5 = 8
two_digits_number = input("Type a number: ")
first_digit = int(two_digits_number[0]) #You separate the digits with the list [] and turn them into an integer
second_digit = int(two_digits_number[1])

result = first_digit + second_digit
print(result)


