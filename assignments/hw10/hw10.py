"""
Name: Aidan Mast
hw10.py

Problem: Do loops without for loops. Also classes.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def fibonacci(number):
    if number < 1:
        return None
    count = 0
    old_total = 0
    new_total = 1
    total = 0
    while count < number:
        count = count + 1
        old_total = new_total
        new_total = total
        total = old_total + new_total
    return total


def double_investment(principle, rate):
    total = principle
    years = 0
    while total < principle * 2:
        years = years + 1
        total = total * (1 + rate)
    return years


def syracuse(number):
    syr = [number]
    while number != 1:
        if number % 2:
            number = (3 * number) + 1
            syr.append(number)
        else:
            number = number / 2
            syr.append(number)
    return syr


def goldbach(number):
    first = 1
    if number % 2:
        return None
    while first < number / 2:
        steve = 1
        first = first + 1
        second = number - first
        i = 3
        while steve:
            if first % i == 0 or second % i == 0:
                steve = 0
            if first % i != 0 or i > first:
                if second % i != 0 or i > second:
                    i = i + 1
            if i >= first and i >= second:
                return [first, second]
