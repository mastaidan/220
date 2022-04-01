"""
Name: Aidan Mast
lab10.py

Problem: Create classes and use classes to create door GUI with button.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
from lab10.button import Button
from lab10.door import Door


def main():

    # creates window
    win = GraphWin("Test", 500, 500)
    win.setCoords(0, 0, 10, 10)

    # creates door and button
    button_shape = Rectangle(Point(3, 7), Point(7, 9))
    button = Button(button_shape, "Exit")
    door_shape = Rectangle(Point(3, 0), Point(7, 6.5))
    door = Door(door_shape, "")
    door.color_door("red")
    door.set_label("Closed")
    button.draw(win)
    door.draw(win)

    # controls door and button
    x = True
    count = 0
    while x:
        p = win.getMouse()
        if door.is_clicked(p):
            count = count + 1
            if count % 2:
                door.open("white", "Open")
            else:
                door.close("red", "Closed")
        if button.is_clicked(p):
            x = False
    win.close()


main()