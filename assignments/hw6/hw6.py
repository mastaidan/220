"""
Name: Aidan Mast
hw6.py

Problem: Create functions with parameters and encode stuff.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from math import pi


def cash_converter():
    amount = eval(input("enter an integer:"))
    print("That is ${}.00".format(amount))


def encode():
    message = input("enter a message:")
    key = eval(input("enter a key:"))
    message_length = len(message)
    uni_message = []
    coded_message = []
    for index in range(message_length):
        coded_value = ord(message[index]) + key
        uni_message.append(coded_value)
    for index in range(message_length):
        coded_chr = chr(uni_message[index])
        coded_message.append(coded_chr)
    print("".join(coded_message))


def sphere_area(radius):
    return 4 * pi * radius * radius


def sphere_volume(radius):
    return 4 / 3 * pi * radius ** 3


def sum_n(number):
    total = 0
    for i in range(number + 1):
        total = total + i
    return total


def sum_n_cubes(number):
    total = 0
    for i in range(number + 1):
        total = total + pow(i, 3)
    return total


def encode_better():
    org_message = input("enter a message:")
    org_key = input("enter a key:")
    message_length = len(org_message)
    key_length = len(org_key)
    number_message = []
    number_key = []
    coded_ord_message = []
    coded_message = []
    for index in range(message_length):
        number_letter = ord(org_message[index]) - 65
        number_message.append(number_letter)
    for index in range(key_length):
        number_letter = ord(org_key[index]) - 65
        number_key.append(number_letter)
    for i in range(message_length):
        repeat_key_values = i % len(org_key)
        coded_number = number_message[i] + number_key[repeat_key_values]
        coded_ord_message.append(coded_number)
    for i in range(message_length):
        number = coded_ord_message[i] % 58
        letter = chr(number + 65)
        coded_message.append(letter)
    print("".join(coded_message))


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
