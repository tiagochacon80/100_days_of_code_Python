print("Welcome to the rollercoaster")
height = int(input("What is your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 7
        print("Please pay 5$")
    elif age <= 18:
        bill = 12
        print("Please pay 7")
    elif age >= 45 and age <= 55:
        print("It's free!!")
    else:
        print("Adult tickets are 12$")

    photo = input("Do you want a photo taken? Y or N ")
    if photo == 'Y':
        bill += 3
        print(f"Your bill with the photo is {bill}$")
else:
    print("Sorry, you have to grow taller before you can ride.")