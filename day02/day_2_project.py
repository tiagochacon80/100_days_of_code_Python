print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
people_split = int(input("How many people to split the bill? "))
percentage_tip = int(input("What a percentage tip would you like to give? 10, 15 or 20 "))
tip_calculation_percentage = ((percentage_tip / 100) + 1)
value_each_person = (total_bill * tip_calculation_percentage) / people_split
final_amount = round(value_each_person, 2)
final_amount = "{:.2f}".format(value_each_person)
print(f"Each person should pay: ${final_amount}")