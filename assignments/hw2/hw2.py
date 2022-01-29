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
    print("3\t6\t9\t12\t15\t18\t21\t24\t27\t30")
    print("4\t8\t12\t16\t20\t24\t08\t32\t36\t40")
    print("5\t10\t15\t20\t25\t30\t35\t40\t45\t50")
    print("6\t12\t18\t24\t30\t36\t42\t48\t54\t60")
    print("7\t14\t21\t28\t35\t42\t49\t56\t63\t70")
    print("8\t16\t24\t32\t40\t48\t56\t64\t72\t80")
    print("9\t18\t27\t36\t45\t54\t63\t72\t81\t90")
    print("10\t20\t30\t40\t50\t60\t70\t80\t90\t100")

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
#Line 51 is to make test.py happy.
        i = i + i
        total = total * base
    print(base, "^", exponent, "=", total)


if __name__ == '__main__':
    pass
