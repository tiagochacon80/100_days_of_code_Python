print("Welcome to the Love Calculator")

name1 = str(input("What is your name? \n"))
name2 = str(input("What is their name? \n"))

combined_string = name1 + name2
lower_case_str = combined_string.lower()

t = lower_case_str.count("t")
r = lower_case_str.count("r")
u = lower_case_str.count("u")
e = lower_case_str.count("e")

true = t + r + u + e

l = lower_case_str.count("l")
o = lower_case_str.count("o")
v = lower_case_str.count("v")
e = lower_case_str.count("e")

love = l + o + v + e

score = int(str(true) + str(love))

if (score < 10) or (score > 90):
    print(f"Your love score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your love score is {score}, your are alright together.")
else:
    print(f"Your score is {score}.")
