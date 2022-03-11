#version 1
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

#version 2
print()
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)
