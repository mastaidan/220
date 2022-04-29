"""
Name: Aidan Mast
lab12.py

Problem: Manipulate lists, numbers, and make games without using for loops.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import Rectangle, Point


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
        if values[c] == search_val:
            x = True
        c += c
        if c > len(values):
            return False
    return True


def selection_sort(values):
    length = len(values)
    for bottom in range(length - 1):
        mp = bottom
        for i in range(bottom + 1, length):
            if values[i] < values[mp]:
                mp = i
            values[bottom], values[mp] = values[mp], values[bottom]
    return values


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    return abs(p1.getX() - p2.getX()) * abs(p1.getY() - p2.getY())


def rect_sort(rectangles):
    length = len(rectangles)
    for bottom in range(length - 1):
        mp = bottom
        for i in range(bottom + 1, length):
            if calc_area(rectangles[i]) < calc_area(rectangles[mp]):
                mp = i
            rectangles[bottom], rectangles[mp] = rectangles[mp], rectangles[bottom]
    return rectangles
