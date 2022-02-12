"""
Name: Aidan Mast
hw3.py

Problem: Runs the numbers for several functions, providing averages, totals, and approximations.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import graphics
import math


def squares():
    win = graphics.GraphWin("Clicks", 700, 700)
    instruct = graphics.Text(graphics.Point(350, 675), "Click to draw a square")
    instruct.draw(win)
    for i in range(6):
        user_point = win.getMouse()
        user_point_clone = user_point.clone()
        user_point.move(25, 25)
        user_point_clone.move(-25, -25)
        square = graphics.Rectangle(user_point, user_point_clone)
        square.setFill("red")
        square.setOutline("white")
        square.draw(win)
    close_message = graphics.Text(graphics.Point(350, 400), "Click again to close")
    close_message.draw(win)
    win.getMouse()
    win.close()


def rectangle():  # uses user input to make rectangle, then returns perimeter and area
    win = graphics.GraphWin("Click", 700, 700)
    point1 = win.getMouse()
    point2 = win.getMouse()
    rect = graphics.Rectangle(point1, point2)
    rect.setFill("green")
    rect.draw(win)
    message = graphics.Text(graphics.Point(350, 400), "Click again to close")
    perimeter_text = graphics.Text(graphics.Point(350, 550), "Perimeter")
    area_text = graphics.Text(graphics.Point(350, 600), "Area")
    side1 = abs(point1.getX() - point2.getX())
    side2 = abs(point1.getY() - point2.getY())
    perimeter_value = (side1 * 2) + (side2 * 2)
    area_value = side1 * side2
    perimeter_number = graphics.Text(graphics.Point(350, 575), perimeter_value)
    area_number = graphics.Text(graphics.Point(350, 625), area_value)
    message.draw(win)
    perimeter_text.draw(win)
    area_text.draw(win)
    perimeter_number.draw(win)
    area_number.draw(win)
    win.getMouse()
    win.close()


def circle():
    win = graphics.GraphWin("Circle", 700, 700)
    center = win.getMouse()
    edge = win.getMouse()
    radius = math.sqrt((center.getX() - edge.getX()) ** 2 + (center.getY() - edge.getY()) ** 2)
    circle1 = graphics.Circle(center, radius)
    circle1.setFill("light blue")
    message = graphics.Text(graphics.Point(350, 400), "Click again to close")
    radius_text = graphics.Text(graphics.Point(350, 625), "Radius")
    radius_number = graphics.Text(graphics.Point(350, 650), radius)
    circle1.draw(win)
    message.draw(win)
    radius_text.draw(win)
    radius_number.draw(win)
    win.getMouse()
    win.close()


def pi2():
    n = eval(input("enter the number of terms to sum: "))
    total = 0

    for i in range(n):
        num = 4
        dum = i * 2 + 1
        oddeven = i % 2
        total = total + (num / dum) - (num / dum * oddeven) * 2
    acc = abs(math.pi - total)
    print("pi approximation:", total)
    print("accuracy: ", acc)


