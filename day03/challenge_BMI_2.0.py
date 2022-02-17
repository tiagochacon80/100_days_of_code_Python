#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#It should tell them the interpretation of their BMI based on the BMI value.

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slighty overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obesse.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

