"""
Name: Aidan Mast
hw4.py

Problem: Create interactable windows that create images when clicked, and estimate pi.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math

def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw a square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(25, 25), Point(75, 75))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        user_point = win.getMouse()
        user_point_clone = user_point.clone()
        user_point.move(25, 25)
        user_point_clone.move(-25, -25)
        square = Rectangle(user_point, user_point_clone)
        square.setFill("red")
        square.setOutline("white")
        square.draw(win)

    # displays close message
    close_message = Text(Point(200, 200), "Click again to close")
    close_message.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    # creates window
    win = GraphWin("Rectangle", 700, 700)
    # creates rectangle by grabbing points from user
    point1 = win.getMouse()
    point2 = win.getMouse()
    rect = Rectangle(point1, point2)
    rect.setFill("green")
    rect.draw(win)
    # create messages
    message = Text(Point(350, 400), "Click again to close")
    perimeter_text = Text(Point(350, 550), "Perimeter")
    area_text = Text(Point(350, 600), "Area")
    # calculates area and perimeter
    side1 = abs(point1.getX() - point2.getX())
    side2 = abs(point1.getY() - point2.getY())
    perimeter_value = (side1 * 2) + (side2 * 2)
    area_value = side1 * side2
    perimeter_number = Text(Point(350, 575), perimeter_value)
    area_number = Text(Point(350, 625), area_value)
    # draws objects
    message.draw(win)
    perimeter_text.draw(win)
    area_text.draw(win)
    perimeter_number.draw(win)
    area_number.draw(win)
    # pauses for user to close window
    win.getMouse()
    win.close()


def circle():
    # creates window
    win = GraphWin("Circle", 700, 700)
    # user input to find center and radius
    center = win.getMouse()
    edge = win.getMouse()
    radius = math.sqrt((center.getX() - edge.getX()) ** 2 + (center.getY() - edge.getY()) ** 2)
    # creates circle
    circle1 = Circle(center, radius)
    circle1.setFill("light blue")
    # creates instructions and radius info
    message = Text(Point(350, 400), "Click again to close")
    radius_text = Text(Point(350, 625), "Radius")
    radius_number = Text(Point(350, 650), radius)
    # draws objects
    circle1.draw(win)
    message.draw(win)
    radius_text.draw(win)
    radius_number.draw(win)
    # pauses for user to close window
    win.getMouse()
    win.close()


def pi2():
    # asks for total terms
    terms = eval(input("enter the number of terms to sum: "))
    total = 0
    # loops to find pi
    for i in range(terms):
        # defines fraction and adds/subtracts
        num = 4
        dum = i * 2 + 1
        oddeven = i % 2
        total = total + (num / dum) - (num / dum * oddeven) * 2
    acc = abs(math.pi - total)
    # prints totals and accuracy
    print("pi approximation:", total)
    print("accuracy: ", acc)


if __name__ == '__main__':
    pass
