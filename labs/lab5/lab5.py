"""
Name: Aidan Mast
lab5.py

Problem: Draw things with and without user input, process lists, and run the numbers.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
from math import *


def triangle():
    win = GraphWin("Triangle", 700, 700)
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    tri = Polygon(point1, point2, point3)
    tri.setFill("green")
    tri.draw(win)
    message = Text(Point(350, 400), "Click again to close")
    perimeter_text = Text(Point(350, 550), "Perimeter")
    area_text = Text(Point(350, 600), "Area")
    side1 = sqrt((point1.getX() - point2.getX()) ** 2 + (point1.getY() - point2.getY()) ** 2)
    side2 = sqrt((point1.getX() - point3.getX()) ** 2 + (point1.getY() - point3.getY()) ** 2)
    side3 = sqrt((point2.getX() - point3.getX()) ** 2 + (point2.getY() - point3.getY()) ** 2)
    perimeter_value = side1 + side2 + side3
    s = perimeter_value / 2
    area_value = sqrt(s * (s - side1) * (s - side2) * (s - side3))
    perimeter_number = Text(Point(350, 575), perimeter_value)
    area_number = Text(Point(350, 625), area_value)
    message.draw(win)
    perimeter_text.draw(win)
    area_text.draw(win)
    perimeter_number.draw(win)
    area_number.draw(win)
    # pauses for user to close window
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_entry = Entry(Point(200, 240), 5)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_entry = Entry(Point(200, 270), 5)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_entry = Entry(Point(200, 300), 5)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    red_entry.draw(win)
    green_entry.draw(win)
    blue_entry.draw(win)

    # grabs color values and updates circle
    for i in range(5):
        win.getMouse()
        red_number = eval(red_entry.getText())
        green_number = eval(green_entry.getText())
        blue_number = eval(blue_entry.getText())
        shape.setFill(color_rgb(red_number, green_number, blue_number))
    inst.setText("\nClick window to close")

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    word = input("Enter a string: ")
    first = word[0]
    last = word[-1]
    firstlast = first + last
    number = word.count("") - 1
    print("First character:", first)
    print("Last character:", last)
    print("2-5 characters:", word[1:5])
    print("First and last characters:", firstlast)
    print("First three characters 10 times:")
    for i in range(10):
        print(word[0:3])
    print("Each separate character:")
    for i in range(number):
        letter = str(word[i])
        print(letter)
    print("The number of characters:", number)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, '7.2']
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    length = eval(input("How many terms?"))
    total = 0
    series = []
    for i in range(length):
        term = str((i % 3) * 2 + 2)
        series.append(term)
        total = total + int(term)
    a = list(series)
    print(" + ".join(series))
    print("sum =", total)


def target():
    win = GraphWin("Target", 700, 700)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green")
    center = Point(5, 5)
    white_circle = Circle(center, 5)
    white_circle.setFill("white")
    black_circle = Circle(center, 4)
    black_circle.setFill("black")
    blue_circle = Circle(center, 3)
    blue_circle.setFill("blue")
    red_circle = Circle(center, 2)
    red_circle.setFill("red")
    yellow_circle = Circle(center, 1)
    yellow_circle.setFill("yellow")
    white_circle.draw(win)
    black_circle.draw(win)
    blue_circle.draw(win)
    red_circle.draw(win)
    yellow_circle.draw(win)
    message = Text(Point(5, .5), "Click to close window")
    message.draw(win)
    win.getMouse()
    win.close()
