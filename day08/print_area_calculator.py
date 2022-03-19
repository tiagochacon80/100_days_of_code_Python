import math

def paint_calc(height, width, cover):
    area = height * width
    numbers_of_can = area / cover
    round_up = int(math.ceil(numbers_of_can))
    print(f"You'll need {round_up} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)