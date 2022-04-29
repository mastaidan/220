"""
Name: Aidan Mast
lab12.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def read_data(filename):
    file = open(filename, "r")
    text = file.readlines()
    text = " ".join(text).split("\n")
    text = " ".join(text).split(" ")
    while text.count(""):
        text.remove("")
    return text


def is_in_linear(search_val, values):
    x = False
    c = 0
    while not x:
        x = values[c] == search_val
        c += c
        if search_val == int(values[-1]) + 1:
            return False
    return True

