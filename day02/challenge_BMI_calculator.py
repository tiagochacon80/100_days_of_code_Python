weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in M: "))

bmi = weight / height ** 2
print("Your BMI is {:.2f}".format(bmi))


