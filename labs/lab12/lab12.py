"""
Name: Aidan Mast
lab12.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from algorithms import *
from random import randint


def find_and_remove_first(list, value):
    while list.count(value):
        pos = list.index(value)
        list.insert(pos, "Aidan")
        list.remove(value)
        return list
    return list


def good_input():
    number = eval(input("Enter a number 1-10"))
    while not 1 <= number <= 10:
        number = eval(input("Invalid number. Make sure your number is in the range 1-10"))
    return number


def num_digits():
    number = eval(input("Input a positive number to count the digits. Input a negative number or 0 to close."))
    while number > 0:
        digits = 0
        while number > 0:
            number //= 10
            digits += 1
        print(digits)
        number = eval(input("Enter another number."))
    return


def hi_lo_game():
    number = randint(1, 100)
    guesses = 0
    while guesses < 7:
        guess = eval(input("There is a number 1-100, try to guess it."))
        if guess > number:
            print("too high")
            guesses += 1
        elif guess < number:
            print("too low")
            guesses += 1
        elif guess < 1 or guess > 100:
            print("Invalid number. Make sure it is between 1 and 100.")
        else:
            print("correct, you won in {} moves".format(guesses + 1))
            return
    print("Sorry, you lose. The number was {}".format(number))
    return



def main():
    hi_lo_game()


main()
