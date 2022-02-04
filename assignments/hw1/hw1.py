"""
Name: Aidan Mast
hw1.py

Problem: Use functions to run the numbers.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height"))
    volume = length * width * height
    print("Area =", volume)

def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    shot_percent = shots_made / total_shots * 100
    print("Shooting Percentage:", shot_percent)

def coffee():
    cof_lb = eval(input("How many pounds of coffee would you like?"))
    total = round(cof_lb * 11.36 + 1.50, 2)
    print("Your total is: $", total)

def kilometers_to_miles():
    kilo = eval(input("How many kilometers did you travel?"))
    mile = kilo / 1.61
    print("That's", mile, ("miles!"))


if __name__ == '__main__':
    pass
