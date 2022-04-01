"""
Name: Aidan Mast
hw3.py

Problem: Runs the numbers for several functions, providing averages, totals, and approximations.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""



def average():
    grade_amount = eval(input("how many grades.txt will you enter?"))
    total = 0
    for i in range(grade_amount):
        grade_value = eval(input("Enter grade:"))
        total = total + grade_value
    grade_average = total / grade_amount
    print("average is", grade_average)


def tip_jar():
    total = 0
    for i in range(5):
        tip = eval(input("how much would you like to donate?"))
        total = total + tip
    print("total tips:", total)


def newton():
    first_number = eval(input("what number do you want to square root?"))
    runs = eval(input("How many times should we improve the approximation?"))
    approximation = first_number
    for i in range(runs):
        approximation = (approximation + (first_number / approximation)) / 2
    print("the square root is approximately", approximation)



def sequence():
    terms = eval(input("how many terms would you like?"))
    for i in range(1, terms + 1):
        true_value = int((i + 1) / 2) * 2 - 1
        print(true_value, end=" ")



def pi():
    terms = eval(input("how many terms in the series?"))
    pie = 1
    for i in range(1, terms + 1):
        num = int((i + 1 ) / 2) * 2
        dum = int((i + 2) / 2) * 2 - 1
        pie = pie * (num / dum)
    print(pie * 2)


if __name__ == '__main__':
    pass
