print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? "))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = (percentage_tip / 100) + 1
total_person = (total_bill * tip_as_percent) / people
final_amount = round(total_person, 2)
print(f"Each person should pay: ${final_amount}")



