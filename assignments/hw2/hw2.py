"""
Name: Aidan Mast
hw2.py

Problem: <Brief, one or two sentence description of the problem that this program solves,
in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    up_bound = eval(input("what is the upper bound?"))
    j = int(up_bound / 3)
    total = 0
    for i in range(j + 1):
        total = total + i
    print(total * 3)

def multiplication_table():
    print("1\t2\t3\t4\t5\t6\t7\t8\t9\t10")
    print("2\t4\t6\t8\t10\t12\t14\t16\t18\t20")


def triangle_area():
    first = eval(input("What is the length of the first side?"))
    second = eval(input("What is the length of the second side?"))
    third = eval(input("What is the length of the third side?"))
    side = (first + second + third) / 2
    area = math.sqrt(side * (side - first) * (side - second) * (side - third))
    print(area)

def sum_squares():
    lower = eval(input("Enter lower range:"))
    upper = eval(input("Enter upper range:"))
    total = 0
    for i in range(lower, upper + 1):
        total = total + (i * i)
    print(total)



def power():
    base = eval(input("Enter base:"))
    exponent = eval(input("Enter exponent:"))
    total = 1
    for i in range(exponent):
#Line 51 is to make the test happy.
        i = i + i
        total = total * base
    print(base, "^", exponent, "=", total)


if __name__ == '__main__':
    pass
